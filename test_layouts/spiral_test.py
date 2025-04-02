# # from functools import partial

# # import gdsfactory as gf
# # import gdsfactory.components as pc
# # from gdsfactory.generic_tech import LAYER

# # @gf.cell
# # def sample_reticle_with_spiral(
# #     size=(1500, 2000),
# #     ec="edge_coupler_silicon",
# #     spiral=partial(gf.components.spiral_double, min_bend_radius=80, separation=2, number_of_loops=15, npoints=1000, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'), bend="bend_circular"),
# # ) -> gf.Component:
# #     """Returns a reticle with spirals and edge couplers.

# #     Args:
# #         size: size of the reticle.
# #         ec: edge coupler component name.
# #         spiral: spiral component.
# #     """
# #     # Create spiral components
# #     spirals = [spiral() for _ in range(3)]  # Create 3 spirals
# #     copies = 3  # Number of copies of each component
# #     components = spirals * copies

# #     xsizes = [component.xsize for component in components]
# #     xsize_max = max(xsizes)
# #     ec = gf.get_component(ec)
# #     components_ec = []

# #     if xsize_max + 2 * ec.xsize > size[0]:
# #         raise ValueError(
# #             f"Component xsize_max={xsize_max} is larger than reticle size[0]={size[0]}"
# #         )

# #     for component in components:
# #         extension_length = (
# #             size[0] - 2 * ec.xsize - component.xsize
# #         ) / 2

# #         straight_extension = pc.straight(length=extension_length, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'))  # Ensure matching width
# #         component_extended = gf.components.extend_ports(
# #             component,
# #             extension=straight_extension,
# #             port2="o2",
# #             port1="o1",
# #         )

# #         component_ec = gf.components.extend_ports(
# #             component_extended, extension=ec, port1="o1", port2="o2"
# #         )
# #         components_ec.append(component_ec)

# #     c = gf.Component()
# #     fp = c << pc.rectangle(size=size, layer=LAYER.FLOORPLAN)

# #     text_offset_y = 10
# #     text_offset_x = 100

# #     grid = c << gf.grid_with_text(
# #         components_ec,
# #         shape=(len(components), 1),
# #         text=partial(gf.c.text_rectangular, layer=LAYER.M3),
# #         text_offsets=(
# #             (-size[0] / 2 + text_offset_x, text_offset_y),
# #             (+size[0] / 2 - text_offset_x - 160, text_offset_y),
# #         ),
# #     )
# #     fp.x = grid.x
# #     return c

# # # Create reticle with spirals
# # c = sample_reticle_with_spiral()
# # c.plot()

# # # Export the reticle to a GDS file
# # gds_file_path = "reticle_with_spirals.gds"
# # c.write_gds(gds_file_path)
# # print(f"GDS file saved as {gds_file_path}")




# # from functools import partial

# # import gdsfactory as gf
# # import gdsfactory.components as pc
# # from gdsfactory.generic_tech import LAYER

# # @gf.cell
# # def sample_reticle_with_spiral(
# #     size=(1500, 2000),
# #     ec="edge_coupler_silicon",
# #     spiral=partial(gf.components.spiral_double, min_bend_radius=80, separation=2, number_of_loops=15, npoints=1000, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'), bend="bend_circular"),
# # ) -> gf.Component:
# #     """Returns a reticle with spirals and edge couplers.

# #     Args:
# #         size: size of the reticle.
# #         ec: edge coupler component name.
# #         spiral: spiral component.
# #     """
# #     # Create spiral components
# #     spirals = [spiral() for _ in range(3)]  # Create 3 spirals
# #     copies = 3  # Number of copies of each component
# #     components = spirals * copies

# #     xsizes = [component.xsize for component in components]
# #     xsize_max = max(xsizes)
# #     ec = gf.get_component(ec)
# #     taper = pc.taper(width1=1.5, width2=1.5, length=10)  # Ensure taper matches spiral width
# #     components_ec = []

# #     if xsize_max + 2 * taper.xsize + 2 * ec.xsize > size[0]:
# #         raise ValueError(
# #             f"Component xsize_max={xsize_max} is larger than reticle size[0]={size[0]}"
# #         )

# #     for component in components:
# #         extension_length = (
# #             size[0] - 2 * taper.xsize - 2 * ec.xsize - component.xsize
# #         ) / 2

