import numpy as np
import gdsfactory as gf
from functools import partial
from shapely.geometry.polygon import Polygon

class StarCoupler(gf.Component):
    def __init__(self, NRadius: float = 8, Nin: int = 12, Nout: int = 12, min_line: float = 0.5, min_space: float = 0.5, win: float = 1, wout: float = 2, 
                 w: float = 1, slab_width: float = 100, taper_ratio: float = 25, npts_arc: int = 256, neff__slab: float = 2.2, lamc: float = 1550e-3, 
                 sc_layer: int = 2, Rbend: float = 200, input_sepX: float = 200, input_sepY: float = 120, output_sepX: float = 127, output_sepY: float = 20, 
                 pop_all_wg: int = 0):
        super().__init__("Star Coupler")

        buffer_length = 1

        pitch = np.max([win, wout]) + min_space
        #print(pitch)

        taper_length = taper_ratio * (np.max([win, wout]) - w)

        term_taper_length = taper_ratio * (w - min_line)

        R = (NRadius) * pitch / (2 * np.arcsin(lamc / 2 / neff__slab / pitch))
        #print(R)
        R = np.round(R, 7)

        Rin = R
        Rout = R / 2

        if pop_all_wg:
            Nindex_in = np.round(np.linspace(1,Nin) - (Nin + 1) / 2)
            Nindex_out = np.round(np.linspace(1, Nout) - (Nout + 1) / 2)
            Nindex_in_y = np.abs(np.abs(Nindex_in) - np.max(np.abs(Nindex_in)))
            Nindex_out_y = np.abs(np.abs(Nindex_out) - np.max(np.abs(Nindex_out)))

            if np.remainder(Nin, 2) == 0:
                Nindex_in_x = np.abs(Nindex_in) - 1
            else:
                Nindex_in_x = np.abs(Nindex_in)
            if np.remainder(Nout, 2) == 0:
                Nindex_out_x = np.abs(Nindex_out) - 1
            else:
                Nindex_out_x = np.abs(Nindex_out)

            wg_in_dirX = np.array(np.ones((1, np.floor(Nin / 2))) - 1 * np.ones((1, np.ceil(Nin / 2))))
            wg_out_dirX = np.array(np.ones((1, np.floor(Nout / 2))) - 1 * np.ones((1, np.ceil(Nout / 2))))

        else:
            if np.remainder(NRadius,2) == 0 and np.remainder(Nin, 2) != 0:
                Nindex_in = np.round(np.linspace(1, NRadius - 1) - ((NRadius - 1) + 1) / 2)
            else:
                Nindex_in = np.round(np.linspace(1, NRadius) - (NRadius + 1) / 2)
            if np.remainder(NRadius,2) == 0 and np.remainder(Nout, 2) != 0:
                Nindex_out = np.round(np.linspace(1, NRadius - 1) - ((NRadius - 1) + 1) / 2)
            else:
                Nindex_out = np.round(np.linspace(1, NRadius) - (NRadius + 1) / 2)

            Nindex_in_y = np.abs(np.abs(Nindex_in) - np.max(np.abs(Nindex_in)))
            Nindex_out_y = np.abs(np.abs(Nindex_out) - np.max(np.abs(Nindex_out)))

            if np.remainder(Nin, 2) == 0:
                Nindex_in_x = np.abs(Nindex_in) - 1
            else:
                Nindex_in_x = np.abs(Nindex_in)
            if np.remainder(Nout, 2) == 0:
                Nindex_out_x = np.abs(Nindex_out) - 1
            else:
                Nindex_out_x = np.abs(Nindex_out)

            wg_in_dirX = np.array(np.ones(1, np.floor(Nin / 2)) - np.ones(1, np.ceil(Nin / 2)))
            wg_out_dirX = np.array(np.ones(1, np.floor(Nout / 2)) - np.ones(1, np.ceil(Nout / 2)))

        input_thetas = -(pitch * (np.linspace(1, Nin) - (Nin + 1) / 2) / Rin)
        output_thetas = -pitch * (np.linspace(1, Nout) - (Nout + 1) / 2) / Rin

        output_thetas_pos = -pitch * (np.linspace(1, Nout) - (Nout + 1) / 2) / Rout

        input_theta_start = 3 * np.pi / 2 + input_thetas[0] + pitch / Rin
        input_theta_stop = 3 * np.pi / 2 + input_thetas[-1] - pitch / Rin
        input_theta_arc = np.linspace(input_theta_start, input_theta_stop, npts_arc)
        #print(input_theta_arc)

        output_theta_start = np.pi / 2 + output_thetas_pos[0] + pitch / Rout
        output_theta_stop = np.pi / 2 + output_thetas_pos[-1] - pitch / Rout
        output_theta_arc = np.linspace(output_theta_start, output_theta_stop, npts_arc)

        ####################################################################################
        # Free propagation region of star coupler
        ####################################################################################

        # central polygon
        x = [Rout*np.cos(output_theta_arc[-1]), Rin*np.cos(input_theta_arc[0]) + 0.25*np.sin(input_theta_arc[0]+np.pi/2),
             Rin*np.cos(input_theta_arc[-1]) - 0.25*np.cos(input_theta_arc[-1]+np.pi/2), Rout*np.cos(output_theta_arc[0])]
        y = [Rout*np.sin(output_theta_arc[0]), Rin*np.sin(input_theta_arc[-1])+Rin/2 + 0.25*np.sin(input_theta_arc[-1]-np.pi/2),
             Rin*np.sin(input_theta_arc[-1])+Rin/2 + 0.25*np.sin(input_theta_arc[-1]-np.pi/2), Rout*np.sin(output_theta_arc[0])]

        #print(x)
        #print(y)

        self.add_polygon((x, y), layer=(sc_layer, 0))

        # input arc
        x = Rin * np.cos(input_theta_arc)
        y = Rin * np.sin(input_theta_arc)
        #y /= 2
        self.add_polygon((x, y), layer=(sc_layer, 0))

        # output arc
        x = Rout * np.cos(output_theta_arc)
        y = Rout * np.sin(output_theta_arc)
        self.add_polygon((x, y), layer=(sc_layer, 0))

        Xc = 0
        Yc = Rin / 2
        phirot = 0; xnew = x * np.cos(phirot) - y * np.sin(phirot); ynew = x * np.sin(phirot) + y * np.cos(phirot)
        xnew += Xc; ynew += Yc

        # left slab absorber
        x = [Rin*np.cos(input_theta_arc[-1]) - 0.25*np.cos(input_theta_arc[-1]+np.pi/2),
        (Rin+2*taper_length)*np.cos(input_theta_arc[-1]) - 0.25*np.cos(input_theta_arc[-1]+np.pi/2),
        (Rin+2*taper_length)*np.cos(input_theta_arc[-1])-slab_width + 0.25,
        (Rin+2*taper_length)*np.cos(input_theta_arc[-1])-slab_width + 0.25,
        Rout*np.cos(output_theta_arc[0]) + 2*taper_length*np.cos(np.pi/2 + output_thetas[0] + pitch/Rout/2) - 0.25*np.cos(output_theta_arc[0]-np.pi/2),
        Rout*np.cos(output_theta_arc[0])]

        y = [Rin*np.sin(input_theta_arc[-1])+Rin/2 + 0.25*np.sin(input_theta_arc[-1]-np.pi/2),
            (Rin+2*taper_length)*np.sin(input_theta_arc[-1]) + Rin/2 + 0.25,
            (Rin+2*taper_length)*np.sin(input_theta_arc[-1]) + Rin/2 + 0.25,
            Rout*np.sin(output_theta_arc[0]) + 2*taper_length*np.sin(np.pi/2 + output_thetas[0] + pitch/Rout/2) - 0.25,
            Rout*np.sin(output_theta_arc[0]) + 2*taper_length*np.sin(np.pi/2 + output_thetas[0] + pitch/Rout/2) - 0.25,
            Rout*np.sin(output_theta_arc[0])]
        
        #print(x)
        #print(y)
        
        
        self.add_polygon((x, y), layer=(sc_layer, 0))

        # Left slab extension
        if slab_width:
            x = [(Rin+2*taper_length)*np.cos(input_theta_arc[-1]),
            (Rin+2*taper_length)*np.cos(input_theta_arc[-1])-slab_width,
            (Rin+2*taper_length)*np.cos(input_theta_arc[-1])-slab_width,
            Rout*np.cos(output_theta_arc[0]) + 2*taper_length*np.cos(np.pi/2 + output_thetas[0] + pitch/Rout/2)]
            y = [(Rin+2*taper_length)*np.sin(input_theta_arc[-1]) + Rin/2,
            (Rin+2*taper_length)*np.sin(input_theta_arc[-1]) + Rin/2,
            Rout*np.sin(output_theta_arc[-1]) + 2*taper_length*np.sin(np.pi/2 + output_thetas[0] + pitch/Rout/2),
            Rout*np.sin(output_theta_arc[0]) + 2*taper_length*np.sin(np.pi/2 + output_thetas[0] + pitch/Rout/2)]
        
            self.add_polygon((x, y), layer=(sc_layer, 0))

        # right slab absorber
        x = [Rout*np.cos(output_theta_arc[-1]),
        Rout*np.cos(output_theta_arc[-1]) + 2*taper_length*np.cos(np.pi/2 + output_thetas[-1] - pitch/Rout/2) + 0.25*np.cos(output_theta_arc[-1]-np.pi/2),
        (Rin+2*taper_length)*np.cos(input_theta_arc[0])+slab_width - 0.25,
        (Rin+2*taper_length)*np.cos(input_theta_arc[0])+slab_width - 0.25,
        (Rin+2*taper_length)*np.cos(input_theta_arc[0]) + 0.25*np.cos(input_theta_arc[0]+np.pi/2),
        Rin*np.cos(input_theta_arc[0]) + 0.25*np.sin(input_theta_arc[0]+np.pi/2)]

        y = [Rout*np.sin(output_theta_arc[-1]),
            Rout*np.sin(output_theta_arc[-1]) + 2*taper_length*np.sin(np.pi/2 + output_thetas[-1] - pitch/Rout/2) - 0.25,
            Rout*np.sin(output_theta_arc[-1]) + 2*taper_length*np.sin(np.pi/2 + output_thetas[-1] - pitch/Rout/2) - 0.25,
            (Rin+2*taper_length)*np.sin(input_theta_arc[0]) + Rin/2 + 0.25,
            (Rin+2*taper_length)*np.sin(input_theta_arc[0]) + Rin/2 + 0.25,
            Rin*np.sin(input_theta_arc[0])+Rin/2 + 0.25*np.sin(input_theta_arc[0]+np.pi/2)]
        
        self.add_polygon((x, y), layer=(sc_layer, 0))



        ####################################################################################
        # Waveguides and tapers
        ####################################################################################

        # define general taper shape
        tap = gf.components.taper(taper_length, 1, 0.5)
        
        wgnums = np.linspace(0, np.max([Nin, Nout]) - 1)

        for wgnum in wgnums:
            wgnum = int(wgnum)
            if wgnum <= Nin:
                print(wgnum)
                x = [-win/2, -w/2, -w/2, -min_line/2,
                    min_line/2, w/2, w/2, win/2]
                y = [0.2, -taper_length, -taper_length-buffer_length,
                    -taper_length-buffer_length-term_taper_length,
                    -taper_length-buffer_length-term_taper_length,
                    -taper_length-buffer_length, -taper_length, 0.2];
                Xc = Rin*np.cos(3*np.pi/2+input_thetas[wgnum]);
                Yc = Rin*np.sin(3*np.pi/2+input_thetas[wgnum]) + Rin/2;
                phirot = input_thetas[wgnum];
                xnew = []; ynew = []
                for i in range(len(x)):
                    temp_x = x[i] * np.cos(phirot) - y[i] * np.sin(phirot)
                    temp_x += Xc
                    xnew.append(temp_x)
                    temp_y = x[i] * np.sin(phirot) + y[i] * np.cos(phirot)
                    temp_y += Yc
                    ynew.append(temp_y)

                self.add_polygon((xnew, ynew), layer=(sc_layer, 0))

            if wgnum <= Nout:
                x = [-wout/2, -w/2, -w/2, -min_line/2,
                    min_line/2, w/2, w/2, wout/2]
                y = [-0.22, taper_length, taper_length+buffer_length,
                    taper_length+buffer_length+term_taper_length,
                    taper_length+buffer_length+term_taper_length,
                    taper_length+buffer_length, taper_length, -0.22];
                Xc = Rout*np.cos(np.pi/2+output_thetas_pos[wgnum]);
                Yc = Rout*np.sin(np.pi/2+output_thetas_pos[wgnum]);
                phirot = output_thetas[wgnum];
                for i in range(len(x)):
                    temp_x = x[i] * np.cos(phirot) - y[i] * np.sin(phirot)
                    temp_x += Xc
                    xnew.append(temp_x)
                    temp_y = x[i] * np.sin(phirot) + y[i] * np.cos(phirot)
                    temp_y += Yc
                    ynew.append(temp_y)

                self.add_polygon((xnew, ynew), layer=(sc_layer, 0))
        
        #self.add_array(tap, columns=2, rows=2, spacing=(100, 100))

        
