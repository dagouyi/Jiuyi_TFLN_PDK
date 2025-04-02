import gdsfactory as gf
from PSI_PDK import create_straight_mzm_1x1_wg_right_open as mzm_right_open
from PSI_PDK import create_wg_crossing
from gdsfactory.component import Component
import config as cf

def create_folded_MZM_wg(
    waveguide_width=2,  # The LN waveguide width
    waveguide_length_of_MZM=2,  # The length of the MZMs, unit in cm    
    waveguide_left_length=500,  # The length of the very left input waveguide
    waveguide_right_length=500,  # The length of the very right input waveguide
    waveguide_sbend_geom=[325, 33.5],  # The S-bend inside two parallel MZMs
    mmi_length=140,  # The length of the MMIs
    mmi_length_taper=53,  # The length of the tapers of MMIs
    mmi_taper_width=3,  # The taper width of MMIs
    mmi_gap=4.5,  # The gap between two output taper of MMIs
    mmi_width=15,  # The width of the MMIs
    MZM_distance=600,  # The distance between MZMs
):
    c = gf.Component()

    # Create the first MZM
    mzm_1_ref = c << mzm_right_open(
        layer_num=waveguide_layer_num,
        left_length=waveguide_left_length,
        right_length=waveguide_right_length,
        length=waveguide_length_of_MZM,
        sbend_geom=waveguide_sbend_geom,
        mmi_length=mmi_length,
        mmi_length_taper=mmi_length_taper,
        wg_width=waveguide_width,
        taper_width=mmi_taper_width,
        mmi_gap=mmi_gap,
        mmi_width=mmi_width,
    )

    # Position the first MZM
    mzm_1_ref.movex(waveguide_left_length + mmi_length + mmi_length_taper)

    # Create the second MZM
    mzm_2_ref = c << mzm_right_open(
        layer_num=waveguide_layer_num,
        left_length=waveguide_left_length,
        right_length=waveguide_right_length,
        length=waveguide_length_of_MZM,
        sbend_geom=waveguide_sbend_geom,
        mmi_length=mmi_length,
        mmi_length_taper=mmi_length_taper,
        wg_width=waveguide_width,
        taper_width=mmi_taper_width,
        mmi_gap=mmi_gap,
        mmi_width=mmi_width,
    )

    # Position the second MZM
    mzm_2_ref.movex(waveguide_left_length + mmi_length + mmi_length_taper)
    mzm_2_ref.movey(-MZM_distance)

    # Create and position the waveguide crossing
    waveguide_crossing = c << create_wg_crossing()
    waveguide_crossing.rotate(angle=-45)
    waveguide_crossing.movex(
        waveguide_left_length + mmi_length + mmi_length_taper * 2
    )
    waveguide_crossing.movey(-MZM_distance / 2)

    # Route between the waveguide crossing and the first MZM
    route = gf.routing.route_dubin(
        component=c,
        port1=waveguide_crossing.ports["o1"],
        port2=mzm_1_ref.ports["o1"],
        cross_section=gf.cross_section.strip(width=waveguide_width, radius=200),
    )
    # c.add(route.references)
    c

    # Route between the waveguide crossing and the second MZM
    route2 = gf.routing.route_dubin(
        component=c,
        port1=waveguide_crossing.ports["o2"],
        port2=mzm_2_ref.ports["o1"],
        cross_section=gf.cross_section.strip(width=waveguide_width, radius=200),
    )
    # c.add(route2.references)
    c

    return c

# Create and visualize the folded MZM layout
c = create_folded_MZM_wg()
c.plot()








# import gdsfactory as gf
# from PSI_PDK import create_straight_mzm_1x1_wg_right_open as mzm_right_open
# from PSI_PDK import create_wg_crossing
# from PSI_PDK import create_electrode_array as electrode
# # from PSI_PDK import create_electrode_launch
# from PSI_PDK import create_heater_single as heater
# from gdsfactory.component import Component






