"""HFSS automation helper for TFLN traveling-wave electrode modulators.

Run on Windows host with AEDT 2022 R1 + PyAEDT installed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from ansys.aedt.core import Desktop, Hfss


def db_per_cm_from_s21(s21_mag: np.ndarray, length_mm: float) -> np.ndarray:
    """Convert |S21| to RF loss (dB/cm) using a uniform-line approximation."""
    length_cm = length_mm / 10.0
    eps = 1e-15
    return -20.0 * np.log10(np.maximum(s21_mag, eps)) / length_cm


def extract_line_metrics(freq_hz: np.ndarray, s21_complex: np.ndarray, length_mm: float):
    """Estimate RF attenuation and effective microwave index from S21 phase."""
    c0 = 299_792_458.0
    phase = np.unwrap(np.angle(s21_complex))
    beta = -phase / (length_mm * 1e-3)
    n_rf = beta * c0 / (2 * np.pi * freq_hz)
    rf_loss_db_cm = db_per_cm_from_s21(np.abs(s21_complex), length_mm)
    return rf_loss_db_cm, n_rf


def summarize_design(hfss: Hfss) -> dict:
    return {
        "project": hfss.project_name,
        "design": hfss.design_name,
        "solution_type": hfss.solution_type,
        "setups": list(hfss.setups),
        "boundaries": list(hfss.boundaries.keys()),
        "excitations": list(hfss.excitations.keys()),
        "materials": sorted(hfss.materials.material_keys.keys()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exe", required=True, help="Full path to ansysedt.exe")
    parser.add_argument("--project", required=True, help=".aedt project path")
    parser.add_argument("--design", default=None, help="HFSS design name")
    parser.add_argument("--setup", default="Setup1")
    parser.add_argument("--sweep", default="Sweep1")
    parser.add_argument("--line-length-mm", type=float, default=10.0)
    parser.add_argument("--n-optical", type=float, default=2.20)
    parser.add_argument("--run-analyze", action="store_true")
    parser.add_argument("--out", default="hfss_tfln_audit.json")
    args = parser.parse_args()

    with Desktop(specified_version="2022.1", non_graphical=False, new_desktop_session=True,
                 close_on_exit=True, student_version=False, aedt_process_id=None,
                 port=None, machine=None, remove_lock=True, executable=args.exe):
        hfss = Hfss(project=args.project, design=args.design)

        if args.run_analyze:
            hfss.analyze_setup(args.setup)

        report_expr = ["S(2,1)"]
        sol_data = hfss.post.get_solution_data(
            expressions=report_expr,
            setup_sweep_name=f"{args.setup} : {args.sweep}",
            domain="Sweep",
        )
        freq = np.array(sol_data.primary_sweep_values, dtype=float)
        s21 = np.array(sol_data.data_complex(report_expr[0]), dtype=complex)

        rf_loss_db_cm, n_rf = extract_line_metrics(freq, s21, args.line_length_mm)
        delta_n = n_rf - args.n_optical
        # first index where mismatch within +-0.05 as practical criterion
        idx = np.where(np.abs(delta_n) <= 0.05)[0]
        vel_match_ghz = float(freq[idx[-1]] / 1e9) if len(idx) else None

        z_expr = "Z0(1)"
        z_data = hfss.post.get_solution_data(
            expressions=[z_expr],
            setup_sweep_name=f"{args.setup} : {args.sweep}",
            domain="Sweep",
        )
        z0 = np.array(z_data.data_complex(z_expr), dtype=complex)

        summary = summarize_design(hfss)
        summary["metrics"] = {
            "freq_ghz": (freq / 1e9).tolist(),
            "rf_loss_db_per_cm": rf_loss_db_cm.tolist(),
            "n_rf": n_rf.tolist(),
            "n_optical": args.n_optical,
            "delta_n": delta_n.tolist(),
            "velocity_match_band_edge_ghz": vel_match_ghz,
            "z0_real_ohm": np.real(z0).tolist(),
            "z0_imag_ohm": np.imag(z0).tolist(),
        }

        Path(args.out).write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(f"Saved report: {args.out}")


if __name__ == "__main__":
    main()
