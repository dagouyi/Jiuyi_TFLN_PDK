# import gdsfactory as gf
# import matplotlib.pyplot as plt

# from PSI_PDK import create_electrode_Ucell_duty_cycle
# from PSI_PDK import create_wg_crossing
# from PSI_PDK import create_electrode_Ucell
# from PSI_PDK import create_straight_mzm_1x1_wg
# from PSI_PDK import create_straight_mzm_1x2_wg
# from PSI_PDK import create_straight_mzm_2x1_wg
# from PSI_PDK import create_heater_single
# from PSI_PDK import create_electrode_launch

# layout = gf.Component()
# c1 = layout << create_electrode_Ucell_duty_cycle(h1=3, s=20, duty_cycle=20, gap=17, period=50, r=3, signal_height=50, ground_height=100)


# 创建组件
# c1 = layout << create_electrode_Ucell()
# c2 = layout << create_straight_mzm_1x1_wg()
# c3 = layout << create_heater_single()
# c4 = layout << create_electrode_launch()
# c5 = layout << create_straight_mzm_1x2_wg()
# c6 = layout << gf.components.mmi1x2(width=2, width_taper=3, length_taper=53, length_mmi=140, width_mmi=15, gap_mmi=4.5, layer = (2, 0))


import gdsfactory as gf
import matplotlib.pyplot as plt
# from PSI_PDK import create_straight_mzm_1x2_wg
# from PSI_PDK import create_straight_mzm_2x1_wg
# from PSI_PDK import create_straight_mzm_1x1_wg
# from PSI_PDK import create_straight_mzm_1x2  
# from PSI_PDK import create_electrode_Ucell
# from PSI_PDK import create_electrode_array
# # from PSI_PDK import create_electrode_launch
# from PSI_PDK import create_heater_single
# from psi_elements.IQ_modulator_wg import create_IQ_modulator_wg
# from psi_elements.IQ_modulator_with_electrode_and_heater import create_IQ_modulator
# from psi_elements. IQ_modulator_folded import create_IQ_modulator_folded
# from psi_elements. straight_MZM_1x1_with_electrode_and_heater import create_1x1_MZM_modulator
# from psi_elements. straight_MZM_1x2_with_electrode_and_heater import create_1x2_MZM_modulator
# from psi_elements. QPSK_modulator_folded import create_QPSK_modulator_folded
# from psi_elements.phase_modulator_folded import create_phase_modulator_folded
from psi_elements.Folded_MZM_wg import create_folded_MZM_wg


# Create a new layout component to hold both MZM and electrode 
layout = gf.Component()

length_of_MZM = 2 # in cm
waveguide_length = 2.5*1000 # in um

# Add MZM and electrode to the layout
#c1 = layout << create_straight_mzm_1x2_wg (layer_num = (1, 0), left_length = 500, right_length = 500, length = length_of_MZM, sbend_geom = [325, 33.5], mmi_length = 140, wg_width = 2, taper_width = 3, mmi_gap = 4.5, mmi_width = 15) # length unit is cm not um
#c1 = layout << create_straight_mzm_2x1_wg (layer_num = (1, 0), left_length = 500, right_length = 500, length = length_of_MZM, sbend_geom = [325, 33.5], mmi_length = 140, wg_width = 2, taper_width = 3, mmi_gap = 4.5, mmi_width = 15) # length unit is cm not um
# c2 = layout << create_electrode_Ucell
#c3 = layout << create_straight_mzm_1x1_wg(layer_num = (2, 0), left_length = 500, right_length = 500, length = length_of_MZM, sbend_geom = [325, 33.5], mmi_length = 140, wg_width = 2, taper_width = 3, mmi_gap = 4.5, mmi_width = 15) # length unit is cm not um
#c4 = layout << create_electrode_array(length = length_of_MZM, h1 = 3, s = 20, d = 45, gap = 15*2, period = 50, r = 3, signal_height = 50, ground_height = 100) # length unit is cm not um
#c5.movex(140+53+325+25) # x offset between wg and electrode = mmi z_length + mmi length_taper + x sbend_geom + half length of a single period electrode (50/2)

