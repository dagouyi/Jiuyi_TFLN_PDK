""" Global configuration file for editing variables across modules 

    SIN_WG_LAYER: KLayout layer for hybrid loaded SiN waveguides = (1, 0)
    LN_WG_LAYER: KLayout layer for ridge etch TFLN waveguides = (2, 0)
    HEATER_LAYER: KLayout layer for NiCr heaters = (20, 0)
    ELECTRODE_LAYER: KLayout layer for gold electrodes = (31, 0)
    LN_WG_WIDTH: Default width for ridge etch TFLN waveguides = 1
    SIN_WG_WIDTH: Default width for hybrid loaded SiN waveguides = 2

    SIN_SI_MMI_1x2_LENGTH: Length of 1x2 mmi region for hybrid SiN on Silicon = 140
    SIN_SI_MMI_2x2_LENGTH: Length of 2x2 mmi region for hybrid SiN on Silicon = 636
    SIN_QZ_MMI_1x2_LENGTH: Length of 1x2 mmi region for hybrid SiN on Quartz  = 140
    SIN_QZ_MMI_2x2_LENGTH: Length of 2x2 mmi region for hybrid SiN on Quartz  = 636
    SIN_SI_MMI_1x2_WIDTH: Width of 1x2 mmi region for hybrid SiN on Silicon  = 15  
    SIN_SI_MMI_2x2_WIDTH: Width of 2x2 mmi region for hybrid SiN on Silicon  = 15  
    SIN_QZ_MMI_1x2_WIDTH: Width of 1x2 mmi region for hybrid SiN on Quartz   = 15  
    SIN_QZ_MMI_2x2_WIDTH: Width of 2x2 mmi region for hybrid SiN on Quartz   = 15  

    RIDGE_SI_MMI_1x2_LENGTH: Length of 1x2 mmi region for ridge etched TFLN on Silicon = 160.4
    RIDGE_SI_MMI_2x2_LENGTH: Length of 2x2 mmi region for ridge etched TFLN on Silicon = 160.4
    RIDGE_QZ_MMI_1x2_LENGTH: Length of 1x2 mmi region for ridge etched TFLN on Quartz  = 160.4
    RIDGE_QZ_MMI_2x2_LENGTH: Length of 2x2 mmi region for ridge etched TFLN on Quartz  = 160.4
    RIDGE_SI_MMI_1x2_WIDTH: Length of 1x2 mmi region for ridge etched TFLN on Silicon  = 15    
    RIDGE_SI_MMI_2x2_WIDTH: Length of 2x2 mmi region for ridge etched TFLN on Silicon  = 15    
    RIDGE_QZ_MMI_1x2_WIDTH: Length of 1x2 mmi region for ridge etched TFLN on Quartz   = 15    
    RIDGE_QZ_MMI_2x2_WIDTH: Length of 2x2 mmi region for ridge etched TFLN on Quartz   = 15    

    SIN_SI_SBEND_GEOM:   XY Geometry tuple for s-bends emerging from hybrid SiN on Silicon MMI   = (241.22, 30)
    SIN_QZ_SBEND_GEOM:   XY Geometry tuple for s-bends emerging from hybrid SiN on Quartz MMI    = (241.22, 30)
    RIDGE_SI_SBEND_GEOM: XY Geometry tuple for s-bends emerging from ridge TFLN on Silicon MMI = (241.964, 30)
    RIDGE_QZ_SBEND_GEOM: XY Geometry tuple for s-bends emerging from ridge TFLN on Quartz MMI  = (325, 48.25)
"""

