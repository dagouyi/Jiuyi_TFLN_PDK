import gdsfactory as gf
from gdsfactory.component import Component
import matplotlib.pyplot as plt

c = gf.Component()

# Create two straight waveguides with different orientations
wg1 = c << gf.components.straight(length=100, width=3.2)
wg2 = c << gf.components.straight(length=100, width=3.2)

# Move and rotate the second waveguide
wg2.move((300, 50))
wg2.rotate(135)

# Route between the output of wg1 and input of wg2
route = gf.routing.route_dubin(
    c,
    port1=wg1.ports["o2"],
    port2=wg2.ports["o1"],
    cross_section=gf.cross_section.strip(width=3.2, radius=200),
)
c

c.plot()
# c.show(show_ports = True)
# c.plot_matplotlib(show_ports = True)
plt.show()