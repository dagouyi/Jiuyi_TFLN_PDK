# 使用 HFSS (AEDT 2022 R1) 验证行波电极 TFLN 调制器的流程（含 Python 自动化）

> 说明：当前自动化脚本面向你给出的 AEDT 可执行程序 `C:\Program Files\AnsysEM\v221\Win64\ansysedt.exe`。

## 1) 先在本机定位 Python

在 Windows `CMD` 执行：

```bat
where python
py -0p
```

如果输出多个 Python，建议固定到 3.10/3.11 的一个解释器，并记录绝对路径。

## 2) 安装 PyAEDT（在你选定的 Python 下）

```bat
"<你的python.exe路径>" -m pip install --upgrade pip
"<你的python.exe路径>" -m pip install pyaedt numpy
```

## 3) 用 Python 调用 HFSS 打开示例工程

仓库中已提供脚本：`tools/hfss_tfln_workflow.py`。

### 示例 1：只审计模型与设置（不重算）

```bat
"<你的python.exe路径>" tools\hfss_tfln_workflow.py ^
  --exe "C:\Program Files\AnsysEM\v221\Win64\ansysedt.exe" ^
  --project "C:\Users\jZhang\Desktop\Coplanar_waveguide_with_results_jiuyi.aedt" ^
  --design "HFSSDesign1" ^
  --setup "Setup1" --sweep "Sweep1" ^
  --line-length-mm 10 --n-optical 2.20 ^
  --out "coplanar_audit.json"
```

### 示例 2：审计 + 重新求解

```bat
"<你的python.exe路径>" tools\hfss_tfln_workflow.py ^
  --exe "C:\Program Files\AnsysEM\v221\Win64\ansysedt.exe" ^
  --project "C:\Users\jZhang\Desktop\confinement_factor_caculation (1).aedt" ^
  --design "HFSSDesign1" ^
  --setup "Setup1" --sweep "Sweep1" ^
  --line-length-mm 10 --n-optical 2.20 ^
  --run-analyze ^
  --out "confinement_audit.json"
```

## 4) 关键指标定义与 HFSS 对应提取

- **RF loss (dB/cm)**：由 `|S21|` 按线长换算得到，脚本内公式：
  \(\alpha_{\mathrm{dB/cm}} = -20\log_{10}|S21|/L_{\mathrm{cm}}\)。
- **Characteristic impedance**：直接读取 `Z0(1)`（实部接近 50Ω，虚部尽可能小）。
- **Velocity matching**：由 `S21` 相位提取微波有效折射率 \(n_{\mathrm{RF}}\)，与光学群折射率 \(n_g\) 对比；脚本输出 `delta_n = n_RF - n_optical`。
- **EO 带宽（工程近似）**：若满足 `|delta_n| <= 0.05` 到某频点，可作为速度匹配主导的上边界参考。最终仍需与系统级 TWE/Interconnect 联合验证。

## 5) 你两个示例文件的“可用性”检查清单

请用脚本导出的 JSON 对照以下条目：

1. `solution_type` 是否为驱动端口传输线求解（Driven Modal/Terminal，按你的建模口径）。
2. `setups`/`sweep` 是否覆盖目标频段（例如 1–110 GHz）。
3. `excitations` 是否为差分端口/共面波导端口正确定义。
4. `boundaries` 是否含辐射边界或 PML（避免高频虚假反射）。
5. 网格是否对电极边缘和间隙加密（否则 Z0 和损耗误差明显）。
6. 材料中金属导电率、LN 各向异性介电常数、衬底损耗角正切是否与工艺一致。

若以上任意一项不满足，RF loss / Z0 / velocity matching / EE 带宽结论都会偏差。

## 6) 推荐的仿真流程（HFSS + 光学协同）

1. 光学模式解算得到 `n_g` 与重叠因子（MODE/FDE 等）。
2. HFSS 提取传输线 `S` 参数、`Z0(f)`、`n_RF(f)`、`alpha_RF(f)`。
3. 在系统级（如 Ansys INTERCONNECT 的 Traveling Wave Electrode 元件）导入上述频散参数，得到 `S21_EO(f)` 与 3 dB 带宽。
4. 对电极宽度/间距/金属厚度/缓冲层厚度做参数扫描，联合优化 `Vπ·L`、带宽、插损与阻抗匹配。

## 7) 参考资料（重点是 Ansys 官方与 TFLN 文献）

- PyAEDT HFSS API: https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html
- PyAEDT Client-Server/启动: https://aedt.docs.pyansys.com/version/stable/Getting_started/ClientServer.html
- Ansys Optics Traveling-Wave MZM 示例: https://optics.ansys.com/hc/en-us/articles/360042328774-Traveling-Wave-Mach-Zehnder-Modulator
- Ansys Optics TFLN 相位调制器示例: https://optics.ansys.com/hc/en-us/articles/19435937674387-Thin-Film-Lithium-Niobate-Electro-Optic-Phase-Modulator
- TFLN 行波电极综述（开源综述示例）: https://arxiv.org/abs/2404.06398


## 8) 基于 `coplanar_audit.json` 和 `confinement_audit.json` 自动判定是否满足指标

仓库新增判定脚本：`tools/hfss_tfln_judge.py`，可自动给出 PASS/FAIL 与改参建议。

```bat
"<你的python.exe路径>" tools\hfss_tfln_judge.py ^
  --coplanar "coplanar_audit.json" ^
  --confinement "confinement_audit.json" ^
  --out "hfss_judgement_report.md"
```

默认阈值（可在脚本里调整）：

- `|Z0 - 50Ω| <= 3Ω`
- `|Im(Z0)| <= 3Ω`
- `|delta_n| <= 0.05`
- `RF loss <= 0.5 dB/cm`

输出内容包含：

1. 两个模型各自的 RF loss / impedance / velocity matching / full-band 判定结果。
2. 约束下的频段上边界（含 EE 带宽估计边界）。
3. 40/67/110 GHz 关键频点指标。
4. 对应的具体改参建议（W/G/T、缓冲层厚度、金属电导率、回流路径等）。
