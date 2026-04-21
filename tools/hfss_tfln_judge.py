"""Judge TFLN traveling-wave electrode model quality from HFSS audit JSON files.

Input JSON files are expected to come from tools/hfss_tfln_workflow.py.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np


@dataclass
class JudgeConfig:
    z0_target: float = 50.0
    z0_tol_ohm: float = 3.0
    z0_imag_max: float = 3.0
    delta_n_max: float = 0.05
    rf_loss_max_db_cm: float = 0.5
    report_points_ghz: Tuple[float, ...] = (40.0, 67.0, 110.0)


def _interp(freq_ghz: np.ndarray, values: np.ndarray, f0: float) -> float:
    if f0 <= freq_ghz[0]:
        return float(values[0])
    if f0 >= freq_ghz[-1]:
        return float(values[-1])
    return float(np.interp(f0, freq_ghz, values))


def _find_edge(freq_ghz: np.ndarray, mask: np.ndarray) -> float | None:
    valid = np.where(mask)[0]
    if valid.size == 0:
        return None
    return float(freq_ghz[valid[-1]])


def evaluate(metrics: Dict, cfg: JudgeConfig) -> Dict:
    f = np.asarray(metrics["freq_ghz"], dtype=float)
    rf_loss = np.asarray(metrics["rf_loss_db_per_cm"], dtype=float)
    z0r = np.asarray(metrics["z0_real_ohm"], dtype=float)
    z0i = np.asarray(metrics["z0_imag_ohm"], dtype=float)
    dn = np.asarray(metrics["delta_n"], dtype=float)

    pass_rf = rf_loss <= cfg.rf_loss_max_db_cm
    pass_z0 = (np.abs(z0r - cfg.z0_target) <= cfg.z0_tol_ohm) & (np.abs(z0i) <= cfg.z0_imag_max)
    pass_vm = np.abs(dn) <= cfg.delta_n_max
    pass_all = pass_rf & pass_z0 & pass_vm

    rf_edge = _find_edge(f, pass_rf)
    z0_edge = _find_edge(f, pass_z0)
    vm_edge = _find_edge(f, pass_vm)
    ee_edge = _find_edge(f, pass_all)

    points = {}
    for p in cfg.report_points_ghz:
        points[str(int(p))] = {
            "rf_loss_db_cm": _interp(f, rf_loss, p),
            "z0_real_ohm": _interp(f, z0r, p),
            "z0_imag_ohm": _interp(f, z0i, p),
            "delta_n": _interp(f, dn, p),
        }

    return {
        "pass": {
            "rf_loss": bool(np.all(pass_rf)),
            "impedance": bool(np.all(pass_z0)),
            "velocity_matching": bool(np.all(pass_vm)),
            "full_band": bool(np.all(pass_all)),
        },
        "edges_ghz": {
            "rf_loss": rf_edge,
            "impedance": z0_edge,
            "velocity_matching": vm_edge,
            "ee_bandwidth_est": ee_edge,
        },
        "points": points,
    }


def recommendations(result: Dict) -> List[str]:
    recs: List[str] = []
    e = result["edges_ghz"]
    p = result["pass"]

    if not p["rf_loss"]:
        recs.append(
            "RF loss 超标：优先加厚/换低电阻率金属（Au/Cu）、缩短电极、优化信号-地间隙与回流路径，并检查导电率与表面粗糙度模型。"
        )
    if not p["impedance"]:
        recs.append(
            "阻抗不匹配：以 50Ω 为目标，联调信号线宽 W、间隙 G、金属厚度 T；必要时增厚缓冲层/调整接地宽度。"
        )
    if not p["velocity_matching"]:
        recs.append(
            "速度失配：通过改变电极几何（W/G/T）和缓冲层厚度调 n_RF，使其接近光学群折射率 n_g。"
        )
    if p["rf_loss"] and p["impedance"] and p["velocity_matching"]:
        recs.append("当前频段内三项均满足阈值，可进一步在系统级验证 EO S21 与 Vπ·L。")

    if e["ee_bandwidth_est"] is not None:
        recs.append(f"按当前阈值估计 EE 带宽上边界约为 {e['ee_bandwidth_est']:.2f} GHz。")
    else:
        recs.append("按当前阈值未找到可用 EE 带宽区间，请先修正模型与参数。")
    return recs


def render(name: str, result: Dict) -> str:
    p = result["pass"]
    e = result["edges_ghz"]
    lines = [f"## {name}"]
    lines.append(
        f"- 结论: RF loss={'PASS' if p['rf_loss'] else 'FAIL'}, "
        f"Impedance={'PASS' if p['impedance'] else 'FAIL'}, "
        f"Velocity matching={'PASS' if p['velocity_matching'] else 'FAIL'}, "
        f"Full-band={'PASS' if p['full_band'] else 'FAIL'}"
    )
    lines.append(
        f"- 频段边界(GHz): RF loss={e['rf_loss']}, Z0={e['impedance']}, "
        f"Velocity={e['velocity_matching']}, EE估计={e['ee_bandwidth_est']}"
    )
    lines.append("- 关键频点:")
    for f0, vals in result["points"].items():
        lines.append(
            f"  - {f0} GHz: loss={vals['rf_loss_db_cm']:.3f} dB/cm, "
            f"Z0={vals['z0_real_ohm']:.2f}+j{vals['z0_imag_ohm']:.2f} Ω, "
            f"Δn={vals['delta_n']:.4f}"
        )
    for rec in recommendations(result):
        lines.append(f"- 建议: {rec}")
    return "\n".join(lines)


def load_json(path: str) -> Dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--coplanar", required=True)
    ap.add_argument("--confinement", required=True)
    ap.add_argument("--out", default="hfss_judgement_report.md")
    args = ap.parse_args()

    cfg = JudgeConfig()
    cop = load_json(args.coplanar)
    con = load_json(args.confinement)

    cop_result = evaluate(cop["metrics"], cfg)
    con_result = evaluate(con["metrics"], cfg)

    content = [
        "# TFLN 行波电极模型判定报告",
        "",
        "判定阈值：|Z0-50|<=3Ω, |Im(Z0)|<=3Ω, |Δn|<=0.05, RF loss<=0.5 dB/cm",
        "",
        render("Coplanar 示例", cop_result),
        "",
        render("Confinement 示例", con_result),
        "",
    ]
    Path(args.out).write_text("\n".join(content), encoding="utf-8")
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
