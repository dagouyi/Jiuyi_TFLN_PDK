import gdsfactory as gf
from PSI_PDK import create_straight_mzm_1x1_wg as mzm
from PSI_PDK import create_electrode_array as electrode
import config as cf

def create_IQ_modulator_wg(
    length_of_MZM=2, # the length of the MZMs, unit in cm !!!
    yspacing=800,  # The spacing between two parallel MZMs   
    layer_num=(2, 0),  # layer of the layout, (2,0) is for the LN rib layer
    left_length=500,  # the length of the very left input waveguide
    right_length=500,  # the length of the very right input waveguide
    sbend_input_geom=[1525, 33.5],  # The sbend connect input MMI and two parallel MZMs
    sbend_geom=[325, 33.5],         # The sbend inside two parallel MZMs
    mmi_length=140,  # the length of the MMIs
    mmi_length_taper = 53,
    wg_width=2,  # The LN waveguide width
    taper_width=3,  # the length of the tapers of MMIs
    mmi_gap=4.5,  # The gap between two output taper of MMIs
    mmi_width=15  # the width of the MMIs     
) -> gf.Component:
    """
    Create a dual polarization coherent transmitter layout with two MMIs, two MZMs, and connecting waveguides.

    Returns:
        gf.Component: The complete layout for a dual polarization coherent transmitter.
    """
    c = gf.Component("IQ modulator waveguide")

    # Create the leftmost input MMI (1x2 splitter)
    mmi_input = gf.components.mmi1x2(
        width=wg_width,
        width_taper=taper_width,
        length_taper=mmi_length_taper,
        length_mmi=mmi_length,
        width_mmi=mmi_width,
        gap_mmi=mmi_gap,
        #layer=layer_num
    )
    mmi_input_ref = c << mmi_input

    # Create the rightmost output MMI (1x2 combiner) and rotate it 180 degrees
    mmi_output = gf.components.mmi1x2(
        width=wg_width,
        width_taper=taper_width,
        length_taper=mmi_length_taper,
        length_mmi=mmi_length,
        width_mmi=mmi_width,
        gap_mmi=mmi_gap,
        # layer=layer_num
    )
    mmi_output_ref = c << mmi_output
    mmi_output_ref.rotate(180)
    # mmi_output_ref.movey(100)
    mmi_output_ref.movex(left_length+mmi_length_taper + sbend_input_geom[0]+ left_length+mmi_length_taper+mmi_length+mmi_length_taper+sbend_geom[0]+length_of_MZM*1000+sbend_geom[0]+mmi_length_taper+mmi_length+mmi_length_taper+mmi_length+mmi_length_taper+sbend_input_geom[0]+mmi_length)

    # Create the two MZMs
    mzm_top_ref = c << mzm(
        # layer_num=layer_num,
        left_length=left_length,
        right_length=right_length,
        length=length_of_MZM,
        sbend_geom=sbend_geom,
        mmi_length=mmi_length,
        mmi_length_taper = mmi_length_taper,
        wg_width=wg_width,
        taper_width=taper_width,
        mmi_gap=mmi_gap,
        mmi_width=mmi_width
    )
    mzm_bottom_ref = c << mzm(
        # layer_num=layer_num,
        left_length=left_length,
        right_length=right_length,
        length=length_of_MZM,
        sbend_geom=sbend_geom,
        mmi_length=mmi_length,
        mmi_length_taper = mmi_length_taper,
        wg_width=wg_width,
        taper_width=taper_width,
        mmi_gap=mmi_gap,
        mmi_width=mmi_width
    )

    # Position the MZMs
    mzm_top_ref.movex(left_length+mmi_length+mmi_length_taper + sbend_input_geom[0]+ mmi_length_taper)
    mzm_top_ref.movey(yspacing / 2)

    mzm_bottom_ref.movex(left_length+mmi_length+mmi_length_taper + sbend_input_geom[0]+ mmi_length_taper)
    mzm_bottom_ref.movey(-yspacing / 2)

    # Create S-bends for input connections
    cs = gf.cross_section.cross_section(width=wg_width, layer=layer_num)
    bendS_input_top = gf.components.bend_s(size=sbend_input_geom, cross_section=cs)
    bendS_input_bottom = gf.components.bend_s(size=[sbend_input_geom[0], -sbend_input_geom[1]], cross_section=cs)

    # Connect input MMI to MZMs via bends
    bendS_input_top_ref = c << bendS_input_top
    bendS_input_top_ref.connect("o1", destination=mmi_input_ref.ports["o2"])
    bendS_input_top_ref.connect("o2", destination=mzm_top_ref.ports["o1"])
    # bendS_input_top_ref.movex(mmi_length_taper+mmi_length)

    bendS_input_bottom_ref = c << bendS_input_bottom
    bendS_input_bottom_ref.connect("o1", destination=mmi_input_ref.ports["o3"])
    bendS_input_bottom_ref.connect("o2", destination=mzm_bottom_ref.ports["o1"])
    # bendS_input_bottom_ref.movex(mmi_length_taper+mmi_length)

    # Create S-bends for the output side (mirrored)
    bendS_output_top = gf.components.bend_s(size=sbend_input_geom, cross_section=cs)
    bendS_output_bottom = gf.components.bend_s(size=[sbend_input_geom[0], -sbend_input_geom[1]], cross_section=cs)

    bendS_output_top_ref = c << bendS_output_top
    bendS_output_top_ref.connect("o1", destination=mzm_top_ref.ports["o2"])
    bendS_output_top_ref.movex(left_length+mmi_length_taper + sbend_input_geom[0]+ left_length+mmi_length_taper+mmi_length+mmi_length_taper+sbend_geom[0]+length_of_MZM*1000+sbend_geom[0]+mmi_length_taper+mmi_length+mmi_length_taper+mmi_length+mmi_length_taper)

    bendS_output_bottom_ref = c << bendS_output_bottom
    bendS_output_bottom_ref.connect("o1", destination=mzm_bottom_ref.ports["o2"])
    bendS_output_bottom_ref.movex(left_length+mmi_length_taper + sbend_input_geom[0]+ left_length+mmi_length_taper+mmi_length+mmi_length_taper+sbend_geom[0]+length_of_MZM*1000+sbend_geom[0]+mmi_length_taper+mmi_length+mmi_length_taper+mmi_length+mmi_length_taper)

    # Connect bends to the rotated output MMI
    bendS_output_top_ref.connect("o2", destination=mmi_output_ref.ports["o2"])
    bendS_output_bottom_ref.connect("o2", destination=mmi_output_ref.ports["o3"])

    # Add input and output waveguides
    input_waveguide = gf.components.straight(length=left_length, width=wg_width, layer=layer_num)
    input_waveguide_ref = c << input_waveguide
    input_waveguide_ref.connect("o2", destination=mmi_input_ref.ports["o1"])

    output_waveguide = gf.components.straight(length=right_length, width=wg_width, layer=layer_num)
    output_waveguide_ref = c << output_waveguide
    output_waveguide_ref.connect("o1", destination=mmi_output_ref.ports["o1"])

    # Add ports for the overall component
    c.add_port("optical_in", port=input_waveguide_ref.ports["o1"])
    c.add_port("optical_out", port=output_waveguide_ref.ports["o2"])

    electrode_top_MZM = c << electrode(length = 22, h1 = 3, s = 20, d = 45, gap = 17, period = 50, r = 3, signal_height = 50, ground_height = 100)

    electrode_bottom_MZM = c << electrode(length = 22, h1 = 3, s = 20, d = 45, gap = 17, period = 50, r = 3, signal_height = 50, ground_height = 100)

    return c

# Create the dual polarization coherent transmitter
dual_pol_tx = create_IQ_modulator_wg()

# Plot and show the layout
# dual_pol_tx.plot()
# dual_pol_tx.show()




