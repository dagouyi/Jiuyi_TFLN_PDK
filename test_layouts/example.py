from functools import partial

import gdsfactory as gf
import gdsfactory.components as pc
from gdsfactory.generic_tech import LAYER


@gf.cell
def sample_reticle(
    size=(1500, 2000),
    ec="edge_coupler_silicon",
    bend_s=partial(gf.c.bend_s, size=(200, 200)),
) -> gf.Component:
    """Returns MZI with edge couplers.

    Args:
        size: size of the reticle.
        ec: edge coupler component name.
        bend_s: bend_s component.
    """
    mzis = [pc.mzi(length_x=lengths) for lengths in [100, 200, 300]]
    copies = 3  # number of copies of each component
    components = mzis * copies

    xsizes = [component.xsize for component in components]
    xsize_max = max(xsizes)
    ec = gf.get_component(ec)
    taper = pc.taper(width2=0.5)
    components_ec = []

    if xsize_max + 2 * taper.xsize + 2 * ec.xsize > size[0]:
        raise ValueError(
            f"Component xsize_max={xsize_max} is larger than reticle size[0]={size[0]}"
        )

    if bend_s:
        bend_s = gf.get_component(bend_s)

    for component in components:
        if bend_s:
            component = gf.components.extend_ports(
                component, extension=bend_s, port1="o1", port2="o2"
            )
            extension_length = (
                size[0]
                - 2 * taper.xsize
                - 2 * ec.xsize
                - component.xsize
                - 2 * bend_s.xsize
            ) / 2
        else:
            extension_length = (
                size[0] - 2 * taper.xsize - 2 * ec.xsize - component.xsize
            ) / 2

        component_extended = gf.components.extend_ports(
            component,
            extension=pc.straight(extension_length),
            port2="o2",
            port1="o1",
        )

        component_tapered = gf.components.extend_ports(
            component_extended, extension=taper, port2="o2", port1="o1"
        )
        component_ec = gf.components.extend_ports(
            component_tapered, extension=ec, port1="o1", port2="o2"
        )
        components_ec.append(component_ec)

    c = gf.Component()
    fp = c << pc.rectangle(size=size, layer=LAYER.FLOORPLAN)

    text_offset_y = 10
    text_offset_x = 100

    grid = c << gf.grid_with_text(
        components_ec,
        shape=(len(components), 1),
        text=partial(gf.c.text_rectangular, layer=LAYER.M3),
        text_offsets=(
            (-size[0] / 2 + text_offset_x, text_offset_y),
            (+size[0] / 2 - text_offset_x - 160, text_offset_y),
        ),
    )
    fp.x = grid.x
    return c


c = sample_reticle()
c.plot()
c.show()