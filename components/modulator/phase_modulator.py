import gdsfactory as gf
# from PSI_PDK import create_straight_mzm_1x1_wg as mzm
from PSI_PDK import create_electrode_array as electrode
from PSI_PDK import create_electrode_launch
import config as cf

waveguide_length = 10*1000 # normalized length

def create_phase_modulator_folded(
    waveguide_width=2,
    waveguide_layer_num=(2, 0),
    waveguide_length_1=waveguide_length,
    waveguide_length_2=waveguide_length,
    electrode_length=2,
    electrode_distance_base_to_T=3,
    electrode_T_base_width=20,
    electrode_T_width=45,
    electrodes_gap=17,
    electrode_period=50,
    electrode_T_top_thickness=3,
    electrode_signal_height=150,
    electrode_ground_height=100,
    electrode_launch_is_left=False,
    electrode_launch_radius=612,
    electrode_launch_outer_width=96,
    electrode_launch_inner_width=84,
    electrode_launch_pitch=102,
    electrode_launch_gap=13,
    electrode_launch_signal_height=50,
    electrode_launch_ground_height=100,
    electrode_launch_npts=50,
    arc_waveguide_radius=100,
    waveguide_electrode_offset = 1000
) -> gf.Component:
    """Create a phase modulator folded layout."""


    total_gap = electrode_T_top_thickness*2 + electrode_distance_base_to_T*2 + electrodes_gap
    c = gf.Component("phase_modulator_folded")

    # define waveguide parameters
    cs = gf.cross_section.cross_section(width=waveguide_width, layer=waveguide_layer_num)

    # create waveguide1
    waveguide1 = gf.components.straight(length=waveguide_length_1, cross_section=cs)
    waveguide1_ref = c << waveguide1
    # waveguide1_ref.add_port("input", port=waveguide1_ref.ports["o1"])
    # waveguide1_ref.add_port("output", port=waveguide1_ref.ports["o2"])

    # create arc_waveguide
    arc_waveguide = gf.components.bend_circular(radius=arc_waveguide_radius, angle=-180, cross_section=cs)
    arc_waveguide_ref = c << arc_waveguide
    arc_waveguide_ref.connect("o1", destination=waveguide1_ref.ports["o2"])
    # arc_waveguide_ref.add_port("output", port=arc_waveguide_ref.ports["o2"])

    # create waveguide2
    waveguide2 = gf.components.straight(length=waveguide_length_2, cross_section=cs)
    waveguide2_ref = c << waveguide2
    waveguide2_ref.connect("o1", destination=arc_waveguide_ref.ports["o2"])
    # waveguide2_ref.add_port("output", port=waveguide2_ref.ports["o2"])

    # # add the final input and output ports
    # c.add_port("final_input", port=waveguide1_ref.ports["input"])
    # c.add_port("final_output", port=waveguide2_ref.ports["output"])

    # add electrode
    electrode_ref = c.add_ref(
        electrode(
            length=electrode_length,
            h1=electrode_distance_base_to_T,
            s=electrode_T_base_width,
            d=electrode_T_width,
            gap=electrodes_gap,
            period=electrode_period,
            r=electrode_T_top_thickness,
            signal_height=electrode_signal_height,
            ground_height=electrode_ground_height,
        )
    )
    electrode_ref.movex(waveguide_electrode_offset) 
    electrode_ref.movey(electrode_signal_height/2 + electrodes_gap/2 + electrode_T_top_thickness + electrode_distance_base_to_T)

    # add electrode launch
    electrode_launch_ref = c.add_ref(
        create_electrode_launch(
            is_left=electrode_launch_is_left,
            radius=electrode_launch_radius,
            outer_width=electrode_launch_outer_width,
            inner_width=electrode_launch_inner_width,
            pitch=electrode_launch_pitch,
            gap=total_gap,
            signal_height=electrode_launch_signal_height,
            ground_height=electrode_launch_ground_height,
            npts=electrode_launch_npts,
        )
    )
    electrode_launch_ref.movex(waveguide_electrode_offset + electrode_length*1000 - electrode_period/2)
    electrode_launch_ref.movey(electrode_launch_radius- electrode_launch_outer_width - electrode_launch_gap/2 - electrode_T_top_thickness - electrode_distance_base_to_T)

    return c


if __name__ == "__main__":
    layout = gf.Component("layout")
    c9 = layout << create_phase_modulator_folded()
    c9.show()