# -------------------------------------- KLayout layer numbers --------------------------------------------------- #
SIN_WG_LAYER: tuple                       =        (1, 0)    # KLayout layer for hybrid loaded SiN waveguides
LN_WG_LAYER: tuple                        =        (2, 0)    # KLayout layer for ridge etch TFLN waveguides 
SION_ETCH_LAYER: tuple                    =        (4, 0)    # KLayout layer for SiON etch 
OXIDE_ETCH_LAYER: tuple                   =       (12, 0)    # KLayout layer for oxide etch back
HEATER_LAYER: tuple                       =       (20, 0)    # KLayout layer for NiCr heaters
VTC_ETCH_LAYER: tuple                     =       (24, 0)    # KLayout layer for Vertical Taper Couper 
ELECTRODE_LAYER: tuple                    =       (31, 0)    # KLayout layer for gold electrodes
DICING_KERF_LAYER: tuple                  =       (50, 0)    # KLayout layer for dicing kerfs
FILL_KEEPOUT_LAYER: tuple                 =       (72, 0)    # KLayout layer for fill pattern on wafer/substrate
WAFER_BOUNDARY_LAYER: tuple               =       (90, 0)    # KLayout layer for wafer/substrate boundary
CHIP_BOUNDARY_LAYER: tuple                =       (91, 0)    # KLayout layer for device (chip) boundary
PIC_BOUNDARY_LAYER: tuple                 =       (92, 0)    # KLayout layer for PIC boundary
EBR_LAYER: tuple                          =       (96, 0)    # KLayout layer for edge bead removal region
ALIGNMENT_BOUNDARY_LAYER: tuple           =       (99, 0)    # KLayout layer for alignment boundary marks
ALIGNMENT_LAYER: tuple                    =      (120, 0)    # KLayout layer for alignment marks - default
ID_LAYER: tuple                           =      (121, 0)    # KLayout layer for ID markup


# -------------------------------------- Waveguide Widths --------------------------------------------------- #
LN_WG_WIDTH_SI: float                     =             1    # Default width for ridge etch TFLN waveguides on Silicon
LN_WG_WIDTH_QZ: float                     =             1    # Default width for ridge etch TFLN waveguides on Quartz
SIN_WG_WIDTH_SI: float                    =             2    # Default width for ridge etch TFLN waveguides on Silicon
SIN_WG_WIDTH_QZ: float                    =             2    # Default width for hybrid loaded SiN waveguides on Quartz


# -------------------------------------- SiN on Silicon mmi --------------------------------------------------- #
SIN_SI_MMI_1x2_LENGTH: float              =           140    # Length of 1x2 mmi region for hybrid SiN on Silicon
SIN_SI_MMI_1x2_WIDTH:  float              =            15    # Width of 1x2 mmi region for hybrid SiN on Silicon
SIN_SI_MMI_1x2_TAPER_LENGTH: float        =          52.5    # Length of taper for hybrid SiN on Silicon MMI 1x2
SIN_SI_MMI_1x2_TAPER_WIDTH: float         =           7.0    # Width of taper for hybrid SiN on Silicon MMI 1x2
SIN_SI_MMI_1x2_TAPER_GAP: float           =             1    # Width of taper for hybrid SiN on Silicon MMI 1x2
SIN_SI_MMI_1x2_STRAIGHT_LENGTH: float     =            26    # Width of taper for hybrid SiN on Silicon MMI 1x2

SIN_SI_MMI_2x2_LENGTH: float              =           636    # Length of 2x2 mmi region for hybrid SiN on Silicon
SIN_SI_MMI_2x2_WIDTH:  float              =            15    # Width of 2x2 mmi region for hybrid SiN on Silicon
SIN_SI_MMI_2x2_TAPER_LENGTH: float        =          52.5    # Length of taper for hybrid SiN on Silicon MMI 2x2
SIN_SI_MMI_2x2_TAPER_WIDTH: float         =           7.0    # Width of taper for hybrid SiN on Silicon MMI 2x2
SIN_SI_MMI_2x2_TAPER_GAP: float           =             1    # Width of taper for hybrid SiN on Silicon MMI 2x2
SIN_SI_MMI_2x2_STRAIGHT_LENGTH: float     =            26    # Width of taper for hybrid SiN on Silicon MMI 2x2

# -------------------------------------- SiN on Quartz mmi ---------------------------------------------------- #
SIN_QZ_MMI_1x2_LENGTH: float              =           140    # Length of 1x2 mmi region for hybrid SiN on Quartz 
SIN_QZ_MMI_1x2_WIDTH:  float              =            15    # Width of 1x2 mmi region for hybrid SiN on Quartz 
SIN_QZ_MMI_1x2_TAPER_LENGTH: float        =          52.5    # Length of taper for hybrid SiN on Quartz MMI 1x2
SIN_QZ_MMI_1x2_TAPER_WIDTH: float         =           7.0    # Width of taper for hybrid SiN on QuartzMMI 1x2
SIN_QZ_MMI_1x2_TAPER_GAP: float           =             1    # Width of taper for hybrid SiN on Quartz MMI 1x2
SIN_QZ_MMI_1x2_STRAIGHT_LENGTH: float     =            26    # Width of taper for hybrid SiN on Quartz MMI 1x2

