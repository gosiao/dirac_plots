#!/usr/bin/env python

import numpy as np
from mayavi import mlab
#import mayavi.mlab as plt

from tvtk.api import tvtk
from tvtk.common import configure_input_data, configure_input


 
class molecule_3d:

    def __init__(self, p):
        self.p = p

    def plot_atoms_3d(self, fig, a_name, a_nr, x, y, z):
#       plot all atoms:
#       ---------------
#       first prepare the radius of a sphere depending on the atomic number
        sphere_radius = []
        sphere_color  = []
#       specific size and color for every element
#       always in order: X, H, H, H, H, O
        sphere_radius = [0.6, 0.2, 0.2, 0.2, 0.2, 0.4]
        sphere_color  = [(1.0, 1.0, 0.0), (0.8, 0.8, 0.8), (0.8, 0.8, 0.8), (0.8, 0.8, 0.8), (0.8, 0.8, 0.8), (1.0, 0.0, 0.0)]
        #for i in range(118):
        #    sphere_radius.append(0.05*np.sqrt(i))
        #    r = (118-i)/118.0
        #    g = i/118.0
        #    b = i/118.0
        #    sphere_color.append((r, g, b))
        atom = []
        for i in range(len(a_name)):
            print 'bubai, radius = ', i, a_nr[i], sphere_radius[i]
            #sphere = tvtk.SphereSource(center=(x[i], y[i], z[i]), radius = sphere_radius[a_nr[i]])
            sphere = tvtk.SphereSource(center=(x[i], y[i], z[i]), radius = sphere_radius[i], theta_resolution = 80, phi_resolution = 80)
            sphere_mapper = tvtk.PolyDataMapper()
            configure_input_data(sphere_mapper, sphere.output)
            sphere.update()
            #p = tvtk.Property(opacity=0.8, color=sphere_color[a_nr[i]])
            p = tvtk.Property(opacity=0.8, color=sphere_color[i])
            sphere_actor = tvtk.Actor(mapper=sphere_mapper, property=p)
            fig.scene.add_actor(sphere_actor)
            #sphere_actor.position = np.array([-10.0, -2.0, 5.0])
            atom.append(sphere_actor)
#       connectivity:
#       -------------
#       always in order: X, H, H, H, H, O
        pairs = [[0, 1], [0, 2], [5, 3], [5, 4]]
        bond = []
        for i in range(len(pairs)):
            p1 = (x[pairs[i][0]], y[pairs[i][0]], z[pairs[i][0]])
            p2 = (x[pairs[i][1]], y[pairs[i][1]], z[pairs[i][1]])
            line = tvtk.LineSource(point1=p1, point2=p2) 
            #line_mapper = tvtk.PolyDataMapper()
            tube = tvtk.TubeFilter(radius=5.0, number_of_sides=10, input=line)
            tube_mapper = tvtk.PolyDataMapper()
            #configure_input(add_filter, line)
            #configure_input_data(line_mapper, line.output)
            configure_input_data(tube_mapper, tube.output)
            #line.update()
            tube.update()
            tvtk.Property(opacity=0.8, color=(1.0, 1.0, 0.2))
            #line_actor = tvtk.Actor(mapper=line_mapper)
            tube_actor = tvtk.Actor(mapper=tube_mapper)
            #fig.scene.add_actor(line_actor)
            fig.scene.add_actor(tube_actor)
            #bond.append(line_actor)
            bond.append(tube_actor)
        return atom, bond
            

#
##.......prepare data
#        an = np.array(n)
#        ax = np.array(x)
#        ay = np.array(y)
#        az = np.array(z)
#        ar = np.array(r)
##.......plot atoms as 3d points, vary size and color (order of atoms from *cube files):
##       X
#        f = 0.6
#        c = (1.0, 1.0, 0.0)
#        p1 = self.p.points3d(ax[0], ay[0], az[0], ar[0],
#                        scale_factor=f,
#                        resolution=80,
#                        color=c,
#                        scale_mode='none')
##       O
#        f = 0.4
#        c = (1.0, 0.0, 0.0)
#        p1 = self.p.points3d(ax[5], ay[5], az[5], ar[5],
#                        scale_factor=f,
#                        resolution=80,
#                        color=c,
#                        scale_mode='none')
##       H
#        f = 0.2
#        c = (0.8, 0.8, 0.8)
#        p1 = self.p.points3d(ax[1:5], ay[1:5], az[1:5], ar[1:5],
#                        scale_factor=f,
#                        resolution=80,
#                        color=c,
#                        scale_mode='none')
##.......plot bonds (order of atoms from *cube files)
##       h2x
#        p1 = self.p.plot3d([ax[0],ax[1]], [ay[0],ay[1]], [az[0],az[1]], tube_radius=0.02, colormap='Oranges')
#        p1 = self.p.plot3d([ax[0],ax[2]], [ay[0],ay[2]], [az[0],az[2]], tube_radius=0.02, colormap='Oranges')
##       h2o
#        p1 = self.p.plot3d([ax[5],ax[3]], [ay[5],ay[3]], [az[5],az[3]], tube_radius=0.02, colormap='Oranges')
#        p1 = self.p.plot3d([ax[5],ax[4]], [ay[5],ay[4]], [az[5],az[4]], tube_radius=0.02, colormap='Oranges')
##.......plot atom names
##        xoff = 0.05*(max(x)-min(x))
##        yoff = 0.05*(max(y)-min(y))
##        zoff = 0.05*(max(z)-min(z))
##        nx = []
##        ny = []
##        nz = []
##        for i in range(len(x)):
##            nx.append(x[i]+xoff)
##            ny.append(y[i]+yoff)
##            nz.append(z[i]+zoff)
##        for i, a in enumerate(nx):
##            self.p.text3d(nx[i], ny[i], nz[i], n[i], scale=(0.2, 0.2, 0.2), color=(0.2, 0.2, 0.2))
#        return p1
#

    def plot_atoms_3d_3mol(self, n1, r1, x1, y1, z1, n2, r2, x2, y2, z2, n3, r3, x3, y3, z3):
        fig1 = mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
