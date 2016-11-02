#!/usr/bin/env python

import numpy as np
from mayavi import mlab
import math
from tvtk.api import tvtk
from tvtk.common import configure_input_data, configure_input


class dirac_plots_3d:

    def __init__(self, mode, plot_type, data, mol=None, out=None):
        self.mode = mode
        self.pt   = plot_type
        self.data = data
        if mol != None:
            self.mol = mol
        if out != None:
            self.out = out


    def set_orientation_axes(self):
#           simple
            oa = mlab.orientation_axes(line_width = 1.0, opacity = 0.3)
            oa.axes.axis_labels = True



    def visualize_3d(self):

        if self.pt == '3d.isosurface':

            fig = mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))

#           density
            self.plot_pm_isosurface_3d()

#           molecule
            if self.mol:
                self.plot_atoms_3d(fig, self.mol[1], self.mol[2], self.mol[3], self.mol[4])

#           orientation axes
            self.set_orientation_axes()

        if self.mode == 'show':
            mlab.show()
        elif self.mode == 'save' and self.out:
#           unless you change DISPLAY=:1, the mayavi window will pop up for a second...
#           but fig will be saved correctly
            mlab.savefig(self.out)
            mlab.close(fig)



    def plot_pm_isosurface_3d(self):

        """ 
        change contours=[] for different isovalues
        """

        src = mlab.pipeline.scalar_field(self.data[0], self.data[1], self.data[2], self.data[3])

#       plus 
        mlab.pipeline.iso_surface(src, 
                                  contours=[0.01, ],
                                  color=(1.0,0.0,0.0), 
                                  opacity=0.3) 
#       minus
        mlab.pipeline.iso_surface(src, 
                                  contours=[-0.01, ],
                                  color=(0.0,1.0,1.0), 
                                  opacity=0.3) 



    def plot_atoms_3d(self, fig, a, x, y, z):
#       
#       !!! works on our molecules only !!!
#       todo: use some python libraries to draw any molecule

#       always in order: X, H, H, H, H, O
        sphere_radius = [0.3, 0.1, 0.1, 0.1, 0.1, 0.2]
        sphere_color  = [(0.0, 0.5, 0.5), (0.1, 0.1, 0.1), (0.1, 0.1, 0.1), (0.1, 0.1, 0.1), (0.1, 0.1, 0.1), (1.0, 0.0, 0.0)]

#       draw atoms
#       ----------
        atom = []
        for i in range(len(x)):
            sphere = tvtk.SphereSource(center=(x[i],y[i],z[i]), radius = sphere_radius[i], theta_resolution = 80, phi_resolution = 80)
            sphere_mapper = tvtk.PolyDataMapper()
            configure_input_data(sphere_mapper, sphere.output)
            sphere.update()
            p = tvtk.Property(opacity=0.8, color=sphere_color[i])
            sphere_actor = tvtk.Actor(mapper=sphere_mapper, property=p)
            fig.scene.add_actor(sphere_actor)
            atom.append(sphere_actor)

#       draw bonds
#       ----------
#       always in order: X, H, H, H, H, O
        pairs = [[0, 1], [0, 2], [5, 3], [5, 4]]
        bond = []
        for i in range(len(pairs)):
            p1 = (x[pairs[i][0]], y[pairs[i][0]], z[pairs[i][0]])
            p2 = (x[pairs[i][1]], y[pairs[i][1]], z[pairs[i][1]])
            line = tvtk.LineSource(point1=p1, point2=p2) 
            line_mapper = tvtk.PolyDataMapper()
            configure_input_data(line_mapper, line.output)
            line.update()
            tvtk.Property(opacity=0.8)
            line_actor = tvtk.Actor(mapper=line_mapper)
            line_actor.property.line_width = 1.9
            line_actor.property.color = (0.4, 0.4, 0.4)
            fig.scene.add_actor(line_actor)
            bond.append(line_actor)

 
