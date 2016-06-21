#!/usr/bin/env python

#   gosia, last revision: 05/06/2016

import numpy as np
import mayavi.mlab as plt
import matplotlib

def project(x, y, z):
    for i in range(len(x)):
#       points on a plane
        o = [-8.0, -8.0, 0.0]
        r = [ 8.0, -8.0, 0.0]
        t = [-8.0, 16.0, 0.0]
#       diff
        a = [r[0]-o[0], r[1]-o[1], r[2]-o[2]]
        b = [t[0]-o[0], t[1]-o[1], t[2]-o[2]]
#       c = a x b
        c =  [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]
        print "a, b = ", a, b
#       norm
        na = np.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
        nb = np.sqrt(b[0]*b[0] + b[1]*b[1] + b[2]*b[2])
        nc = np.sqrt(c[0]*c[0] + c[1]*c[1] + c[2]*c[2])
#       normalize all
        a = a/na
        b = b/nb
        c = c/nc
#       finally
        x[i] = x[i] - (a[0]*x[i] + a[1]*y[i] + a[2]*z[i])
        y[i] = y[i] - (b[0]*x[i] + b[1]*y[i] + b[2]*z[i])
        
 
class molecule:

    def __init__(self, p):
        self.p = p

           

    def plot_atoms_2d(self, n, x, y, z, p1x, p1y, p2x, p2y, p3x, p3y):
#.......play with these settings to get the nicest atoms
#       ------------------------------------------------
        atom_font = matplotlib.font_manager.FontProperties(weight='extra bold', size=14)
        atom_label_xoff = 0.01*(max(x) - min(x))
        atom_label_yoff = 0.01*(max(y) - min(y))
        atom_style = 'or'
#.......and plot:
#       ---------
        n_in_range = ['Po', 'Hb', 'H']
        x_in_range = [-0.004448, 0.436982, 3.281067]
        y_in_range = [-0.150403, 3.125443, -0.579443]
        z_in_range = [0.001037, -0.181733, 0.052432]
        print "buba before, x = ", x_in_range
        print "buba before, y = ", y_in_range
        print "buba before, z = ", z_in_range
        project(x_in_range, y_in_range, z_in_range)
        print "buba after , x = ", x_in_range
        print "buba after , y = ", y_in_range
        print "buba after , z = ", z_in_range
        for i, a in enumerate(n_in_range):
#            f = 1.8897
            f = 1.0
            x_in_range[i] = x_in_range[i]*f
            y_in_range[i] = y_in_range[i]*f
# remember that x <-> y
            pa = self.p.plot(y_in_range[i], x_in_range[i], atom_style)
            self.p.annotate(a,
                       xy = (y_in_range[i], x_in_range[i]),
                       xytext = (y_in_range[i]+atom_label_yoff, x_in_range[i]+atom_label_xoff),
                       fontproperties = atom_font)
        return pa


    def plot_atoms_3d(self, n, r, x, y, z, fig_extent=None):
#.......prepare data
        an = np.array(n)
        ax = np.array(x)
        ay = np.array(y)
        az = np.array(z)
        ar = np.array(r)
#.......plot atoms as 3d points, vary size and color (order of atoms from *cube files):
        if fig_extent:
#           X
            f = 0.6
            c = (1.0, 1.0, 0.0)
            self.p.points3d(ax[0], ay[0], az[0], ar[0],
                            scale_factor=f,
                            resolution=80,
                            color=c,
                            scale_mode='none',
                            extent=fig_extent)
#           O
            f = 0.4
            c = (1.0, 0.0, 0.0)
            self.p.points3d(ax[5], ay[5], az[5], ar[5],
                            scale_factor=f,
                            resolution=80,
                            color=c,
                            scale_mode='none',
                            extent=fig_extent)
#           H
            f = 0.2
            c = (0.8, 0.8, 0.8)
            self.p.points3d(ax[1:5], ay[1:5], az[1:5], ar[1:5],
                            scale_factor=f,
                            resolution=80,
                            color=c,
                            scale_mode='none',
                            extent=fig_extent)
