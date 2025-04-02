import gdsfactory as gf

from PSI_PDK import create_straight_mzm_1x2_wg
from PSI_PDK import create_electrode_Ucell
from PSI_PDK import create_straight_mzm_1x1_wg
from PSI_PDK import create_electrode_array
from PSI_PDK import create_straight_mzm_1x2  
from PSI_PDK import create_heater_single



# Create a new layout component to hold both MZM and electrode
layout = gf.Component()

length_of_MZM = 2 # in cm

# Add MZM and electrode to the layout
#c1 = layout << MZM_1x2
#c2 = layout << electrode
c3 = layout << create_straight_mzm_1x1_wg(layer_num = (2, 0), left_length = 500, right_length = 500, length = length_of_MZM, sbend_geom = [325, 33.5], mmi_length = 140, wg_width = 2, taper_width = 3, mmi_gap = 4.5, mmi_width = 15) # length unit is cm not um
c4 = layout << create_electrode_array(length = length_of_MZM, h1 = 3, s = 20, d = 45, gap = 12.5*2, period = 50, r = 3, signal_height = 50, ground_height = 100) # length unit is cm not um
c4.movex(140+53+325+25) # x offset between wg and electrode = mmi z_length + mmi length_taper + x sbend_geom + half length of a single period electrode (50/2)
c5 = layout << create_heater_single()
#c6 = layout << MZM

# Position the electrode relative to MZM if needed
#electrode_ref.movex(MZM_1x2.xsize + 10)  # Adjust the offset as required

# Display the layout component
layout.plot()
layout.show()

# Export the layout to a GDS file
gds_file_path = "straight_mzm_1x2_with_electrode.gds"
layout.write_gds(gds_file_path)
print(f"GDS file saved as {gds_file_path}")
