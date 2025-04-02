import gdsfactory as gf
from gdsfactory.config import PATH
from gdsfactory.generic_tech import get_generic_pdk
from gdsfactory.technology import lyp_to_dataclass 

gf.config.rich_output()

layer_map = lyp_to_dataclass('./2323PDK.lyp')
print(layer_map)