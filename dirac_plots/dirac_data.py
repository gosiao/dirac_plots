#!/usr/bin/env python

"""
 prepare data from dirac *plot files

 supported files (from DIRAC visualization):

 * plot.2d.scalar:
   x y  s
   
 * plot.2d.vector:
   x y  u v

 * plot.3d.scalar:
   x y z  s

 * plot.3d.scalar:
   x y z  u v w


   2d: x, y calculated in a loop with x outside:  for i in x; do for j in y; do echo $i $j; done; done
   3d: x, y, z calculated in a loop with x outside, z inside: for i in x; do for j in y; do for k in z; do echo $i $j $k; done; done

"""

import numpy as np
import sys


class prepare_data:


    def __init__(self, data_type, file_name):

        self.dt = data_type
        self.fname = file_name 


    def get_data(self):

        try:
            f = open(self.fname, 'r')
        except:
            print('error in opening the file ', self.fname)

        if self.dt == '3d.scalar':
            x, y, z, s = np.loadtxt(f, unpack=True)
            data = self.xyz_1d_to_3d(x, y, z, s=s)
        elif self.dt == '3d.vector':
            x, y, z, u, v, w = np.loadtxt(f, unpack=True)
            data = self.xyz_1d_to_3d(x, y, z, u=u, v=v, w=w)
        else:
            print('error: unknown data type')

        f.close()
        return data


    def xyz_1d_to_3d(self, x, y, z, s=None, u=None, v=None, w=None):

#       mayavi 3d visualization works on the 3d arrays
#       thus we need to transform the 1d x, y, ... vectors to 3d arrays
#       this is what this function is doing

        l = 0
#       z is the most inner loop for grid points on plot.3d* files
        z0 = z[0]
        for i in range(len(z)):
            i = i + 1
            if (z[i] == z0):
                l = l + i
                break

        x = np.array(x).reshape(l, l, l)
        y = np.array(y).reshape(l, l, l)
        z = np.array(z).reshape(l, l, l)

        if s != []:
            s = np.array(s).reshape(l, l, l)
            data = [x, y, z, s]
        elif (u != [] or v != [] or w != []):
            u = np.array(u).reshape(l, l, l)
            v = np.array(v).reshape(l, l, l)
            w = np.array(w).reshape(l, l, l)
            data = [x, y, z, u, v, w]
        else:
            sys.exit('error in xyz_1d_to_3d')

        return data




