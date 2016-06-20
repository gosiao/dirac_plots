#!/usr/bin/env python

#   gosia, last revision: 17/06/2016   


import string
import os,sys
import numpy as np
import mayavi.mlab as mlab

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib

from optparse import OptionParser

# local
from plots_2d import *
from plots_3d import *
from dirac_data import *
from molecule import *


usage = """

 usage: %prog --finp= --mode= --fout --t --fgeom= --plot

  where:
  * --finp is the input file; one of *scalar or *vector files from Dirac run
  * --mode can be either 'show' or 'save_png'
  * --fout is the name of the output file; it is neccesary when mode=='save_png'
  * --t is the type of inpfile, can be one of: '3d.scalar', '3d.vector', '2d.scalar', '2d.vector'
  * --plot is the type of plot; can be one of: 'isosurface'
  * --fgeom is a 'plot.3d.cube' file - now we need it only to retrieve molecular geometry in the correct units
            if you want to use *xyz file instead - there is one line to uncomment below

"""

parser = OptionParser(usage=usage)
parser.add_option("--finp",
                  dest="inpfile",
                  action="store")

parser.add_option("--fgeom",
                  dest="geomfile",
                  action="store")

parser.add_option("--mode",
                  dest="mode",
                  action="store")

parser.add_option("--t",
                  dest="tp",
                  action="store")

parser.add_option("--fout",
                  dest="outfile",
                  action="store")

parser.add_option("--plot",
                  dest="plot",
                  action="store")

if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)

(options, args) = parser.parse_args()


# ----------------------------------------------------------------------------------------------- #

# prepare data
# ------------
dd = dirac_data(options.tp)

# densities:
f = open(options.inpfile, 'r')
if (options.tp == '3d.scalar'):
    x, y, z, s = numpy.loadtxt(f, unpack=True)
    l1, vx, vy, vz = dd.make_1d_to_3d_xyz(x, y, z)
    vs = np.array(s).reshape(l1, l1, l1)
elif (options.tp == '3d.vector'):
    x, y, z, u, v, w = numpy.loadtxt(f, unpack=True)
    l1, vx, vy, vz = dd.make_1d_to_3d_xyz(x, y, z)
    vu = np.array(u).reshape(l1, l1, l1)
    vv = np.array(v).reshape(l1, l1, l1)
    vw = np.array(w).reshape(l1, l1, l1)
elif (options.tp == '2d.scalar'):
    x, y, s = numpy.loadtxt(f, unpack=True)
    l1, vx, vy = dd.make_1d_to_2d_xy(x, y)
    vs = np.array(s).reshape(l1, l1)
elif (options.tp == '2d.vector'):
    x, y, u, v = numpy.loadtxt(f, unpack=True)
    l1, vx, vy = dd.make_1d_to_2d_xy(x, y)
    vu = np.array(u).reshape(l1, -1)
    vv = np.array(v).reshape(l1, -1)
else:
    print "give correct type; one of:'3d.scalar', '3d.vector', '2d.scalar', '2d.vector'"
f.close()


# start plotting
# --------------

if (options.tp == '3d.scalar' or options.tp == '3d.vector'):
    mlab.figure(fgcolor=(0., 0., 0.), bgcolor=(1, 1, 1))
if (options.tp == '2d.scalar' or options.tp == '2d.vector'):
    plt.figure()
    #ax = fig.add_subplot(111)

# molecule:
# be careful with units!
# e.g. geometry in *xyz files is in Angstrom, but in the preamble to *cube files is in a.u.
# to work with plot.3d* files from DIRAC we need geometry in a.u.
# that's why -- to be sure -- here we read-in molecular geometry from the corresponding *cube files
# to read geometry from xyz file - uncomment a line with a call to read_xyz_file

if (options.geomfile):
    f = open(options.geomfile, 'r')
    #(atoms_name, atoms_x, atoms_y, atoms_z) = dd.read_xyz_file(f)
    (atoms_name, atomic_nr, atoms_x, atoms_y, atoms_z) = dd.read_xyz_from_cube(f)
    f.close()
    if (options.tp == '3d.scalar' or options.tp == '3d.vector'):
        dm = molecule(mlab)
        dm.plot_atoms_3d(atoms_name, atomic_nr, atoms_x, atoms_y, atoms_z)
    elif (options.tp == '2d.scalar' or options.tp == '2d.vector'):
        dm = molecule(plt)
        dm.plot_atoms_2d(atoms_name, atoms_x, atoms_y, atoms_z, x[0], y[0], x[-1], y[-1], x[len(x)/2], y[len(x)/2])
else:
    print "no xyz file given; atoms will not be drawn"


if (options.tp == '3d.scalar'):
    dp = dirac_plots_3d(mlab)
    if (options.plot == 'isosurface'):
       #mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
       dp.plot_isosurface_3d(vx, vy, vz, vs)

if (options.tp == '3d.vector'):
    dp = dirac_plots_3d(mlab)
    if (options.plot == 'stream3d'):
       #mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
       dp.plot_streamlines_3d(vx, vy, vz, vu, vv, vw)
       #dp.plot_3d_test(x, y, z, u, v, w)

if (options.tp == '2d.vector'):
    dp = dirac_plots_2d(plt, [min(y), max(y)], [min(x), max(x)])
    if (options.plot == 'stream2d'):
       #mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
       p1 = dp.plot_streamlines(plt,vy, vx, vv, vu)
       plt.show()


if (options.mode == 'save_png'):
    mlab.savefig(options.outfile)

if (options.mode == 'show'):
    mlab.show()

#
#
#sns.set(style="dark")
#current_palette = sns.color_palette()
#sns.palplot(current_palette)
#cmap = sns.cubehelix_palette(light=1, as_cmap=True)
#
#mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
#
##sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
#plot_isosurface(mlab, xx, yy, zz, ss)
#
#mlab.colorbar(title='Shielding density', orientation='vertical')
#
##sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
##plot_contour3d(mlab, xx, yy, zz, ss)
#
#
#mlab.show()

