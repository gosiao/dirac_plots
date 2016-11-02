#!/usr/bin/env python

import sys
import numpy as np
import parse_input
import dirac_data
import plots_3d
import molecule_3d



def main():

#   process command line arguments
    pcl = parse_input.parse_command_line()
    pcl.process_arguments()
    pcl.print_arguments()

#   get the data
    dd   = dirac_data.prepare_data(pcl.finp_type, pcl.plot_inp)
    data = dd.get_data()

#   get the molecule (optional)
    if (pcl.cube_inp):
        dm = molecule_3d.molecule3d(pcl.cube_inp)
        mol_data = dm.get_data()

#   visualize
    if pcl.plot_type[0:2] == '3d':
        p3 = plots_3d.dirac_plots_3d(pcl.mode, pcl.plot_type, data, mol=mol_data, out=pcl.plot_out)
        p3.visualize_3d()
    else:
        print('error: unknown plot type')



if __name__ == '__main__':
    sys.exit(main())


