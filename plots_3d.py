#!/usr/bin/env python

#   gosia, last revision: 03/04/2016   


import numpy as np
import mayavi.mlab as plt
import math

#try:
#    engine = mayavi.engine
#except NameError:
#    from mayavi.api import Engine
#    engine = Engine()
#    engine.start()
#if len(engine.scenes) == 0:
#    engine.new_scene()


# local:
from dirac_data import *


#functions:

def proj(x, y, z, u, v, w, d, p):
    if d == 'x':
        proj = []
        l1 = math.ceil(p)
        l2 = math.floor(p)
        nw = (w[l1] - w[l2])/2.0
        for i in range(len(x)):
            proj.append(np.sqrt(u[i]*u[i] + v[i]*v[i] + nw*nw))
        return proj

class dirac_plots_3d:
    def __init__(self, p):
        self.p = p
        self.p.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
#       orientation axes:
        oa = self.p.orientation_axes(line_width = 1.0, opacity = 0.3)
## ------------------------------------------- 
#        orientation_axes = engine.scenes[0].children[4].children[0].children[0].children[0].children[1]
        oa.axes.origin = np.array([ 0.,  0.,  0.])
        oa.axes.normalized_tip_length = np.array([ 0.4,  0.4,  0.4])
        oa.axes.total_length = np.array([ 1.,  1.,  1.])
        oa.axes.render_time_multiplier = 0.6318196001233577
        oa.axes.orientation = np.array([ 0., -0.,  0.])
        oa.axes.scale = np.array([ 1.,  1.,  1.])
        oa.axes.normalized_shaft_length = np.array([ 0.6,  0.6,  0.6])
        oa.axes.normalized_label_position = np.array([ 2.3,  1. ,  1. ])
        oa.axes.reference_count = 3
        oa.axes.position = np.array([ 0.,  0.,  0.])
        oa.axes.normalized_label_position = np.array([ 2.3,  1. ,  1. ])
        oa.axes.origin = np.array([ 0.,  0.,  0.])
        oa.axes.normalized_tip_length = np.array([ 0.4,  0.4,  0.4])
        oa.axes.total_length = np.array([ 1.,  1.,  1.])
        oa.axes.orientation = np.array([ 0., -0.,  0.])
        oa.axes.scale = np.array([ 1.,  1.,  1.])
        oa.axes.normalized_shaft_length = np.array([ 0.6,  0.6,  0.6])
        oa.axes.normalized_label_position = np.array([ 2.3,  2. ,  1. ])
        oa.axes.position = np.array([ 0.,  0.,  0.])
        oa.axes.normalized_label_position = np.array([ 2.3,  2. ,  1. ])
        oa.axes.origin = np.array([ 0.,  0.,  0.])
        oa.axes.normalized_tip_length = np.array([ 0.4,  0.4,  0.4])
        oa.axes.total_length = np.array([ 1.,  1.,  1.])
        oa.axes.orientation = np.array([ 0., -0.,  0.])
        oa.axes.scale = np.array([ 1.,  1.,  1.])
        oa.axes.normalized_shaft_length = np.array([ 0.6,  0.6,  0.6])
        oa.axes.normalized_label_position = np.array([ 2.3,  2. ,  2. ])
        oa.axes.position = np.array([ 0.,  0.,  0.])
        oa.axes.normalized_label_position = np.array([ 2.3,  2. ,  2. ])
## ------------------------------------------- 


    def plot_contour3d(self,x,y,z,s):
        self.p.points3d(0, 0, 0)
        self.p.figure(1, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
        self.p.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
        self.p.contour3d(xx, yy, zz, ss, contours=[0.1], opacity=0.5)
    
    
    def plot_isosurface_3d(self, x, y, z, s):
        #current_palette = sns.color_palette()
        #sns.palplot(current_palette)
        #cmap = sns.cubehelix_palette(light=1, as_cmap=True)
#
        plt.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
        self.p.orientation_axes(line_width = 1.0, opacity = 0.3)
#
        #sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
#       -------------
        src = self.p.pipeline.scalar_field(x, y, z, s)
        self.p.pipeline.iso_surface(src, color=(1.0,0.0,0.0), contours=[0.01, ], opacity=0.3) 
        self.p.pipeline.iso_surface(src, color=(0.0,1.0,1.0),contours=[-0.01, ], opacity=0.3) 
#
        #self.p.pipeline.volume(src)
        #self.p.pipeline.image_plane_widget(src,
        #                    opacity = 0.1,
        #                    plane_orientation='y_axes',
        #                    slice_index=1,
        #                )


    def plot_streamlines_3d(self, x, y, z, u, v, w):
        current_palette = sns.color_palette()
        sns.palplot(current_palette)
        cmap = sns.cubehelix_palette(light=1, as_cmap=True)
#
        plt.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
#
        sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
#       -------------
        src = self.p.pipeline.vector_field(x, y, z, u, v, w)
        #fig=self.p.pipeline.streamline(src, seedtype='plane', seed_scale=2.0) 
        #fig=self.p.quiver3d(x, y, z, u, v, w)
        #self.p.pipeline.vectors(src, scale_factor=3.)
        #self.p.pipeline.vector_cut_plane(src, scale_factor=3)
        magnitude = self.p.pipeline.extract_vector_norm(src)
        self.p.pipeline.iso_surface(magnitude, contours=[1.0, 0.1], colormap="Pastel1")
        #flow = self.p.flow(u, v, w, seed_scale=1,
        #                   seed_resolution=5,
        #                   integration_direction='both')

    def plot_3d_test(self, x, y, z, u, v, w, vx, vy, vz, vu, vv, vw):
        f = proj(x, y, z, u, v, w, 'x', 0.0)
        self.p.surf(vx, vy, vz, colormap='Spectral')

    def plot_streamlines_2d(self, x, y, u, v):
        fig = plt.figure()
        #ax = fig.add_subplot(111)
        #dp = plots_2d(plt, [min(y), max(y)], [min(x), max(x)])
#       -------------------------------------------------------
        stream_color   = 'k'
        stream_density = 2.5
        #stream_cmap    = self.p.cm.bwr
#.......and plot:
#       ---------
        ps = self.p.streamplot(x, y, u, v,
                          color   = stream_color,
                          density = stream_density)
                          #cmap    = stream_cmap)



## prepare data
## ------------
#
#f = open('plot.3d.scalar', 'r')
#x, y, z, s = numpy.loadtxt(f, unpack=True)
#f.close()
#
## 1d to 3d arrays:
#dd = dirac_data('3d.scalar')
#len1, xx, yy, zz = dd.make_1d_to_3d_xyz(x, y, z)
#ss = numpy.array(s).reshape(len1, len1, len1)
#
#sns.set(style="dark")
#current_palette = sns.color_palette()
#sns.palplot(current_palette)
#cmap = sns.cubehelix_palette(light=1, as_cmap=True)
#
#plt.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
#
##sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
#plot_isosurface(plt, xx, yy, zz, ss)
#
#plt.colorbar(title='Shielding density', orientation='vertical')
#
##sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
##plot_contour3d(plt, xx, yy, zz, ss)
#
#
#plt.show()

