#!/usr/bin/env python


#   gosia, last revision: 03/04/2016



import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pylab
import seaborn as sns

import string
import os,sys

from matplotlib import colors, ticker, cm


class dirac_plots_2d:

    def __init__(self, p, x_range, y_range):
        self.rotate      = 1
        self.orientation = ''
        self.p           = p
        self.x_range     = x_range
        self.y_range     = y_range
        axes = self.p.gca()
        axes.set_xlim([self.x_range[0], self.x_range[1]])
        axes.set_ylim([self.y_range[0], self.y_range[1]])


    def plot_streamlines(self, p, x, y, vx, vy):
#.......play with these settings to get the nicest streamlines:
#       -------------------------------------------------------
        stream_color   = 'k'
        stream_density = 2.5
        stream_cmap    = plt.cm.bwr
        back_cmap = cm.PuBu_r
#.......and plot:
#       ---------
        f, ax = plt.subplots(figsize=(16, 8))
        magnitude = np.sqrt(vx*vx + vy*vy)
        ps = p.streamplot(x, y, vx, vy,
                          color   = stream_color,
                          #color   = magnitude,
                          density = stream_density,
                          #linewidth = magnitude/magnitude.max(),
                          cmap    = stream_cmap)
        sns.set(style="dark")
        cmap = sns.cubehelix_palette(start=0, light=1, as_cmap=True)
        #sns.kdeplot(x, y, cmap=cmap, shade=True, cut=5, ax=ax)
        sns.kdeplot(x, y, cmap=cmap, shade=True, cut=5)
        #ps = p.contourf(x, y, magnitude, 
        #          locator=ticker.LogLocator(),
        #          cmap=back_cmap)
        return ps


    def plot_contour(self, p, x, y, v):
#.......play with these settings to get the nicest contours:
#       ----------------------------------------------------
        contour_alpha = 0.5
        contour_cmap  = plt.cm.coolwarm
        #contour_cmap  = plt.get_cmap('PiYG')
#
        # v_min and v_max as min() and max() of s
        v_min = v.min()
        v_max = v.max()
        print 'v_min, v_max = ', v_min, v_max
        contour_color_range = np.linspace(v_min, v_max, 15, endpoint=True)
        #contour_levels  = MaxNLocator(nbins=15).tick_values(v_min, v_max)
        pc = p.contourf(x, y, v,
                        contour_color_range,
                        alpha  = contour_alpha,
                        #levels = contour_levels,
                        locator = ticker.LogLocator(),
                        cmap   = contour_cmap)
        return pc

    def plot_add_legend(self, p, ps, pc):
        contour_bar = p.colorbar(pc)