# def create_folded_MZM_wg(
#     waveguide_width = 2,  # The LN waveguide width
#     waveguide_length_of_MZM = 2, # the length of the MZMs, unit in cm !!!
#     waveguide_layer_num = (2, 0),  # layer of the layout, (2,0) is for the LN rib layer
#     waveguide_left_length = 500,  # the length of the very left input waveguide
#     waveguide_right_length = 500,  # the length of the very right input waveguide 
#     waveguide_sbend_geom = [325, 33.5],         # The sbend inside two parallel MZMs
#     waveguide_two_arm_offset_length_for_heaters = 200 /1000,
#     mmi_length = 140,  # the length of the MMIs
#     mmi_length_taper = 53,    
#     mmi_taper_width= 3,  # the length of the tapers of MMIs
#     mmi_gap= 4.5,  # The gap between two output taper of MMIs
#     mmi_width= 15,  # the width of the MMIs 
#     # electrode_length = 2,
#     # electrode_distance_base_to_T = 3,
#     # electrode_T_base_width = 20,
#     # electrode_T_width = 45,
#     # electrodes_gap = 17,
#     # electrode_period = 50,
#     # electrode_T_top_thickness = 3,
#     # electrode_signal_height = 150,
#     # electrode_ground_height = 100,
#     # electrode_launch_is_left = False,
#     # electrode_launch_radius = 612,  # electrode launch radius
#     # electrode_launch_outer_width = 96, # width of ground launch pads on outside
#     # electrode_launch_inner_width = 84, # width of signal launch pad
#     # electrode_launch_pitch = 102, #  distance between probe contacts
#     # electrode_launch_gap = 13, #  distance between electrodes
#     # electrode_launch_signal_height = 50, #  signal electrode width (or height, depending on how you look at it)
#     # electrode_launch_ground_height = 100, #  ground electrodes width (or height, depending on how you look at it)
#     # electrode_launch_npts = 50,  #  number of points in arc
#     MZM_distance = 600 # the distance between MZMs
#     # heater_only_heater = False,
#     # heater_length = 613,
#     # heater_width = 4,
#     # heater_pad_width=60,
#     # heater_pad_length = 446,
#     # heater_connection_buffer = 15,
#     # heater_height_separation = 45,
#     # heater_bottom_pad_width = 23.2,
#     # heater_left_connection_width = 13.4

    


# ) -> gf.Component:
#     """
#     Create a dual polarization coherent transmitter layout with two MMIs, two MZMs, and connecting waveguides.

#     Returns:
#         gf.Component: The complete layout for a dual polarization coherent transmitter.
#     """
#     c = gf.Component()

#     first_sbends_gap = ((mmi_taper_width/2+ mmi_taper_width/2+ mmi_gap)-(waveguide_width/2+waveguide_width/2))/2 + (waveguide_width/2+waveguide_width/2)/2
#     second_sbens_gap = (mmi_taper_width/2+ mmi_taper_width/2+ mmi_gap)-(waveguide_width/2+waveguide_width/2) - waveguide_width/2 - waveguide_width/2
#     sbend_input_geom = [1530,  - first_sbends_gap] # the x-axis length and y-axis length of the sbend bewteen the input MMI and two parallel MZMs

   
#     # Create the MZM
#     mzm_1_ref = c << mzm_right_open(
#         layer_num=waveguide_layer_num,
#         left_length=waveguide_left_length,
#         right_length=waveguide_right_length,
#         length=waveguide_length_of_MZM,
#         sbend_geom=waveguide_sbend_geom,
#         mmi_length=mmi_length,
#         mmi_length_taper = mmi_length_taper,
#         wg_width=waveguide_width,
#         taper_width=mmi_taper_width,
#         mmi_gap=mmi_gap,
#         mmi_width=mmi_width
#     )

#     c.add_port("MZM_1_output_top", port= mzm_1_ref.ports["o2"], port_type="optical")
    
#     # Position the MZMs
#     mzm_1_ref.movex(waveguide_left_length+mmi_length+mmi_length_taper+ mmi_length_taper)

#         # Create the MZM
#     mzm_2_ref = c << mzm_right_open(
#         layer_num=waveguide_layer_num,
#         left_length=waveguide_left_length,
#         right_length=waveguide_right_length,
#         length=waveguide_length_of_MZM,
#         sbend_geom=waveguide_sbend_geom,
#         mmi_length=mmi_length,
#         mmi_length_taper = mmi_length_taper,
#         wg_width=waveguide_width,
#         taper_width=mmi_taper_width,
#         mmi_gap=mmi_gap,
#         mmi_width=mmi_width
#     )
    
#     # Position the MZMs
#     mzm_2_ref.movex(waveguide_left_length+mmi_length+mmi_length_taper+ mmi_length_taper)
#     mzm_2_ref.movey(-MZM_distance)
    
#     # electrode_top_MZM = c.add_ref(electrode(
#     #     length=electrode_length,
#     #     h1=electrode_distance_base_to_T,
#     #     s=electrode_T_base_width,
#     #     d=electrode_T_width,
#     #     gap=electrodes_gap,
#     #     period=electrode_period,
#     #     r=electrode_T_top_thickness,
#     #     signal_height=electrode_signal_height,
#     #     ground_height=electrode_ground_height
#     # ))
#     # electrode_top_MZM.movex(mmi_length_taper + mmi_length + mmi_length_taper  + waveguide_left_length + mmi_length_taper + mmi_length + waveguide_sbend_geom[0] + electrode_period / 2)
    