# #         straight_extension = pc.straight(length=extension_length, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'))  # Ensure matching width
# #         component_extended = gf.components.extend_ports(
# #             component,
# #             extension=straight_extension,
# #             port2="o2",
# #             port1="o1",
# #         )

# #         component_tapered = gf.components.extend_ports(
# #             component_extended, extension=taper, port2="o2", port1="o1"
# #         )
# #         component_ec = gf.components.extend_ports(
# #             component_tapered, extension=ec, port1="o1", port2="o2"
# #         )
# #         components_ec.append(component_ec)

# #     c = gf.Component()
# #     fp = c << pc.rectangle(size=size, layer=LAYER.FLOORPLAN)

# #     text_offset_y = 10
# #     text_offset_x = 100

# #     grid = c << gf.grid_with_text(
# #         components_ec,
# #         shape=(len(components), 1),
# #         text=partial(gf.c.text_rectangular, layer=LAYER.M3),
# #         text_offsets=(
# #             (-size[0] / 2 + text_offset_x, text_offset_y),
# #             (+size[0] / 2 - text_offset_x - 160, text_offset_y),
# #         ),
# #     )
# #     fp.x = grid.x
# #     return c

# # # Create reticle with spirals
# # c = sample_reticle_with_spiral()
# # c.plot()

# # # Export the reticle to a GDS file
# # gds_file_path = "reticle_with_spirals.gds"
# # c.write_gds(gds_file_path)
# # print(f"GDS file saved as {gds_file_path}")...



# # from functools import partial

# # import gdsfactory as gf
# # import gdsfactory.components as pc
# # from gdsfactory.generic_tech import LAYER

# # @gf.cell
# # def sample_reticle_with_spiral(
# #     size=(1500, 2000),
# #     ec="edge_coupler_silicon",
# #     spiral=partial(gf.components.spiral_double, min_bend_radius=80, separation=2, number_of_loops=15, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.5, offset=0, layer='WG'), bend="bend_circular"),
# # ) -> gf.Component:
# #     """Returns a reticle with spirals and edge couplers.

# #     Args:
# #         size: size of the reticle.
# #         ec: edge coupler component name.
# #         spiral: spiral component.
# #     """
# #     # Create spiral components
# #     spirals = [spiral() for _ in range(3)]  # Create 3 spirals
# #     copies = 3  # Number of copies of each component
# #     components = spirals * copies

# #     xsizes = [component.xsize for component in components]
# #     xsize_max = max(xsizes)
# #     ec = gf.get_component(ec)
# #     taper = pc.taper(width2=1.5)
# #     components_ec = []

# #     if xsize_max + 2 * taper.xsize + 2 * ec.xsize > size[0]:
# #         raise ValueError(
# #             f"Component xsize_max={xsize_max} is larger than reticle size[0]={size[0]}"
# #         )

# #     for component in components:
# #         extension_length = (
# #             size[0] - 2 * taper.xsize - 2 * ec.xsize - component.xsize
# #         ) / 2

# #         component_extended = gf.components.extend_ports(
# #             component,
# #             extension=pc.straight(extension_length),
# #             port2="o2",
# #             port1="o1",
# #         )

# #         component_tapered = gf.components.extend_ports(
# #             component_extended, extension=taper, port2="o2", port1="o1"
# #         )
# #         component_ec = gf.components.extend_ports(
# #             component_tapered, extension=ec, port1="o1", port2="o2"
# #         )
# #         components_ec.append(component_ec)

# #     c = gf.Component()
# #     fp = c << pc.rectangle(size=size, layer=LAYER.FLOORPLAN)

# #     text_offset_y = 10
# #     text_offset_x = 100

# #     grid = c << gf.grid_with_text(
# #         components_ec,
# #         shape=(len(components), 1),
# #         text=partial(gf.c.text_rectangular, layer=LAYER.M3),
# #         text_offsets=(
# #             (-size[0] / 2 + text_offset_x, text_offset_y),
# #             (+size[0] / 2 - text_offset_x - 160, text_offset_y),
# #         ),
# #     )
# #     fp.x = grid.x
# #     return c

# # # Create reticle with spirals
# # c = sample_reticle_with_spiral()
# # c.plot()

# # # Export the reticle to a GDS file
# # gds_file_path = "reticle_with_spirals.gds"
# # c.write_gds(gds_file_path)
# # print(f"GDS file saved as {gds_file_path}")




import gdsfactory as gf
import matplotlib.pyplot as plt
from gdsfactory.components.spirals.spiral import spiral
import config as cf

