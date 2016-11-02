#!/usr/bin/env python

import numpy as np
from mayavi import mlab


class atoms():

    def __init__(self):

        self.atoms = {}
        self.atoms['1']  = 'H'
        self.atoms['8']  = 'O'
        self.atoms['34'] = 'Se'
        self.atoms['52'] = 'Te'
        self.atoms['84'] = 'Po'
 


class molecule3d:

    def __init__(self, file_name):
        self.fname = file_name
        self.atoms = atoms()

    def get_data(self):

        try:
            f = open(self.fname, 'r')
        except:
            print('error in opening the file ', self.fname)

        data = self.read_mol_from_cube(f)
        f.close()
        return data


    def read_mol_from_cube(self, f):

        lines = f.readlines()
        nr_atoms = int(lines[2].split()[0])
        at_num = []
        a      = []
        x      = []
        y      = []
        z      = []
        for line in lines[6:6+nr_atoms]:
                at_num.append(int(line.split()[0]))
                a.append(self.atoms.atoms[line.split()[0]])
                x.append(float(line.split()[2]))
                y.append(float(line.split()[3]))
                z.append(float(line.split()[4]))
        return [at_num, a, x, y, z]


           