#...........plot bonds (order of atoms from *cube files)
#           h2x
            self.p.plot3d([ax[0],ax[1]], [ay[0],ay[1]], [az[0],az[1]], tube_radius=0.02, colormap='Oranges', extent=fig_extent)
            self.p.plot3d([ax[0],ax[2]], [ay[0],ay[2]], [az[0],az[2]], tube_radius=0.02, colormap='Oranges', extent=fig_extent)
#           h2o
            self.p.plot3d([ax[5],ax[3]], [ay[5],ay[3]], [az[5],az[3]], tube_radius=0.02, colormap='Oranges', extent=fig_extent)
            self.p.plot3d([ax[5],ax[4]], [ay[5],ay[4]], [az[5],az[4]], tube_radius=0.02, colormap='Oranges', extent=fig_extent)
        else:
#           X
            f = 0.6
            c = (1.0, 1.0, 0.0)
            self.p.points3d(ax[0], ay[0], az[0], ar[0],
                            scale_factor=f,
                            resolution=80,
                            color=c,
                            scale_mode='none')
#           O
            f = 0.4
            c = (1.0, 0.0, 0.0)
            self.p.points3d(ax[5], ay[5], az[5], ar[5],
                            scale_factor=f,
                            resolution=80,
                            color=c,
                            scale_mode='none')
#           H
            f = 0.2
            c = (0.8, 0.8, 0.8)
            self.p.points3d(ax[1:5], ay[1:5], az[1:5], ar[1:5],
                            scale_factor=f,
                            resolution=80,
                            color=c,
                            scale_mode='none')
#...........plot bonds (order of atoms from *cube files)
#           h2x
            self.p.plot3d([ax[0],ax[1]], [ay[0],ay[1]], [az[0],az[1]], tube_radius=0.02, colormap='Oranges')
            self.p.plot3d([ax[0],ax[2]], [ay[0],ay[2]], [az[0],az[2]], tube_radius=0.02, colormap='Oranges')
#           h2o
            self.p.plot3d([ax[5],ax[3]], [ay[5],ay[3]], [az[5],az[3]], tube_radius=0.02, colormap='Oranges')
            self.p.plot3d([ax[5],ax[4]], [ay[5],ay[4]], [az[5],az[4]], tube_radius=0.02, colormap='Oranges')
#.......plot atom names
#        xoff = 0.05*(max(x)-min(x))
#        yoff = 0.05*(max(y)-min(y))
#        zoff = 0.05*(max(z)-min(z))
#        nx = []
#        ny = []
#        nz = []
#        for i in range(len(x)):
#            nx.append(x[i]+xoff)
#            ny.append(y[i]+yoff)
#            nz.append(z[i]+zoff)
#        for i, a in enumerate(nx):
#            self.p.text3d(nx[i], ny[i], nz[i], n[i], scale=(0.2, 0.2, 0.2), color=(0.2, 0.2, 0.2))


    def plot_atoms_3d_3mol(self, n1, r1, x1, y1, z1, n2, r2, x2, y2, z2, n3, r3, x3, y3, z3):
#       mol1:
        fig1_extent = (-10.0, -4.0, 14.0, 8.0, 0.0, 6.0)
        self.plot_atoms_3d(n1, r1, x1, y1, z1, fig_extent=fig1_extent)
#       mol1:
        fig2_extent = (-2.0, 4.0, 6.0, 0.0, 0.0, 6.0)
        #self.plot_atoms_3d(n2, r2, x2, y2, z2, fig_extent=fig2_extent)
        self.plot_atoms_3d(n2, r2, x2, y2, z2)
#       mol1:
        fig3_extent = (6.0, 12.0, -2.0, -8.0, 0.0, 6.0)
        #self.plot_atoms_3d(n3, r3, x3, y3, z3, fig_extent=fig3_extent)
        self.plot_atoms_3d(n3, r3, x3, y3, z3)