#c4 = layout << create_phase_electrode_array(length = length_of_MZM, h1 = 3, s = 20, d = 45, gap = 18*2, period = 50, r = 3, signal_height = 100, ground_height = 100) # length unit is cm not um

#c6 = layout << create_heater_single()
#c7 = layout << MZM

# c8 = layout << create_electrode_launch(
#     is_left = False, 
#     radius = 612, 
#     outer_width = 96, 
#     inner_width = 84, 
#     pitch = 1102, 
#     gap = 13, 
#     signal_height = 150, 
#     ground_height = 100, 
#     npts = 50)






################################################################## for phase modulator folded

# electrode_signal_height = 100
# electrode_ground_height = 100
# electrodes_gap = 17



# c9 = layout << create_phase_modulator_folded(
#     waveguide_width = 2,  # The LN waveguide width    
#     waveguide_layer_num = (2, 0),  # layer of the layout, (2,0) is for the LN rib layer
#     waveguide_length_1 = waveguide_length,
#     waveguide_length_2 = waveguide_length,    
#     electrode_length = 2,
#     electrode_distance_base_to_T = 3,
#     electrode_T_base_width = 20,
#     electrode_T_width = 45,
#     electrodes_gap = electrodes_gap,
#     electrode_period = 50,
#     electrode_T_top_thickness = 3,
#     electrode_signal_height = electrode_signal_height,
#     electrode_ground_height = electrode_ground_height,
#     electrode_launch_is_left = False,
#     electrode_launch_radius = 612,  # electrode launch radius
#     electrode_launch_outer_width = electrode_signal_height, # width of ground launch pads on outside
#     electrode_launch_inner_width = electrode_ground_height, # width of signal launch pad
#     electrode_launch_pitch = 102, #  distance between probe contacts
#     electrode_launch_gap = electrodes_gap, #  distance between electrodes
#     electrode_launch_signal_height = electrode_signal_height, #  signal electrode width (or height, depending on how you look at it)
#     electrode_launch_ground_height = electrode_ground_height, #  ground electrodes width (or height, depending on how you look at it)
#     electrode_launch_npts = 50,  #  number of points in arc    
#     arc_waveguide_radius=200,  # New parameter for the radius of the arc waveguide
#     waveguide_electrode_offset = 200

# )

##################################################################### folded MZM


# #  MZM part parameters:
# wg_width=2  # The LN waveguide width
# length_of_MZM = 2 # the length of MZM, nuit in cm !!!
# MZM_length_additional = 0.5 /1000 # the addition offset length between electrode_launch and heater, renomalized the length unit to cm

# # electrode launch and heater part parameters:
# two_arm_offset_length_for_heaters = 200 /1000
# electrode_launch_radius = 618.0 # the radius of electrode launch, , renomalized the length unit to cm
# electrode_launch_radius_normalized = electrode_launch_radius/1000.0
# heater_length = 618 # the length of heater, renomalized the length unit to cm
# heater_length_normalized = heater_length/1000
# MZM_length_offset_for_electrode_launch_and_heater = MZM_length_additional  + heater_length_normalized + two_arm_offset_length_for_heaters #+ electrode_launch_radius_normalized
# total_length_of_MZM = length_of_MZM + MZM_length_offset_for_electrode_launch_and_heater

# mmi and sbends part parameters:
# yspacing = 850 # The spacing between two parallel MZMs
# mmi_gap = 6.5 # The gap between two output taper of MMIs
# taper_width = 3 # input mmi taper width
# sbend_geom=[325, 90]
# first_sbends_gap = ((taper_width/2+ taper_width/2+ mmi_gap)-(wg_width/2+wg_width/2))/2 + (wg_width/2+wg_width/2)/2
# second_sbens_gap = (taper_width/2+ taper_width/2+ mmi_gap)-(wg_width/2+wg_width/2) - wg_width/2 - wg_width/2
# sbend_input_geom = [1530, yspacing/2 - first_sbends_gap] # the x-axis length and y-axis length of the sbend bewteen the input MMI and two parallel MZMs

