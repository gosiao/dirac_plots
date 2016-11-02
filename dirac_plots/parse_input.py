#!/usr/bin/env python

"""
    parsing the command line arguments for dirac_plots
"""

import os
import sys
from optparse import OptionParser


class parse_command_line():

    def __init__(self):

        self.plot_inp = ''
        self.plot_out = ''
        self.cube_inp = ''

        self.mode = 'show'
        self.finp_type = ''
        self.plot_type = ''

    def process_arguments(self):

        usage = """
        
         usage: 
          %prog --finp= --ftype= --plot= [--fcube= --mode= --fout=]
        
          where:
          * --finp is the input file; one of plot*scalar or plot*vector files from Dirac run
          * --mode can be either 'show' (default) or 'save_png'
          * --fout is the name of the output file on which the plot is written in png format (necessary when mode=='save_png')
          * --ftype is the type of inpfile, can be one of: '3d.scalar', '3d.vector', '2d.scalar', '2d.vector'
          * --plot is the type of plot; can be one of: 'isosurface.3d', ....
          * --fcube is a 'plot.3d.cube' file - we need it only to retrieve molecular geometry in the correct units
        
        """

        parser = OptionParser(usage)
        
        parser.add_option('--finp',
                          dest='plot_inp',
                          type='string',
                          default=self.plot_inp,
                          metavar='FILE',
                          help='one of plot* files from DIRAC calculations',
                          action='store')
        
        parser.add_option('--fcube',
                          dest='cube_inp',
                          type='string',
                          default=self.cube_inp,
                          metavar='FILE',
                          help='a related *cube file - the information on geometry of the molecule is used',
                          action='store')
        
        parser.add_option('--mode',
                          dest='mode',
                          type='string',
                          default=self.mode,
                          help='either show the plot on the screen or save as *png file',
                          action='store')
        
        parser.add_option('--ftype',
                          dest='finp_type',
                          type='string',
                          default=self.finp_type,
                          help='type of the plot, can be one of: 3d.scalar, 3d.vector, 2d.scalar, 2d.vector',
                          action='store')
        
        parser.add_option('--plot',
                          dest='plot_type',
                          type='string',
                          default=self.plot_type,
                          help='what to plot, can be one of: 3d.isosurface,....',
                          action='store')

        parser.add_option('--fout',
                          dest='plot_out',
                          type='string',
                          default=self.plot_out,
                          metavar='FILE',
                          help='name of output file, has to be *png',
                          action='store')
        
        
        if len(sys.argv) < 2:
            parser.print_usage()
            sys.exit(1)
        
        (options, args) = parser.parse_args()


        if options.plot_inp:
            self.plot_inp = options.plot_inp
        else:
            print('--finp is mandatory')

        if options.finp_type:
            self.finp_type = options.finp_type
        else:
            print('--ftype is mandatory')

        if options.plot_type:
            self.plot_type = options.plot_type
        else:
            print('--plot is mandatory')

        if options.plot_out:
            self.plot_out = options.plot_out

        if options.cube_inp:
            self.cube_inp = options.cube_inp

        if options.mode:
            self.mode = options.mode


    def print_arguments(self):

        print('dirac_plots: command line arguments:')
        print('plot_inp  = ', self.plot_inp)
        print('finp_type = ', self.finp_type)
        print('plot_type = ', self.plot_type)
        print('plot_out  = ', self.plot_out)
        print('cube_inp  = ', self.cube_inp)
        print('mode      = ', self.mode)