layout = gf.Component()
waveguide_layer_num = (1,0)

# c1 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=25, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'), bend='bend_circular').copy()
c1 = layout << gf.components.spiral_racetrack(min_radius=80, straight_length=5000, spacings=(25, 25, 25, 25, 25, 25), cross_section=gf.cross_section.cross_section(width=1.0, layer = cf.LN_WG_LAYER), n_bend_points=100000, with_inner_ports=False, extra_90_deg_bend=False, allow_min_radius_violation=True)

# # c2 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=25, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'), bend='bend_circular').copy()
# # c3 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=25, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'), bend='bend_circular').copy()
# # c4 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=25, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'), bend='bend_circular').copy()
# # c5 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=25, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG'), bend='bend_circular').copy()

# c6 = layout << gf.components.ring_double_bend_coupler(radius=80, gap=0.5, coupling_angle_coverage=0.5, length_x=0.5, length_y=0.5, cross_section_inner=gf.cross_section.cross_section(width=1.5, layer='WG'), cross_section_outer=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# c7 = layout << gf.components.ring_double_bend_coupler(radius=80, gap=0.6, coupling_angle_coverage=0.5, length_x=0.5, length_y=0.5, cross_section_inner=gf.cross_section.cross_section(width=1.5, layer='WG'), cross_section_outer=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# c8 = layout << gf.components.ring_double_bend_coupler(radius=80, gap=0.7, coupling_angle_coverage=0.5, length_x=0.5, length_y=0.5, cross_section_inner=gf.cross_section.cross_section(width=1.5, layer='WG'), cross_section_outer=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# c9 = layout << gf.components.ring_double_bend_coupler(radius=80, gap=0.8, coupling_angle_coverage=0.5, length_x=0.5, length_y=0.5, cross_section_inner=gf.cross_section.cross_section(width=1.5, layer='WG'), cross_section_outer=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# c10 = layout << gf.components.ring_double_bend_coupler(radius=80, gap=0.9, coupling_angle_coverage=0.5, length_x=0.5, length_y=0.5, cross_section_inner=gf.cross_section.cross_section(width=1.5, layer='WG'), cross_section_outer=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()

# c11 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=15, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG'), bend='bend_circular').copy()
# c12 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=15, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG'), bend='bend_circular').copy()
# c13 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=15, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG'), bend='bend_circular').copy()
# c14 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=15, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG'), bend='bend_circular').copy()
# c15 = layout << gf.components.spiral_double(min_bend_radius=160, separation=4, number_of_loops=15, npoints=100000, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG'), bend='bend_circular').copy()






# # c2.movex(1000)
# # c2.movey(20)

# # c3.movex(2000)
# # c3.movey(40)

# # c4.movex(3000)
# # c4.movey(60)

# # c5.movex(4000)
# # c5.movey(80)

# c6.movex(0)
# c6.movey(1420)

# c7.movex(1000)
# c7.movey(1840)

# c8.movex(2000)
# c8.movey(2260)

# c9.movex(3000)
# c9.movey(2680)

# c10.movex(4000)
# c10.movey(3100)

# c11.movex(0)
# c11.movey(-900)

# c12.movex(1000)
# c12.movey(-880)

# c13.movex(2000)
# c13.movey(-860)

# c14.movex(3000)
# c14.movey(-840)

# c15.movex(4000)
# c15.movey(-820)




input_waveguide = gf.components.straight(length= 1000, width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer = cf.LN_WG_LAYER))
input_waveguide_ref = layout << input_waveguide
input_waveguide_ref.connect(port = "o1", other=c1.ports["o2"])

output_waveguide = gf.components.straight(length= 1000, width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer = cf.LN_WG_LAYER))
output_waveguide_ref = layout << output_waveguide
output_waveguide_ref.connect(port = "o2", other=c1.ports["o1"])

# # input_waveguide = gf.components.straight(length= 4000 , width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # input_waveguide_ref = layout << input_waveguide
# # input_waveguide_ref.connect(port = "o2", other=c2.ports["o1"])

# # output_waveguide = gf.components.straight(length= 4000, width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # output_waveguide_ref = layout << output_waveguide
# # output_waveguide_ref.connect(port = "o1", other=c2.ports["o2"])

# # input_waveguide = gf.components.straight(length= 5000 , width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # input_waveguide_ref = layout << input_waveguide
# # input_waveguide_ref.connect(port = "o2", other=c3.ports["o1"])