# # electrode part parameters:
# electrode_length = 1.8
# electrode_distance_base_to_T = 3
# electrode_T_top_thickness = 3
# electrodes_gap = 15
# electrode_signal_height = sbend_geom[1]*2 + second_sbens_gap -  electrode_distance_base_to_T*2 - electrode_T_top_thickness*2 - 2*(electrodes_gap/2) + 2*wg_width
# electrode_ground_height = 150


# c9 = layout << create_folded_MZM_wg(
#     waveguide_width = 2,  # The LN waveguide width
#     waveguide_length_of_MZM = 2, # the length of the MZMs, unit in cm !!!
#     waveguide_layer_num = (2, 0),  # layer of the layout, (2,0) is for the LN rib layer
#     waveguide_left_length = 500,  # the length of the very left input waveguide
#     waveguide_right_length = 500,  # the length of the very right input waveguide 
#     waveguide_sbend_geom = [325, 33.5],         # The sbend inside two parallel MZMs
#     # waveguide_two_arm_offset_length_for_heaters = 200 /1000,
#     mmi_length = 140,  # the length of the MMIs
#     mmi_length_taper = 53,    
#     mmi_taper_width= 3,  # the length of the tapers of MMIs
#     mmi_gap= 4.5,  # The gap between two output taper of MMIs
#     mmi_width= 15,  # the width of the MMIs 
#     electrode_length = 2,
#     electrode_distance_base_to_T = 3,
#     electrode_T_base_width = 20,
#     electrode_T_width = 45,
#     electrodes_gap = 17,
#     electrode_period = 50,
#     electrode_T_top_thickness = 3,
#     electrode_signal_height = 150,
#     electrode_ground_height = 100,
#     # electrode_launch_is_left = False,
#     # electrode_launch_radius = 612,  # electrode launch radius
#     # electrode_launch_outer_width = 96, # width of ground launch pads on outside
#     # electrode_launch_inner_width = 84, # width of signal launch pad
#     # electrode_launch_pitch = 102, #  distance between probe contacts
#     # electrode_launch_gap = 13, #  distance between electrodes
#     # electrode_launch_signal_height = 50, #  signal electrode width (or height, depending on how you look at it)
#     # electrode_launch_ground_height = 100, #  ground electrodes width (or height, depending on how you look at it)
#     # electrode_launch_npts = 50,  #  number of points in arc
#     # heater_only_heater = False,
#     # heater_length = 613,
#     # heater_width = 4,
#     # heater_pad_width=60,
#     # heater_pad_length = 446,
#     # heater_connection_buffer = 15,
#     # heater_height_separation = 45,
#     # heater_bottom_pad_width = 23.2,
#     # heater_left_connection_width = 13.4

    


# )
c9 = layout << create_folded_MZM_wg(
    waveguide_width=2,  # The LN waveguide width
    waveguide_length_of_MZM=2,  # The length of the MZMs, unit in cm
    waveguide_layer_num=(2, 0),  # Layer of the layout, (2,0) is for the LN rib layer
    waveguide_left_length=500,  # The length of the very left input waveguide
    waveguide_right_length=500,  # The length of the very right input waveguide
    waveguide_sbend_geom=[325, 33.5],  # The S-bend inside two parallel MZMs
    mmi_length=140,  # The length of the MMIs
    mmi_length_taper=53,  # The length of the tapers of MMIs
    mmi_taper_width=3,  # The taper width of MMIs
    mmi_gap=4.5,  # The gap between two output taper of MMIs
    mmi_width=15,  # The width of the MMIs
    MZM_distance=600,  # The distance between MZMs
)






# 将组件旋转90度
# c2 = c1.rotate(angle=-45)

# # 可视化布局
# layout.show(crossing_rotated)




layout.plot()
layout.show(show_ports = True)

# Export the layout to a GDS file
gds_file_path = "IQ modulator waveguide.gds"
layout.write_gds(gds_file_path)
print(f"GDS file saved as {gds_file_path}")
layout.plot_matplotlib(show_ports = True)
plt.show()