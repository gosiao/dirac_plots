#!/usr/bin/env python

# prepare data from dirac for plotting
#
# from files we get data in columns that are read in as lists
# * plot.2d.scalar:
#   x y s
#   with x, y calculated in a loop with x outside:  for i in x; do for j in y; do echo $i $j; done; done
#   s is a scalar
#   
# * plot.2d.vector:
#   x y vx vy
#   with x, y calculated in a loop with x outside:  for i in x; do for j in y; do echo $i $j; done; done
#   vx, vy
#
# * plot.3d.scalar:
#   x y z s
#   with x, y, z calculated in a loop with x outside, z inside: for i in x; do for j in y; do for k in z; do echo $i $j $k; done; done
#
# * plot.3d.scalar:
#   x y z vx vy vz
#   with x, y, z calculated in a loop with x outside, z inside: for i in x; do for j in y; do for k in z; do echo $i $j $k; done; done
#
#
#
#   gosia, last revision: 07/04/2016   

import numpy

import string
import os,sys


#..................................................................................................#
atoms = {}
atoms['1']  = 'H'
atoms['8']  = 'O'
atoms['34'] = 'Se'
atoms['52'] = 'Te'
atoms['84'] = 'Po'

#..................................................................................................#
class dirac_data:
    def __init__(self, datatype):
        self.dt = datatype


    def make_1d_to_2d_x(self, x):
        lx = []
        len1 = 0
#.......the most external loop
        s = x[0]
        for i in range(len(x)):
            if (x[i] == s):
                len1 = len1 + 1
#       lx is a list of lists of the same elements
        lx = numpy.array(x).reshape(-1, len1)
        return len1, lx
    

    def make_1d_to_2d_xy(self, x, y):
        lx = []
        ly = []
        len1 = 0
#.......the most external loop
        s = x[0]
        for i in range(len(x)):
            if (x[i] == s):
                len1 = len1 + 1
#       lx is a list of lists of the same elements
        lx = numpy.array(x).reshape(-1, len1)
#.......the most internal loop
#       ly is a list of lists of different elements
        ly = numpy.array(y).reshape(-1, len1)
        return len1, lx, ly
    

    def make_1d_to_2d_xyz(self, x, y, z):
        lx = []
        ly = []
        lz = []
        len1 = 0
#.......the inside loop
        s = y[0]
        for i in range(len(y)):
            if (y[i] == s):
                len1 = len1 + 1
        ly = numpy.array(y).reshape(-1, len1)
        lx = numpy.array(x).reshape(-1, len1)
        lz = numpy.array(z).reshape(-1, len1)
        return len1, lx, ly, lz

    def make_1d_to_3d_xyz(self, x, y, z):
        lx = []
        ly = []
        lz = []
        len1 = 0
#.......the inside loop
        s = z[0]
        for i in range(len(z)):
            i = i + 1
            if (z[i] == s):
                len1 = len1 + i
                break
        print 'len1 = ', len1
        ly = numpy.array(y).reshape(len1, len1, len1)
        lx = numpy.array(x).reshape(len1, len1, len1)
        lz = numpy.array(z).reshape(len1, len1, len1)
        return len1, lx, ly, lz

    def read_xyz_file(self, f):
        lines = f.readlines()
        atoms = []
        x     = []
        y     = []
        z     = []
        for line in lines[2:]:
            if len(line.split()) != 0:
                atoms.append(line.split()[0])
                x.append(float(line.split()[1]))
                y.append(float(line.split()[2]))
                z.append(float(line.split()[3]))
        return (atoms, x, y, z)

    def read_xyz_from_cube(self, f):
        lines = f.readlines()
        nr_atoms = int(lines[2].split()[0])
        at_num = []
        a      = []
        x      = []
        y      = []
        z      = []
        for line in lines[6:6+nr_atoms]:
                at_num.append(int(line.split()[0]))
                a.append(atoms[line.split()[0]])
                x.append(float(line.split()[2]))
                y.append(float(line.split()[3]))
                z.append(float(line.split()[4]))
        return (a, at_num, x, y, z)