SIN_QZ_MMI_2x2_LENGTH: float              =           636    # Length of 2x2 mmi region for hybrid SiN on Quartz 
SIN_QZ_MMI_2x2_WIDTH:  float              =            15    # Width of 2x2 mmi region for hybrid SiN on Quartz 
SIN_QZ_MMI_2x2_TAPER_LENGTH: float        =          52.5    # Length of taper for hybrid SiN on Quartz MMI 2x2
SIN_QZ_MMI_2x2_TAPER_WIDTH: float         =           7.0    # Width of taper for hybrid SiN on Quartz MMI 2x2
SIN_QZ_MMI_2x2_TAPER_GAP: float           =             1    # Width of taper for hybrid SiN on Quartz MMI 2x2
SIN_QZ_MMI_2x2_STRAIGHT_LENGTH: float     =            26    # Width of taper for hybrid SiN on Quartz MMI 2x2

# -------------------------------------- Ridge on Silicon mmi ------------------------------------------------ #
RIDGE_SI_MMI_1x2_LENGTH: float            =         160.4    # Length of 1x2 mmi region for ridge etched TFLN on Silicon
RIDGE_SI_MMI_1x2_WIDTH : float            =            15    # Width of 1x2 mmi region for ridge etched TFLN on Silicon
RIDGE_SI_MMI_1x2_TAPER_LENGTH: float      =            45    # Length of taper for ridge TFLN on Silicon MMI 1x2
RIDGE_SI_MMI_1x2_TAPER_WIDTH: float       =             3    # Width of taper for ridge TFLN on Silicon MMI 1x2
RIDGE_SI_MMI_1x2_TAPER_GAP: float         =           4.5    # Width of taper for ridge TFLN on Silicon MMI 1x2
RIDGE_SI_MMI_1x2_STRAIGHT_LENGTH: float   =            20    # Width of taper for ridge TFLN on Silicon MMI 1x2

RIDGE_SI_MMI_2x2_LENGTH: float            =       138.712    # Length of 2x2 mmi region for ridge etched TFLN on Silicon
RIDGE_SI_MMI_2x2_WIDTH : float            =            12    # Width of 2x2 mmi region for ridge etched TFLN on Silicon
RIDGE_SI_MMI_2x2_TAPER_LENGTH: float      =          52.5    # Length of taper for ridge TFLN on Silicon MMI 2x2
RIDGE_SI_MMI_2x2_TAPER_WIDTH: float       =             3    # Width of taper for ridge TFLN on Silicon MMI 2x2
RIDGE_SI_MMI_2x2_TAPER_GAP: float         =           1.5    # Width of taper for ridge TFLN on Silicon MMI 2x2
RIDGE_SI_MMI_2x2_STRAIGHT_LENGTH: float   =            20    # Width of taper for ridge TFLN on Silicon MMI 2x2

# -------------------------------------- Ridge on Quartz mmi -------------------------------------------------- #
RIDGE_QZ_MMI_1x2_LENGTH: float            =         160.4    # Length of 1x2 mmi region for ridge etched TFLN on Quartz 
RIDGE_QZ_MMI_1x2_WIDTH : float            =            15    # Width of 1x2 mmi region for ridge etched TFLN on Quartz 
RIDGE_QZ_MMI_1x2_TAPER_LENGTH: float      =            45    # Length of taper for ridge TFLN on Quartz MMI 1x2
RIDGE_QZ_MMI_1x2_TAPER_WIDTH: float       =             3    # Width of taper for ridge TFLN on Quartz MMI 1x2
RIDGE_QZ_MMI_1x2_TAPER_GAP: float         =           4.5    # Width of taper for ridge TFLN on Quartz MMI 1x2
RIDGE_QZ_MMI_1x2_STRAIGHT_LENGTH: float   =            20    # Width of taper for ridge TFLN on Quartz MMI 1x2
 