# # output_waveguide = gf.components.straight(length= 3000, width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # output_waveguide_ref = layout << output_waveguide
# # output_waveguide_ref.connect(port = "o1", other=c3.ports["o2"])

# # input_waveguide = gf.components.straight(length= 6000 , width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # input_waveguide_ref = layout << input_waveguide
# # input_waveguide_ref.connect(port = "o2", other=c4.ports["o1"])

# # output_waveguide = gf.components.straight(length= 2000 , width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # output_waveguide_ref = layout << output_waveguide
# # output_waveguide_ref.connect(port = "o1", other=c4.ports["o2"])

# # input_waveguide = gf.components.straight(length= 7000 , width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # input_waveguide_ref = layout << input_waveguide
# # input_waveguide_ref.connect(port = "o2", other=c5.ports["o1"])

# # output_waveguide = gf.components.straight(length= 1000 , width=1.5, cross_section=gf.cross_section.cross_section(width=1.5, layer='WG')).copy()
# # output_waveguide_ref = layout << output_waveguide
# # output_waveguide_ref.connect(port = "o1", other=c5.ports["o2"])



# input_waveguide = gf.components.straight(length= 3000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c6.ports["o1"])

# output_waveguide = gf.components.straight(length= 5000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c6.ports["o4"])

# input_waveguide = gf.components.straight(length= 3000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c6.ports["o2"])

# output_waveguide = gf.components.straight(length= 5000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c6.ports["o3"])


# input_waveguide = gf.components.straight(length= 4000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c7.ports["o1"])

# output_waveguide = gf.components.straight(length= 4000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c7.ports["o4"])

# input_waveguide = gf.components.straight(length= 4000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c7.ports["o2"])

# output_waveguide = gf.components.straight(length= 4000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c7.ports["o3"])




# input_waveguide = gf.components.straight(length= 5000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c8.ports["o1"])

# output_waveguide = gf.components.straight(length= 3000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c8.ports["o4"])

# input_waveguide = gf.components.straight(length= 5000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c8.ports["o2"])

# output_waveguide = gf.components.straight(length= 3000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c8.ports["o3"])


# input_waveguide = gf.components.straight(length= 6000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c9.ports["o1"])

# output_waveguide = gf.components.straight(length= 2000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c9.ports["o4"])

# input_waveguide = gf.components.straight(length= 6000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c9.ports["o2"])

# output_waveguide = gf.components.straight(length= 2000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c9.ports["o3"])


# input_waveguide = gf.components.straight(length= 7000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c10.ports["o1"])

# output_waveguide = gf.components.straight(length= 1000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c10.ports["o4"])

# input_waveguide = gf.components.straight(length= 7000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c10.ports["o2"])

# output_waveguide = gf.components.straight(length= 1000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c10.ports["o3"])



# input_waveguide = gf.components.straight(length= 5000, width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o1", other=c11.ports["o2"])

# output_waveguide = gf.components.straight(length= 3000, width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o2", other=c11.ports["o1"])

# input_waveguide = gf.components.straight(length= 4000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c12.ports["o1"])

# output_waveguide = gf.components.straight(length= 4000, width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c12.ports["o2"])

# input_waveguide = gf.components.straight(length= 5000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c13.ports["o1"])

# output_waveguide = gf.components.straight(length= 3000, width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c13.ports["o2"])

# input_waveguide = gf.components.straight(length= 6000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c14.ports["o1"])

# output_waveguide = gf.components.straight(length= 2000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c14.ports["o2"])

# input_waveguide = gf.components.straight(length= 7000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# input_waveguide_ref = layout << input_waveguide
# input_waveguide_ref.connect(port = "o2", other=c15.ports["o1"])

# output_waveguide = gf.components.straight(length= 1000 , width=1.0, cross_section=gf.cross_section.cross_section(width=1.0, layer='WG')).copy()
# output_waveguide_ref = layout << output_waveguide
# output_waveguide_ref.connect(port = "o1", other=c15.ports["o2"])


layout.draw_ports()
layout.plot()

layout.plot()
# c.show(show_ports = True)
# print(yspacing/2)

# print(first_sbends_gap)
# print(second_sbens_gap)
# Export the layout to a GDS file
gds_file_path = "spiral.gds"
layout.write_gds(gds_file_path)
print(f"GDS file saved as {gds_file_path}")
# print(c1.tail)
# c.plot_matplotlib(show_ports = True)
plt.show()
