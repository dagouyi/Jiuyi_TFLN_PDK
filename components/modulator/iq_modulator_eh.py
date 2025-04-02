import gdsfactory as gf
from PSI_PDK import create_straight_mzm_1x1_wg as mzm
from PSI_PDK import create_electrode_array as electrode
from PSI_PDK import create_electrode_launch
from PSI_PDK import create_heater_single as heater
import config as cf



def create_IQ_modulator(
    waveguide_width = 2,  # The LN waveguide width
    waveguide_length_of_MZM = 2, # the length of the MZMs, unit in cm !!!
    waveguide_yspacing = 800,  # The spacing between two parallel MZMs   
    waveguide_layer_num = (2, 0),  # layer of the layout, (2,0) is for the LN rib layer
    waveguide_left_length = 500,  # the length of the very left input waveguide
    waveguide_right_length = 500,  # the length of the very right input waveguide 
    waveguide_sbend_input_geom = [1525, 33.5],  # The sbend connect input MMI and two parallel MZMs
    waveguide_sbend_geom = [325, 33.5],         # The sbend inside two parallel MZMs
    waveguide_two_arm_offset_length_for_heaters = 200 /1000,
    mmi_length = 140,  # the length of the MMIs
    mmi_length_taper = 53,    
    mmi_taper_width= 3,  # the length of the tapers of MMIs
    mmi_gap= 4.5,  # The gap between two output taper of MMIs
    mmi_width= 15,  # the width of the MMIs 
    electrode_length = 2,
    electrode_distance_base_to_T = 3,
    electrode_T_base_width = 20,
    electrode_T_width = 45,
    electrodes_gap = 17,
    electrode_period = 50,
    electrode_T_top_thickness = 3,
    electrode_signal_height = 150,
    electrode_ground_height = 100,
    electrode_launch_is_left = False,
    electrode_launch_radius = 612,  # electrode launch radius
    electrode_launch_outer_width = 96, # width of ground launch pads on outside
    electrode_launch_inner_width = 84, # width of signal launch pad
    electrode_launch_pitch = 102, #  distance between probe contacts
    electrode_launch_gap = 13, #  distance between electrodes
    electrode_launch_signal_height = 50, #  signal electrode width (or height, depending on how you look at it)
    electrode_launch_ground_height = 100, #  ground electrodes width (or height, depending on how you look at it)
    electrode_launch_npts = 50,  #  number of points in arc
    heater_only_heater = False,
    heater_length = 613,
    heater_width = 4,
    heater_pad_width=60,
    heater_pad_length = 446,
    heater_connection_buffer = 15,
    heater_height_separation = 45,
    heater_bottom_pad_width = 23.2,
    heater_left_connection_width = 13.4

    


) -> gf.Component:
    """
    Create a dual polarization coherent transmitter layout with two MMIs, two MZMs, and connecting waveguides.

    Returns:
        gf.Component: The complete layout for a dual polarization coherent transmitter.
    """
    c = gf.Component("IQ modulator")

    first_sbends_gap = ((mmi_taper_width/2+ mmi_taper_width/2+ mmi_gap)-(waveguide_width/2+waveguide_width/2))/2 + (waveguide_width/2+waveguide_width/2)/2
    second_sbens_gap = (mmi_taper_width/2+ mmi_taper_width/2+ mmi_gap)-(waveguide_width/2+waveguide_width/2) - waveguide_width/2 - waveguide_width/2
    sbend_input_geom = [1530, waveguide_yspacing/2 - first_sbends_gap] # the x-axis length and y-axis length of the sbend bewteen the input MMI and two parallel MZMs

    # Create the leftmost input MMI (1x2 splitter)
    mmi_input = gf.components.mmi1x2(
        width=waveguide_width,
        width_taper=mmi_taper_width,
        length_taper=mmi_length_taper,
        length_mmi=mmi_length,
        width_mmi=mmi_width,
        gap_mmi=mmi_gap,
        layer=waveguide_layer_num
    )
    mmi_input_ref = c << mmi_input

    # Create the rightmost output MMI (1x2 combiner) and rotate it 180 degrees
    mmi_output = gf.components.mmi1x2(
        width=waveguide_width,
        width_taper=mmi_taper_width,
        length_taper=mmi_length_taper,
        length_mmi=mmi_length,
        width_mmi=mmi_width,
        gap_mmi=mmi_gap,
        layer=waveguide_layer_num
    )
    mmi_output_ref = c << mmi_output
    mmi_output_ref.rotate(180)
    # mmi_output_ref.movey(100)
    mmi_output_ref.movex(waveguide_left_length+mmi_length_taper + waveguide_sbend_input_geom[0]+ waveguide_right_length+mmi_length_taper+mmi_length+mmi_length_taper+waveguide_sbend_geom[0]+waveguide_length_of_MZM*1000+waveguide_sbend_geom[0]+mmi_length_taper+mmi_length+mmi_length_taper+mmi_length+mmi_length_taper+waveguide_sbend_input_geom[0]+mmi_length)

    # Create the two MZMs
    mzm_top_ref = c << mzm(
        layer_num=waveguide_layer_num,
        left_length=waveguide_left_length,
        right_length=waveguide_right_length,
        length=waveguide_length_of_MZM,
        sbend_geom=waveguide_sbend_geom,
        mmi_length=mmi_length,
        mmi_length_taper = mmi_length_taper,
        wg_width=waveguide_width,
        taper_width=mmi_taper_width,
        mmi_gap=mmi_gap,
        mmi_width=mmi_width
    )
    mzm_bottom_ref = c << mzm(
        layer_num=waveguide_layer_num,
        left_length=waveguide_left_length,
        right_length=waveguide_right_length,
        length=waveguide_length_of_MZM,
        sbend_geom=waveguide_sbend_geom,
        mmi_length=mmi_length,
        mmi_length_taper = mmi_length_taper,
        wg_width=waveguide_width,
        taper_width=mmi_taper_width,
        mmi_gap=mmi_gap,
        mmi_width=mmi_width
    )

    # Position the MZMs
    mzm_top_ref.movex(waveguide_left_length+mmi_length+mmi_length_taper + waveguide_sbend_input_geom[0]+ mmi_length_taper)
    mzm_top_ref.movey( waveguide_yspacing / 2)

    mzm_bottom_ref.movex(waveguide_left_length+mmi_length+mmi_length_taper + waveguide_sbend_input_geom[0]+ mmi_length_taper)
    mzm_bottom_ref.movey(- waveguide_yspacing / 2)

    # Create S-bends for input connections
    cs = gf.cross_section.cross_section(width=waveguide_width, layer=waveguide_layer_num)
    bendS_input_top = gf.components.bend_s(size=waveguide_sbend_input_geom, cross_section=cs)
    bendS_input_bottom = gf.components.bend_s(size=[waveguide_sbend_input_geom[0], -waveguide_sbend_input_geom[1]], cross_section=cs)

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
    bendS_output_top = gf.components.bend_s(size=waveguide_sbend_input_geom, cross_section=cs)
    bendS_output_bottom = gf.components.bend_s(size=[waveguide_sbend_input_geom[0], -waveguide_sbend_input_geom[1]], cross_section=cs)

    bendS_output_top_ref = c << bendS_output_top
    bendS_output_top_ref.connect("o1", destination=mzm_top_ref.ports["o2"])
    bendS_output_top_ref.movex(waveguide_left_length+mmi_length_taper + waveguide_sbend_input_geom[0]+ waveguide_right_length+mmi_length_taper+mmi_length+mmi_length_taper+waveguide_sbend_geom[0]+waveguide_length_of_MZM*1000+waveguide_sbend_geom[0]+mmi_length_taper+mmi_length+mmi_length_taper+mmi_length+mmi_length_taper)

    bendS_output_bottom_ref = c << bendS_output_bottom
    bendS_output_bottom_ref.connect("o1", destination=mzm_bottom_ref.ports["o2"])
    bendS_output_bottom_ref.movex(waveguide_left_length+mmi_length_taper + waveguide_sbend_input_geom[0]+ waveguide_right_length+mmi_length_taper+mmi_length+mmi_length_taper+waveguide_sbend_geom[0]+waveguide_length_of_MZM*1000+waveguide_sbend_geom[0]+mmi_length_taper+mmi_length+mmi_length_taper+mmi_length+mmi_length_taper)

    # Connect bends to the rotated output MMI
    bendS_output_top_ref.connect("o2", destination=mmi_output_ref.ports["o2"])
    bendS_output_bottom_ref.connect("o2", destination=mmi_output_ref.ports["o3"])

    # Add input and output waveguides
    input_waveguide = gf.components.straight(length=waveguide_left_length, width=waveguide_width, layer=waveguide_layer_num)
    input_waveguide_ref = c << input_waveguide
    input_waveguide_ref.connect("o2", destination=mmi_input_ref.ports["o1"])

    output_waveguide = gf.components.straight(length=waveguide_left_length, width=waveguide_width, layer=waveguide_layer_num)
    output_waveguide_ref = c << output_waveguide
    output_waveguide_ref.connect("o1", destination=mmi_output_ref.ports["o1"])

    # Add ports for the overall component
    c.add_port("optical_in", port=input_waveguide_ref.ports["o1"])
    c.add_port("optical_out", port=output_waveguide_ref.ports["o2"])

    electrode_top_MZM = c.add_ref(electrode(
        length=electrode_length,
        h1=electrode_distance_base_to_T,
        s=electrode_T_base_width,
        d=electrode_T_width,
        gap=electrodes_gap,
        period=electrode_period,
        r=electrode_T_top_thickness,
        signal_height=electrode_signal_height,
        ground_height=electrode_ground_height
    ))
    electrode_top_MZM.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + mmi_length_taper + mmi_length + waveguide_sbend_geom[0] + electrode_period / 2)
    electrode_top_MZM.movey( waveguide_yspacing / 2)

    electrode_bottom_MZM = c.add_ref(electrode(
        length=electrode_length,
        h1=electrode_distance_base_to_T,
        s=electrode_T_base_width,
        d=electrode_T_width,
        gap=electrodes_gap,
        period=electrode_period,
        r=electrode_T_top_thickness,
        signal_height=electrode_signal_height,
        ground_height=electrode_ground_height
    ))
    electrode_bottom_MZM.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + mmi_length_taper + mmi_length + waveguide_sbend_geom[0] + electrode_period / 2)
    electrode_bottom_MZM.movey(- waveguide_yspacing / 2)

    # Create and place the electrode launch
    electrode_launch_ref_top_MZM = c.add_ref(create_electrode_launch(
        is_left=electrode_launch_is_left, 
        radius=electrode_launch_radius, 
        outer_width=electrode_launch_outer_width, 
        inner_width=electrode_launch_inner_width, 
        pitch=electrode_launch_pitch, 
        gap=electrode_launch_gap, 
        signal_height=electrode_launch_signal_height, 
        ground_height=electrode_launch_ground_height, 
        npts=electrode_launch_npts
    ))
    #electrode_launch_ref_bottom_MZM.mirror((0,0),(1,0))
    electrode_launch_ref_top_MZM.movex(mmi_length+ mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + mmi_length_taper + mmi_length + mmi_length_taper+ waveguide_sbend_geom[0] + electrode_length*1000)    
    electrode_launch_ref_top_MZM.movey(waveguide_yspacing / 2+ (electrode_launch_radius-electrode_launch_outer_width -electrode_launch_gap - (electrode_launch_inner_width)/2))


    # Create and place the electrode launch
    electrode_launch_ref_bottom_MZM = c.add_ref(create_electrode_launch(
        is_left=electrode_launch_is_left, 
        radius=electrode_launch_radius, 
        outer_width=electrode_launch_outer_width, 
        inner_width=electrode_launch_inner_width, 
        pitch=electrode_launch_pitch, 
        gap=electrode_launch_gap, 
        signal_height=electrode_launch_signal_height, 
        ground_height=electrode_launch_ground_height, 
        npts=electrode_launch_npts
    ))
    electrode_launch_ref_bottom_MZM.mirror((0,0),(1,0))
    electrode_launch_ref_bottom_MZM.movex(mmi_length+ mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + mmi_length_taper + mmi_length + mmi_length_taper+ waveguide_sbend_geom[0] + electrode_length*1000)
    electrode_launch_ref_bottom_MZM.movey(- waveguide_yspacing / 2 - (electrode_launch_radius-electrode_launch_outer_width -electrode_launch_gap - (electrode_launch_inner_width)/2))

    # Create and place the heater
    heater_ref_output_top = c.add_ref(heater(
        only_heater=heater_only_heater, 
        heater_length=heater_length, 
        heater_width=heater_width, 
        pad_width=heater_pad_width, 
        pad_length=heater_pad_length,                      
        connection_buffer=heater_connection_buffer, 
        height_separation=heater_height_separation, 
        bottom_pad_width=heater_bottom_pad_width, 
        left_connection_width=heater_left_connection_width
    ))
    
    heater_ref_output_top.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + mmi_length_taper + mmi_length + waveguide_sbend_geom[0]  + electrode_length + electrode_launch_radius + waveguide_two_arm_offset_length_for_heaters +waveguide_length_of_MZM*1000 )
    heater_ref_output_top.movey( waveguide_yspacing / 2)

    heater_ref_output_bottom = c.add_ref(heater(
        only_heater=heater_only_heater, 
        heater_length=heater_length, 
        heater_width=heater_width, 
        pad_width=heater_pad_width, 
        pad_length=heater_pad_length,                      
        connection_buffer=heater_connection_buffer, 
        height_separation=heater_height_separation, 
        bottom_pad_width=heater_bottom_pad_width, 
        left_connection_width= heater_left_connection_width
    ))
    

    heater_ref_output_bottom.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + mmi_length_taper + mmi_length + waveguide_sbend_geom[0]  + electrode_length + electrode_launch_radius+ waveguide_two_arm_offset_length_for_heaters +waveguide_length_of_MZM*1000 )
    heater_ref_output_bottom.mirror((0,0),(1,0))
    heater_ref_output_bottom.movey( -waveguide_yspacing / 2)

    heater_ref_top_MZM_top = c.add_ref(heater(
        only_heater=heater_only_heater, 
        heater_length=heater_length, 
        heater_width=heater_width, 
        pad_width=heater_pad_width, 
        pad_length=heater_pad_length,                      
        connection_buffer=heater_connection_buffer, 
        height_separation=heater_height_separation, 
        bottom_pad_width=heater_bottom_pad_width, 
        left_connection_width=heater_left_connection_width
    ))
    
    heater_ref_top_MZM_top.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + waveguide_left_length + electrode_length*1000 + electrode_launch_radius + waveguide_two_arm_offset_length_for_heaters*1000 )
    heater_ref_top_MZM_top.movey( waveguide_yspacing / 2 + waveguide_sbend_geom[1] + second_sbens_gap/2 + (waveguide_width/2)*2 )
    
    heater_ref_top_MZM_bottom = c.add_ref(heater(
        only_heater=heater_only_heater, 
        heater_length=heater_length, 
        heater_width=heater_width, 
        pad_width=heater_pad_width, 
        pad_length=heater_pad_length,                      
        connection_buffer=heater_connection_buffer, 
        height_separation=heater_height_separation, 
        bottom_pad_width=heater_bottom_pad_width, 
        left_connection_width=heater_left_connection_width
    ))
   
    heater_ref_top_MZM_bottom.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + waveguide_left_length + electrode_length*1000 + electrode_launch_radius + waveguide_two_arm_offset_length_for_heaters*1000 )
    heater_ref_top_MZM_bottom.mirror((0,0),(1,0))
    heater_ref_top_MZM_bottom.movey( waveguide_yspacing / 2 - waveguide_sbend_geom[1] - second_sbens_gap/2 - (waveguide_width/2)*2  )

    heater_ref_bottom_MZM_top = c.add_ref(heater(
    only_heater=heater_only_heater, 
    heater_length=heater_length, 
    heater_width=heater_width, 
    pad_width=heater_pad_width, 
    pad_length=heater_pad_length,                      
    connection_buffer=heater_connection_buffer, 
    height_separation=heater_height_separation, 
    bottom_pad_width=heater_bottom_pad_width, 
    left_connection_width=heater_left_connection_width
    ))
    
    heater_ref_bottom_MZM_top.mirror((0,0),(0,1))
    heater_ref_bottom_MZM_top.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + waveguide_left_length + electrode_length*1000 + electrode_launch_radius + waveguide_two_arm_offset_length_for_heaters*1000 + heater_length )    
    heater_ref_bottom_MZM_top.movey( -waveguide_yspacing / 2 + waveguide_sbend_geom[1] + second_sbens_gap/2 + (waveguide_width/2)*2  )

    heater_ref_bottom_MZM_bottom = c.add_ref(heater(
    only_heater=heater_only_heater, 
    heater_length=heater_length, 
    heater_width=heater_width, 
    pad_width=heater_pad_width, 
    pad_length=heater_pad_length,                      
    connection_buffer=heater_connection_buffer, 
    height_separation=heater_height_separation, 
    bottom_pad_width=heater_bottom_pad_width, 
    left_connection_width=heater_left_connection_width
    ))
    
    heater_ref_bottom_MZM_bottom.mirror((0,0),(1,0))
    heater_ref_bottom_MZM_bottom.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_sbend_input_geom[0] + waveguide_left_length + waveguide_left_length + electrode_length*1000 + electrode_launch_radius + waveguide_two_arm_offset_length_for_heaters*1000 )    
    heater_ref_bottom_MZM_bottom.movey( -waveguide_yspacing / 2 - waveguide_sbend_geom[1] - second_sbens_gap/2 - (waveguide_width/2)*2  )


    return c





