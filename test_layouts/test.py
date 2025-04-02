import gdsfactory as gf
import PSI_PDK as Psi_pdk
import config as cf
from gdsfactory.samples.pdk.fab_c import pdk
import gdsfactory.cross_section
from psi_elements.blocks.mmi import mmi_1x2, mmi_1x2_sbend, mmi_2x2, mmi_2x2_sbend
from psi_elements.blocks.grating_coupler import grating_coupler
from psi_elements.blocks.electrode_ucell import ElectrodeUcell
from psi_elements.substrate import Substrate
from psi_elements.star_coupler import StarCoupler

yaml_pdk_decription = pdk.to_updk()
from gdsfactory.read.from_updk import from_updk

#print(yaml_pdk_decription)
#script = from_updk(yaml_pdk_decription)



#print(help(gf.components.mmi))

# Setup main component and mmi
# =================================================================================
c = gf.Component("MyComponent")
sub = Substrate()
c << sub
t = gf.components.text("Hello")


#ec = ElectrodeUcell()
mmi = mmi_2x2_sbend(waveguide="SIN_STRIP")
gc = grating_coupler(wg_width=cf.SIN_WG_WIDTH_SI, layer=cf.SIN_WG_LAYER) # grating coupler generation
#x = c << mmi # reference to the mmi component from our c central component
#y = c << ec # reference to the electrode unit cell for our c central component
#y.movey(1000)
#c << gc
#x.connect("o3", destination=gc["o1"])

min_radius=125

cs = gf.cross_section.cross_section(width=1, layer=(2, 0))
bendS = gf.components.bend_euler(radius=min_radius, cross_section=cs)
bendS1 = c << bendS


spiral = gf.components.spiral_external_io(length=75000, xspacing=10, yspacing=10, y_straight_outer_offset=100.0, cross_section=cs, bend=bendS)
spiral2 = gf.components.spiral_external_io(length=200000, xspacing=10, yspacing=10, cross_section=cs, y_straight_outer_offset=100.0, bend=bendS)
spiral3 = gf.components.spiral_external_io(length=300000, xspacing=10, yspacing=10, cross_section=cs, y_straight_outer_offset=100.0, bend=bendS)

spiralComp = gf.Component("7.5cm Spiral")
spiralComp << spiral
x1 = spiralComp << bendS
x2 = spiralComp << bendS
x1.connect("o2", destination=spiral["o1"])
x2.connect("o1", destination=spiral["o2"])

spiralComp20 = gf.Component("20cm Spiral")
spiralComp20 << spiral2
x1 = spiralComp20 << bendS
x2 = spiralComp20 << bendS
x1.connect("o2", destination=spiral2["o1"])
x2.connect("o1", destination=spiral2["o2"])

spiralComp30 = gf.Component("30cm Spiral")
spiralComp30 << spiral3
x1 = spiralComp30 << bendS
x2 = spiralComp30 << bendS
x1.connect("o2", destination=spiral3["o1"])
x2.connect("o1", destination=spiral3["o2"])

c << spiralComp
c2 = c << spiralComp20
c3 = c << spiralComp30
#c2.movey(-500)
c2.movex(10000)
c3.movey(-1000)
#c2 = c << gc
#euc = ElectrodeUcell()
#c << euc
#c2.movey(mmi.ymove)

#c.add_array(x, columns=1, rows=20, spacing=[0, 500])
#c.add_array(y, columns=1, rows=20, spacing=[0, 1000])



# Test the design in KLayout
# Must Have Klive installed and GDS Factory Extension enabled in Klayout
c.show()