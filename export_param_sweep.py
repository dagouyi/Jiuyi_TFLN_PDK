import gdsfactory as gf
from components.modulator.folded_mzm import Folded_MZM
from pathlib import Path

EXPORTS = Path(__file__).parent / "exports"
EXPORTS.mkdir(exist_ok=True)

lengths = [100, 150, 200]
widths = [1, 2, 3]

for l in lengths:
    for w in widths:
        c = Folded_MZM(length=l, width=w)
        c.write_gds(EXPORTS / f"folded_mzm_L{l}_W{w}.gds")
