import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.port import Port
import matplotlib.pyplot as plt
import config as cf
# from PSI_PDK import create_wg_crossing

wg_width = 1
layer_num = (2,0)
c = gf.Component()
mmi1 = c << gf.components.mmi1x2(cross_section=gf.cross_section.cross_section(layer=cf.LN_WG_LAYER))
mmi2 = c << gf.components.mmi1x2(cross_section=gf.cross_section.cross_section(layer=cf.LN_WG_LAYER))
mmi2.move((100, 50))
# mmi2.drotate(45)

# cross = c << create_wg_crossing()

# cross.move((200,200))

# gf.cross_section.cross_section(width=wg_width, layer=layer_num)

route =  gf.routing.route_dubin(
    c,
    port1=mmi1.ports["o2"],
    # port2=cross.ports["o1"],
    port2=mmi2.ports["o1"],
    # cross_section=gf.cross_section.strip
    cross_section=gf.cross_section.cross_section(layer=cf.LN_WG_LAYER),
)

c1 = c << gf.components.pad()
c2 = c << gf.components.pad()
c2.move((200, 100))
routes = gf.routing.route_bundle_electrical(
    c,
    [c1.ports["e3"]],
    [c2.ports["e1"]],
    cross_section=gf.cross_section.metal3,
)
c

c.plot()
# c.show(show_ports = True)
# c.plot_matplotlib(show_ports = True)


gds_file_path = "routing_test.gds"
c.write_gds(gds_file_path)
print(f"GDS file saved as {gds_file_path}")
# layout.plot_matplotlib(show_ports = True)
plt.show()