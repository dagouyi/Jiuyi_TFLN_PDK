""" Substrate generation for square samples """

import gdsfactory as gf
import config as cf

class Substrate(gf.Component):
    def LW_Alignment_Block(self) -> gf.Component:
        c= gf.Component("LW Alignment Block")
        rect1 = gf.components.rectangle(size= (20, 500), centered=True, layer=cf.ALIGNMENT_LAYER)
        rect2 = gf.components.rectangle(size= (500, 20), centered=True, layer=cf.ALIGNMENT_LAYER)
        outer_rect = gf.components.rectangle(size= (510, 510), centered=True, layer=cf.FILL_KEEPOUT_LAYER)
        c << rect1
        c << rect2
        c << outer_rect

        return c
    
    def EBPG_Alignment_Block(self) -> gf.Component:
        """ Global alignment marks for various etch steps """
        c = gf.Component("EBPG Alignment Block")
        vernier = gf.components.litho_ruler(height=11, width = 4, spacing = 8.2, 
                scale = [1, 1, 1, 1, 31/11, 1, 1, 1, 1, 31/11, 1, 1, 1, 1, 31/11, 1, 1, 1, 1, 
                        51/11, 1, 1, 1, 1, 31/11, 1, 1, 1, 1, 31/11, 1, 1, 1, 1, 31/11, 1, 1, 1, 1], num_marks = 39, layer = cf.ALIGNMENT_LAYER)
        outer_rect = gf.components.rectangle(size=(3480, 1376), centered = True, layer=cf.FILL_KEEPOUT_LAYER)
        v = c.add_ref(vernier)
        v.rotate(180)
        v.movex(315.6 / 2)
        v.movey(-1376/2 + 64)
        c.add_ref(outer_rect)

        alignment_mark = gf.Component("Alignment Mark")
        rec_ring = gf.components.rectangular_ring(enclosed_size = (496, 496), width = 4, layer=cf.ALIGNMENT_LAYER, centered=True)
        top_rec = gf.components.rectangle(size=(4, 280), layer=cf.ALIGNMENT_LAYER)
        right_rec = gf.components.rectangle(size=(280, 4), layer=cf.ALIGNMENT_LAYER, centered = True)
        alignment_mark.add_ref(rec_ring)
        a1 = alignment_mark.add_ref(top_rec)
        a1.movey(496/2 + 2); a1.movex(-2)
        a2 = alignment_mark.add_ref(right_rec)
        a2.movex(496/2 + 2 + 280 / 2)

        # central alignment bounding broken box ----------
        r1 = alignment_mark.add_ref(gf.components.rectangle(size=(45, 10), layer=cf.ALIGNMENT_LAYER))
        r1.movey(40); r1.movex(-50);
        r2 = alignment_mark.add_ref(gf.components.rectangle(size=(45, 10), layer=cf.ALIGNMENT_LAYER))
        r2.movey(40); r2.movex(5);
        r1 = alignment_mark.add_ref(gf.components.rectangle(size=(10, 45), layer=cf.ALIGNMENT_LAYER))
        r1.movey(5); r1.movex(-50);
        r2 = alignment_mark.add_ref(gf.components.rectangle(size=(10, 45), layer=cf.ALIGNMENT_LAYER))
        r2.movey(5); r2.movex(40);
    
        r1 = alignment_mark.add_ref(gf.components.rectangle(size=(45, 10), layer=cf.ALIGNMENT_LAYER))
        r1.movey(-50); r1.movex(-50);
        r2 = alignment_mark.add_ref(gf.components.rectangle(size=(45, 10), layer=cf.ALIGNMENT_LAYER))
        r2.movey(-50); r2.movex(5);
        r1 = alignment_mark.add_ref(gf.components.rectangle(size=(10, 45), layer=cf.ALIGNMENT_LAYER))
        r1.movey(-50); r1.movex(-50);
        r2 = alignment_mark.add_ref(gf.components.rectangle(size=(10, 45), layer=cf.ALIGNMENT_LAYER))
        r2.movey(-50); r2.movex(40);

        # -------------------------------------------------
        am1 = c.add_ref(alignment_mark)
        am2 = c.add_ref(alignment_mark)
        am2.movex(-1000)
        am3 = c.add_ref(alignment_mark)
        am3.movex(1000)

        ox_cross = gf.Component("Oxide Cross")
        r1 = ox_cross.add_ref(gf.components.rectangle(size=(10, 100), centered=True, layer=cf.OXIDE_ETCH_LAYER))
        r1.rotate(45)
        r2 = ox_cross.add_ref(gf.components.rectangle(size=(10, 100), centered=True, layer=cf.OXIDE_ETCH_LAYER))
        r2.rotate(-45)
        r1 = ox_cross.add_ref(gf.components.rectangle(size=(4, 220), centered=True, layer=cf.OXIDE_ETCH_LAYER))
        r1.movey(496/2 + 32 + 110)
        r2 = ox_cross.add_ref(gf.components.rectangle(size=(220, 4), centered=True, layer=cf.OXIDE_ETCH_LAYER))
        r2.movex(496/2 + 32 + 110)
        c.add_ref(ox_cross)

        au_cross = gf.Component("Gold Cross")
        r1 = au_cross.add_ref(gf.components.rectangle(size=(10, 100), centered=True, layer=cf.ELECTRODE_LAYER))
        r1.rotate(45)
        r1.movex(-1000)
        r2 = au_cross.add_ref(gf.components.rectangle(size=(10, 100), centered=True, layer=cf.ELECTRODE_LAYER))
        r2.rotate(-45)
        r2.movex(-1000)
        r1 = au_cross.add_ref(gf.components.rectangle(size=(4, 220), centered=True, layer=cf.ELECTRODE_LAYER))
        r1.movey(496/2 + 32 + 110); r1.movex(-1000)
        r2 = au_cross.add_ref(gf.components.rectangle(size=(220, 4), centered=True, layer=cf.ELECTRODE_LAYER))
        r2.movex(496/2 + 32 + 110 - 1000)
        c.add_ref(au_cross)

        nicr_cross = gf.Component("NiCr Cross")
        r1 = nicr_cross.add_ref(gf.components.rectangle(size=(10, 100), centered=True, layer=cf.HEATER_LAYER))
        r1.rotate(45)
        r1.movex(1000)
        r2 = nicr_cross.add_ref(gf.components.rectangle(size=(10, 100), centered=True, layer=cf.HEATER_LAYER))
        r2.rotate(-45)
        r2.movex(1000)
        r1 = nicr_cross.add_ref(gf.components.rectangle(size=(4, 220), centered=True, layer=cf.HEATER_LAYER))
        r1.movey(496/2 + 32 + 110); r1.movex(1000)
        r2 = nicr_cross.add_ref(gf.components.rectangle(size=(220, 4), centered=True, layer=cf.HEATER_LAYER))
        r2.movex(496/2 + 32 + 110 + 1000)
        c.add_ref(nicr_cross)

        block = gf.components.rectangle(size=(20,20), centered=True, layer=cf.ALIGNMENT_LAYER)
        b1 = c.add_ref(block); b1.movex(-578 - 20); b1.movey(450 - 20)
        b1 = c.add_ref(block); b1.movex(-578 - 20); b1.movey(-450 + 20)
        b1 = c.add_ref(block); b1.movex(-578 - 20 - 980); b1.movey(450 - 20)
        b1 = c.add_ref(block); b1.movex(-578 - 20 - 980); b1.movey(-450 + 20)
        b1 = c.add_ref(block); b1.movex(-578 - 20 + 980); b1.movey(450 - 20)
        b1 = c.add_ref(block); b1.movex(-578 - 20 + 980); b1.movey(-450 + 20)
        b1 = c.add_ref(block); b1.movex(-578 - 20 + 2*980); b1.movey(450 - 20)
        b1 = c.add_ref(block); b1.movex(-578 - 20 + 2*980); b1.movey(-450 + 20)

        return c
    
    def __init__(self, size = (35, 34)):
        super().__init__("{} x {} Substrate".format(size[0], size[1]))

        # add outer boundary -----------------------------------------------------------------------
        main = gf.components.rectangle((size[0] * 1000, size[1] * 1000), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True) # main substrate square
        main_outline = gf.components.rectangle((size[0] * 1000 + 25 * 2, size[1] * 1000 + 25 * 2), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True)
        outer = gf.components.rectangle((size[0] * 1000 + 150 * 2, size[1] * 1000 + 150 * 2), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True)
        outer_outline = gf.components.rectangle((size[0] * 1000 + 175 * 2, size[1] * 1000 + 175 * 2), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True)
        inner_inline = gf.components.rectangle((size[0] * 1000 - 150 * 2, size[1] * 1000 + 150 * 2), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True)
        inner_inline_2 = gf.components.rectangle((size[0] * 1000 - 125 * 2, size[1] * 1000 + 175 * 2), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True)
        inline_3 = gf.components.rectangle((size[0] * 1000 + 175 * 2, size[1] * 1000 - 125 * 2), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True)
        inline_4 = gf.components.rectangle((size[0] * 1000 + 150 * 2, size[1] * 1000 - 150 * 2), 
                                       layer=cf.WAFER_BOUNDARY_LAYER, centered = True)
        self.add_ref(main)
        self.add_ref(main_outline)
        self.add_ref(outer)
        self.add_ref(outer_outline)
        self.add_ref(inner_inline)
        self.add_ref(inner_inline_2)
        self.add_ref(inline_3)
        self.add_ref(inline_4)

        # add layer 99 marks -----------------------------------------------------------------------
        alignment_block = gf.components.rectangle((20, 20), layer=cf.ALIGNMENT_BOUNDARY_LAYER)
        a1 = self.add_ref(alignment_block); a2 = self.add_ref(alignment_block); a3 = self.add_ref(alignment_block);
        a4 = self.add_ref(alignment_block)
        a1.movex(-size[0] * 500 + 150 + 40); a2.movex(-size[0] * 500 + 150 + 40); a3.movex(size[0] * 500 - 150 - 60); a4.movex(size[0] * 500 - 150 - 60)
        a1.movey(-size[1] * 500 + 150 + 40); a2.movey(size[1] * 500 - 150 - 60);  a3.movey(size[1] * 500 - 150 - 60); a4.movey(-size[1] * 500 + 150 + 40)

        # add corner electrode pads -------------------------------------------------------------------
        e1 = self.add_ref(gf.components.ellipse(layer=cf.ELECTRODE_LAYER, radii=(4000, 4000)))
        e2 = self.add_ref(gf.components.ellipse(layer=cf.ELECTRODE_LAYER, radii=(4000, 4000)))
        e3 = self.add_ref(gf.components.ellipse(layer=cf.ELECTRODE_LAYER, radii=(4000, 4000)))
        e4 = self.add_ref(gf.components.ellipse(layer=cf.ELECTRODE_LAYER, radii=(4000, 4000)))
        e1.movex(-size[0] * 500); e1.movey(-size[1] * 500)
        e2.movex(-size[0] * 500); e2.movey(size[1] * 500)
        e3.movex(size[0] * 500); e3.movey(-size[1] * 500)
        e4.movex(size[0] * 500); e4.movey(size[1] * 500)
        b1 = gf.geometry.boolean(B = [e1, e2, e3, e4], A = main, operation='and', layer=cf.ELECTRODE_LAYER)
        self.remove([e1, e2, e3, e4])
        self.add_ref(b1)

        # add ebr region -------------------------------------------------------------------
        ebr = gf.components.rectangle((size[0] * 1000 - 500, size[1] * 1000 - 500), 
                                       layer=cf.EBR_LAYER, centered = True) 
        #ebr_inner_1 = gf.components.rectangle((size[0] * 1000 - 500 - 2250 * 2, size[1] * 1000 - 500 - 4754.365 * 2), 
        #                               layer=cf.EBR_LAYER, centered = True) 
        #ebr_inner_2 = gf.components.rectangle((size[0] * 1000 - 500 - 2250 * 2 - 4754.365 * 2, size[1] * 1000 - 500 - 1750 * 2), 
        #                               layer=cf.EBR_LAYER, centered = True) 
        ebr_inner_1 = gf.components.rectangle((size[0] * 1000 - 500 - 2250 * 2, size[1] * 1000 - 500 - 1750 * 2), 
                                       layer=cf.EBR_LAYER, centered = True) 
        
        #e1 = self.add_ref(gf.components.ellipse(layer=cf.EBR_LAYER, radii=(4754.365, 4754.365)))
        #e2 = self.add_ref(gf.components.ellipse(layer=cf.EBR_LAYER, radii=(4754.365, 4754.365)))
        #e3 = self.add_ref(gf.components.ellipse(layer=cf.EBR_LAYER, radii=(4754.365, 4754.365)))
        #e4 = self.add_ref(gf.components.ellipse(layer=cf.EBR_LAYER, radii=(4754.365, 4754.365)))
        #e1.movex(-size[0] * 500 + 2250 + 4754.365); e1.movey(-size[1] * 500 + 1750 + 4754.365)
        #e2.movex(-size[0] * 500 + 2250 + 4754.365); e2.movey(size[1] * 500 - 1750 - 4754.365)
        #e3.movex(size[0] * 500 - 2250 - 4754.365); e3.movey(-size[1] * 500 + 1750 + 4754.365)
        #e4.movex(size[0] * 500 - 2250 - 4754.365); e4.movey(size[1] * 500 - 1750 - 4754.365)
        b1 = gf.geometry.boolean(A = [ebr], B = [ebr_inner_1], operation='A-B', layer=cf.EBR_LAYER)
        #b2 = gf.geometry.boolean(B = [b1], A = [e1, e2, e3,e4], operation='or', layer=cf.EBR_LAYER)
        #self.remove([e1, e2, e3, e4])
        self.add_ref(b1)
        #self.add_ref(b2)

        # --------------------------------------------- Alignment Blocks Laser Write and EBL ------------------------------ #
        lw1 = self.add_ref(self.LW_Alignment_Block())
        lw2 = self.add_ref(self.LW_Alignment_Block())
        lw3 = self.add_ref(self.LW_Alignment_Block())
        lw4 = self.add_ref(self.LW_Alignment_Block())
        lw1.move(destination=(-12500, 13500))
        lw2.move(destination=(12500, 13500))
        lw3.move(destination=(12500, -13500))
        lw4.move(destination=(-12500, -13500))

        ebl_1 = self.add_ref(self.EBPG_Alignment_Block())

        # TODO: make these movements more accurate to size of rectangle, substrate
        ebl_1.movex(-size[0] * 500 + 5795 + 3480 / 2); ebl_1.movey(-size[1] * 500 + 2834 + 1376 / 2)