#     # Create and place the electrode launch
#     # electrode_launch_ref_top_MZM = c.add_ref(create_electrode_launch(
#     #     is_left=electrode_launch_is_left, 
#     #     radius=electrode_launch_radius, 
#     #     outer_width=electrode_launch_outer_width, 
#     #     inner_width=electrode_launch_inner_width, 
#     #     pitch=electrode_launch_pitch, 
#     #     gap=electrode_launch_gap, 
#     #     signal_height=electrode_launch_signal_height, 
#     #     ground_height=electrode_launch_ground_height, 
#     #     npts=electrode_launch_npts
#     # ))
    
#     # electrode_launch_ref_top_MZM.movex(mmi_length+ mmi_length_taper  + waveguide_left_length + mmi_length_taper + mmi_length + mmi_length_taper+ waveguide_sbend_geom[0] + electrode_length*1000)    
#     # electrode_launch_ref_top_MZM.movey( (electrode_launch_radius-electrode_launch_outer_width -electrode_launch_gap - (electrode_launch_inner_width)/2))
   
#     # heater_ref_top_MZM_top = c.add_ref(heater(
#     #     only_heater=heater_only_heater, 
#     #     heater_length=heater_length, 
#     #     heater_width=heater_width, 
#     #     pad_width=heater_pad_width, 
#     #     pad_length=heater_pad_length,                      
#     #     connection_buffer=heater_connection_buffer, 
#     #     height_separation=heater_height_separation, 
#     #     bottom_pad_width=heater_bottom_pad_width, 
#     #     left_connection_width=heater_left_connection_width
#     # ))
    
#     # heater_ref_top_MZM_top.movex(mmi_length_taper + mmi_length + mmi_length_taper + waveguide_left_length + waveguide_left_length + electrode_length*1000 + electrode_launch_radius + waveguide_two_arm_offset_length_for_heaters*1000 )
#     # heater_ref_top_MZM_top.movey( waveguide_sbend_geom[1] + second_sbens_gap/2 + (waveguide_width/2)*2 )
    
#     # heater_ref_top_MZM_bottom = c.add_ref(heater(
#     #     only_heater=heater_only_heater, 
#     #     heater_length=heater_length, 
#     #     heater_width=heater_width, 
#     #     pad_width=heater_pad_width, 
#     #     pad_length=heater_pad_length,                      
#     #     connection_buffer=heater_connection_buffer, 
#     #     height_separation=heater_height_separation, 
#     #     bottom_pad_width=heater_bottom_pad_width, 
#     #     left_connection_width=heater_left_connection_width
#     # ))
   
#     # heater_ref_top_MZM_bottom.movex(mmi_length_taper + mmi_length + mmi_length_taper  + waveguide_left_length + waveguide_left_length + electrode_length*1000 + electrode_launch_radius + waveguide_two_arm_offset_length_for_heaters*1000 )
#     # heater_ref_top_MZM_bottom.mirror((0,0),(1,0))
#     # heater_ref_top_MZM_bottom.movey(- waveguide_sbend_geom[1] - second_sbens_gap/2 - (waveguide_width/2)*2  )

#     waveguide_crossing = c << create_wg_crossing() 
#     waveguide_crossing.rotate(angle=-45)
#     waveguide_crossing.movex(mmi_length_taper + mmi_length + mmi_length_taper  + waveguide_left_length + waveguide_left_length)+ #electrode_length*1000) + electrode_launch_radius)
#     waveguide_crossing.movey(-MZM_distance/2)

      


# route = gf.routing.route_dubin(
#     c,
#     port1=waveguide_crossing.ports["o1"],
#     port2=mzm_1_ref.ports["o2"],
#     cross_section=gf.cross_section.strip(width=waveguide_width, radius=200),
#     )
# c



# #     route = gf.routing.route_dubin(
# #         input_port=waveguide_crossing.ports["o1"],
# #         output_port=mzm_1_ref.ports["o2"],
# #         # bend=bend_euler,
# #         # radius=5,
# #         # straight=straight_function,
# # )
# #     c.add(route.references)

# #     gf.routing.get_route(
# #     input_port = waveguide_crossing.ports["o1"],
# #     output_port = waveguide_crossing.ports["o2"],
# #     # output_port = mzm_1_ref.ports["o2"],
# #     bend  = bend_euler,
# #     # with_sbend = False,
# #     straight = straight_function,
# #     # taper = None,
# #     # start_straight_length = None,
# #     # end_straight_length = None,
# #     # min_straight_length = 10e-3,
# #     # auto_widen = False,
# #     # auto_widen_minimum_length = 100,
# #     # taper_length  = 10,
# #     # width_wide = 2,
# #     # cross_section = "strip",
    
# # )
    
#     # c.pprint_ports()    

#     return c