#       mol1:
        fig1_extent = (-10.0, -4.0, 2.0, 14.0, 0.0, 6.0)
        fig1_shift = [-6.0, 8.0, 3.0]
        p1, b1 = self.plot_atoms_3d(fig1, n1, r1, x1, y1, z1)
        for p in p1:
            p.position = np.array(fig1_shift)
        for b in b1:
            b.position = np.array(fig1_shift)
            #p.update()
        #p2 = p1.parent.parent
        #p1 = mayavi.tools.pipeline.image_actor(extent=fig1_extent)
        #p1.actor.position = [-6.0, ]
        #p1.actor.scale = []
#       mol2:
        fig2_extent = (-2.0, 4.0, -6.0, 6.0, 0.0, 6.0)
        fig2_shift = (-2.0, 4.0, -6.0, 6.0, 0.0, 6.0)
        #self.plot_atoms_3d(n2, r2, x2, y2, z2)
        #self.plot_atoms_3d(n2, r2, x2, y2, z2, fig_extent=fig2_extent)
#       mol3:
        fig3_extent = (6.0, 12.0, -14.0, -2.0, 0.0, 6.0)
        fig3_shift = (6.0, 12.0, -14.0, -2.0, 0.0, 6.0)
        #self.plot_atoms_3d(n3, r3, x3, y3, z3)
        #self.plot_atoms_3d(n3, r3, x3, y3, z3, fig_extent=fig3_extent)

 
# v = mlab.figure()
# 
# # Create a first sphere
# # The source generates data points
# sphere = tvtk.SphereSource(center=(0, 0, 0), radius=0.5)
# # The mapper converts them into position in, 3D with optionally color (if
# # scalar information is available).
# sphere_mapper = tvtk.PolyDataMapper()
# configure_input_data(sphere_mapper, sphere.output)
# sphere.update()
# 
# # The Property will give the parameters of the material.
# p = tvtk.Property(opacity=0.2, color=(1, 0, 0))
# # The actor is the actually object in the scene.
# sphere_actor = tvtk.Actor(mapper=sphere_mapper, property=p)
# v.scene.add_actor(sphere_actor)
# 
# sphere_actor.position = np.array([-10.0, -2.0, 5.0])
# 
# # Create a second sphere
# sphere2 = tvtk.SphereSource(center=(7, 0, 1), radius=0.2)
# sphere_mapper2 = tvtk.PolyDataMapper()
# configure_input_data(sphere_mapper2, sphere2.output)
# sphere2.update()
# p = tvtk.Property(opacity=0.3, color=(1, 0, 0))
# sphere_actor2 = tvtk.Actor(mapper=sphere_mapper2, property=p)
# v.scene.add_actor(sphere_actor2)
# 
# sphere_actor2.position = np.array([-10.0, -2.0, 5.0])
# 
# # Create a line between the two spheres
# line = tvtk.LineSource(point1=(0, 0, 0), point2=(7, 0, 1))
# line_mapper = tvtk.PolyDataMapper()
# configure_input_data(line_mapper, line.output)
# line.update()
# line_actor = tvtk.Actor(mapper=line_mapper)
# v.scene.add_actor(line_actor)
# 
# line_actor.position = np.array([-10.0, -2.0, 5.0])
# 
# # And display text
# vtext = tvtk.VectorText()
# vtext.text = 'Mayavi'
# text_mapper = tvtk.PolyDataMapper()
# configure_input_data(text_mapper, vtext.get_output())
# vtext.update()
# p2 = tvtk.Property(color=(0, 0.3, 0.3))
# text_actor = tvtk.Follower(mapper=text_mapper, property=p2)
# text_actor.position = (0, 0, 0)
# v.scene.add_actor(text_actor)
# 
# # Choose a view angle, and display the figure
# mlab.view(85, -17, 15, [3.5, -0.3, -0.8])
# mlab.show()
# 
# 




