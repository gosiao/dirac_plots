#!/usr/bin/env python

#   gosia, last revision: 20/06/2016   


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
#from molecule import *
from new_molecule_3d import *


usage = """

 usage: %prog --finp= --mode= --fout --t --fgeom= --plot

  where:
  * --finp1/2/3 are the input files for system 1/2/3
  * --mode can be either 'show' or 'save_png'
  * --fout is the name of the output file; it is neccesary when mode=='save_png'
  * --t is the type of inpfile, can be one of: '3d.scalar', '3d.vector', '2d.scalar', '2d.vector'
  * --plot is the type of plot; can be one of: 'isosurface'
  * --fgeom1/2/3 are 'plot.3d.cube' files - now we need it only to retrieve molecular geometry in the correct units
            if you want to use *xyz file instead - there is one line to uncomment below

"""

parser = OptionParser(usage)

parser.add_option("--finp1",
                  dest="inp1",
                  action="store")

parser.add_option("--finp2",
                  dest="inp2",
                  action="store")

parser.add_option("--finp3",
                  dest="inp3",
                  action="store")

parser.add_option("--fgeom1",
                  dest="geomfile1",
                  action="store")

parser.add_option("--fgeom2",
                  dest="geomfile2",
                  action="store")

parser.add_option("--fgeom3",
                  dest="geomfile3",
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

# here we will have 15 input files (5 densities to show for 3 systems)
# we assume they are in order
x1 = []
y1 = []
z1 = []
s1 = []
vx1 = []
vy1 = []
vz1 = []
vs1 = []
for finp in options.inp1.split():
    f = open(finp, 'r')
    if (options.tp == '3d.scalar'):
        x, y, z, s = numpy.loadtxt(f, unpack=True)
        l1, vx, vy, vz = dd.make_1d_to_3d_xyz(x, y, z)
        vs = np.array(s).reshape(l1, l1, l1)
        x1.append(x)
        y1.append(y)
        z1.append(z) 
        s1.append(s)
        vx1.append(vx) 
        vy1.append(vy)
        vz1.append(vz)
        vs1.append(vs)
    f.close()


x2 = []
y2 = []
z2 = []
s2 = []
vx2 = []
vy2 = []
vz2 = []
vs2 = []
for finp in options.inp2.split():
    f = open(finp, 'r')
    if (options.tp == '3d.scalar'):
        x, y, z, s = numpy.loadtxt(f, unpack=True)
        l1, vx, vy, vz = dd.make_1d_to_3d_xyz(x, y, z)
        vs = np.array(s).reshape(l1, l1, l1)
        x2.append(x)
        y2.append(y)
        z2.append(z) 
        s2.append(s)
        vx2.append(vx) 
        vy2.append(vy)
        vz2.append(vz)
        vs2.append(vs)
    f.close()

x3 = []
y3 = []
z3 = []
s3 = []
vx3 = []
vy3 = []
vz3 = []
vs3 = []
for finp in options.inp3.split():
    f = open(finp, 'r')
    if (options.tp == '3d.scalar'):
        x, y, z, s = numpy.loadtxt(f, unpack=True)
        l1, vx, vy, vz = dd.make_1d_to_3d_xyz(x, y, z)
        vs = np.array(s).reshape(l1, l1, l1)
        x3.append(x)
        y3.append(y)
        z3.append(z) 
        s3.append(s)
        vx3.append(vx) 
        vy3.append(vy)
        vz3.append(vz)
        vs3.append(vs)
    f.close()

print 'buba ', len(x1), len(x2), len(x3)

#f = open(options.inpfile, 'r')
#if (options.tp == '3d.scalar'):
#    x, y, z, s = numpy.loadtxt(f, unpack=True)
#    l1, vx, vy, vz = dd.make_1d_to_3d_xyz(x, y, z)
#    vs = np.array(s).reshape(l1, l1, l1)
#elif (options.tp == '3d.vector'):
#    x, y, z, u, v, w = numpy.loadtxt(f, unpack=True)
#    l1, vx, vy, vz = dd.make_1d_to_3d_xyz(x, y, z)
#    vu = np.array(u).reshape(l1, l1, l1)
#    vv = np.array(v).reshape(l1, l1, l1)
#    vw = np.array(w).reshape(l1, l1, l1)
#elif (options.tp == '2d.scalar'):
#    x, y, s = numpy.loadtxt(f, unpack=True)
#    l1, vx, vy = dd.make_1d_to_2d_xy(x, y)
#    vs = np.array(s).reshape(l1, l1)
#elif (options.tp == '2d.vector'):
#    x, y, u, v = numpy.loadtxt(f, unpack=True)
#    l1, vx, vy = dd.make_1d_to_2d_xy(x, y)
#    vu = np.array(u).reshape(l1, -1)
#    vv = np.array(v).reshape(l1, -1)
#else:
#    print "give correct type; one of:'3d.scalar', '3d.vector', '2d.scalar', '2d.vector'"
#f.close()



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

#if (options.geomfile):
#    f = open(options.geomfile, 'r')
#    #(atoms_name, atoms_x, atoms_y, atoms_z) = dd.read_xyz_file(f)
#    (atoms_name, atomic_nr, atoms_x, atoms_y, atoms_z) = dd.read_xyz_from_cube(f)
#    f.close()
#    if (options.tp == '3d.scalar' or options.tp == '3d.vector'):
#        dm = molecule(mlab)
#        dm.plot_atoms_3d(atoms_name, atomic_nr, atoms_x, atoms_y, atoms_z)
#    elif (options.tp == '2d.scalar' or options.tp == '2d.vector'):
#        dm = molecule(plt)
#        dm.plot_atoms_2d(atoms_name, atoms_x, atoms_y, atoms_z, x[0], y[0], x[-1], y[-1], x[len(x)/2], y[len(x)/2])
#else:
#    print "no xyz file given; atoms will not be drawn"
#
f = open(options.geomfile1, 'r')
(atoms_name1, atomic_nr1, atoms_x1, atoms_y1, atoms_z1) = dd.read_xyz_from_cube(f)
f.close()
f = open(options.geomfile2, 'r')
(atoms_name2, atomic_nr2, atoms_x2, atoms_y2, atoms_z2) = dd.read_xyz_from_cube(f)
f.close()
f = open(options.geomfile3, 'r')
(atoms_name3, atomic_nr3, atoms_x3, atoms_y3, atoms_z3) = dd.read_xyz_from_cube(f)
f.close()
dm = molecule_3d(mlab)
dm.plot_atoms_3d_3mol(atoms_name1, atomic_nr1, atoms_x1, atoms_y1, atoms_z1, atoms_name2, atomic_nr2, atoms_x2, atoms_y2, atoms_z2, atoms_name3, atomic_nr3, atoms_x3, atoms_y3, atoms_z3)



if (options.tp == '3d.scalar'):
    dp = dirac_plots_3d(mlab)
    if (options.plot == 'isosurface'):
       #mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
       #dp.plot_isosurface_3d(vx, vy, vz, vs)
       dp.plot_many_isosurfaces_3d(vx1, vy1, vz1, vs1, vx2, vy2, vz2, vs2, vx3, vy3, vz3, vs3)

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