RIDGE_QZ_MMI_2x2_LENGTH: float            =       138.642    # Length of 2x2 mmi region for ridge etched TFLN on Quartz
RIDGE_QZ_MMI_2x2_WIDTH : float            =            12    # Width of 2x2 mmi region for ridge etched TFLN on Quartz 
RIDGE_QZ_MMI_2x2_TAPER_LENGTH: float      =            44    # Length of taper for ridge TFLN on Quartz MMI 2x2
RIDGE_QZ_MMI_2x2_TAPER_WIDTH: float       =           2.5    # Width of taper for ridge TFLN on Quartz MMI 2x2
RIDGE_QZ_MMI_2x2_TAPER_GAP: float         =           1.5    # Width of taper for ridge TFLN on Quartz MMI 2x2
RIDGE_QZ_MMI_2x2_STRAIGHT_LENGTH: float   =            20    # Width of taper for ridge TFLN on Quartz MMI 2x2

# -------------------------------------- S Bend Geometries coming out of mmi -------------------------------------------------- #
# might need to append with geometries for 1x2 vs 2x2

SIN_SI_SBEND_GEOM: tuple              =      (241.22, 30)    # XY Geometry tuple for s-bends emerging from hybrid SiN on Silicon MMI
SIN_QZ_SBEND_GEOM: tuple              =      (241.22, 30)    # XY Geometry tuple for s-bends emerging from hybrid SiN on Quartz MMI 
RIDGE_SI_SBEND_GEOM: tuple            =     (217.751, 32)    # XY Geometry tuple for s-bends emerging from ridge TFLN on Silicon MMI
RIDGE_QZ_SBEND_GEOM: tuple            =      (325, 48.25)    # XY Geometry tuple for s-bends emerging from ridge TFLN on Quartz MMI 
SIN_SI_SBEND_OUTPUT_GEOM: tuple       =    (500.373, 125)    # OUTPUT XY Geometry tuple for s-bends emerging from hybrid SiN on Silicon MMI
SIN_QZ_SBEND_OUTPUT_GEOM: tuple       =    (500.373, 125)    # OUTPUT XY Geometry tuple for s-bends emerging from hybrid SiN on Quartz MMI 
RIDGE_SI_SBEND_OUTPUT_GEOM: tuple     =        (325, 125)    # OUTPUT XY Geometry tuple for s-bends emerging from ridge TFLN on Silicon MMI
RIDGE_QZ_SBEND_OUTPUT_GEOM: tuple     =        (325, 125)    # OUTPUT XY Geometry tuple for s-bends emerging from ridge TFLN on Quartz MMI 

# -------------------------------------- Electrode T geometry -------------------------------------------------- #
# see https://ieeexplore.ieee.org/document/5634046
H1_SIN_SI             =                                 3 # height of T on Silicon SiN loaded
H1_SIN_QZ             =                                 3 # height of T on Quartz SiN loaded
H1_RIDGE_SI           =                                 3 # height of T on Silicon Ridge
H1_RIDGE_QZ           =                                 3 # height of T on Quartz Ridge
BASE_THICK_SIN_SI     =                                20 # thickness of base of T for Nitride Loaded wg modulator on Si
BASE_THICK_SIN_QZ     =                                20 # thickness of base of T for Nitride Loaded wg modulator on Quartz
BASE_THICK_RIDGE_SI   =                                20 # thickness of base of T for Ridge wg modulator on Si
BASE_THICK_RIDGE_QZ   =                                20 # thickness of base of T for Ridge wg modulator on Quartz
GAP_SIN_SI            =                                 5 # gap between electrodes for Nitride Loaded WG on Silicon
GAP_SIN_QZ            =                                 5 # gap between electrodes for Nitride Loaded WG on Quartz
GAP_RIDGE_SI          =                                 5 # gap between electrodes for Ridge WG on Silicon
GAP_RIDGE_QZ          =                                 5 # gap between electrodes for Ridge WG on Quartz
D_SIN_SI              =                                45 # width of top of "T" on electrode for nitride on Silicon
D_SIN_QZ              =                                45 # width of top of "T" on electrode for nitride on Quartz
D_RIDGE_SI            =                                45 # width of top of "T" on electrode for ridge on Silicon
D_RIDGE_QZ            =                                45 # width of top of "T" on electrode for ridge on Quartz
R_SIN_SI              =                                 3 # thickness of top of "T" on electrode for nitride on Silicon
R_SIN_QZ              =                                 3 # thickness of top of "T" on electrode for nitride on Quartz
R_RIDGE_SI            =                                 3 # thickness of top of "T" on electrode for ridge on Silicon
R_RIDGE_QZ            =                                 3 # thickness of top of "T" on electrode for ridge on Quartz

