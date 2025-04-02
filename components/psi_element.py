import gdsfactory as gf
from enum import Enum

class Handle(Enum):
    """ Enumerable for substrate handle parameter in full device creation
        Using an enum to enforce use of supported handles """
    SILICON = "Silicon"
    QUARTZ = "Quartz"

class Waveguide(Enum):
    """ Enumerable for waveguide production path parameter in full device creation 
        Using an enum to enforce use of supported waveguide designs """
    SIN_STRIP = "SiN Strip-Loaded"
    RIDGE = "Ridge-Etched"

class PsiElement(gf.Component):
    def __init__(self, handle: Handle = Handle.SILICON, waveguide: Waveguide = Waveguide.SIN_STRIP):
        """ Abstract class for all psi pdk elements """
        super().__init__()