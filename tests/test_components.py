import pytest
import gdsfactory as gf
from components.modulator.folded_mzm import Folded_MZM

def test_folded_mzm_builds():
    c = Folded_MZM()
    assert isinstance(c, gf.Component)
    assert len(c.ports) > 0
