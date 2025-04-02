import gdsfactory as gf
import config as cf

def ln_strip(width: float = cf.LN_WG_WIDTH, **kwargs):
    return gf.cross_section.cross_section(width=width, layer=cf.LN_WG_LAYER, **kwargs)
