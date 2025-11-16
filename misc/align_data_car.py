import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

path = os.path.abspath(os.getcwd())                                   # select path as current working directory (cwd)
os.chdir(path)                                                        # change directory to selected path 
for filename in os.listdir(path):                                     # iterate through current path and select each file
    line_count = 0                                                    # reinitialize line_count to 0
    with open(filename, "r") as f:                                    # open any files from the selected path
        if (f.name.find("csv") != -1):                                # do the following steps just for .csv files
            folder_name = (path + "_aligned")                         # initialize folder name as initial path + _aligned
            if not os.path.exists(path + "_aligned"):                 # if directory with _aligned path does not exist
               os.makedirs(path + "_aligned")                         # create directory with _aligned path
            os.chdir(path + "_aligned")                               # change current directory to _aligned path
            g = open(filename.split(".")[0]+"_aligned.csv", "w")      # open new file with _aligned added to the file name
            os.chdir(path)                                            # change current directory to initial path
            align_voltage_index = 0                                   # reinitialize align_voltage_index to 0
            for line in f:                                            # iterate through lines in each csv file
                if(line_count > 4):                                   # then jump over metadata lines from each csv
                    if(len(line)>1):                                  # and ignore empty lines, if any
                        if(line_count < 1000 and (float(line.split(",")[1].replace("\n", "")) - float(line.split(",")[2].replace("\n", ""))) < 1.000):      
                                                                      # check rising edge in first 1000 timesteps
                                align_voltage_index = line_count      # save line count for 1.00 Volts on rising edge (alignment index)
                line_count += 1                                       # increment line count
            #print(align_voltage_index)                               # (debug) print the align voltage index on stdout
            new_line_count = 0                                        # reinitialize new_line_count to 0
            f.seek(0)                                                 # jump with cursor to the initial position in the file
            for line in f:                                            # go again through all lines from the file
                if(new_line_count <= 4):                              # check if lines are actually metadata lines
                   g.write(line)                                      # write metadata lines before voltage data 
                if(new_line_count > align_voltage_index - 200 and new_line_count <= align_voltage_index + 1400):      
                                                                      # check if line index is in the expected range
                   g.write(line)                                      # write 1600 lines - all lines between align_voltage_index - 200 and align_voltage_index + 1400
                new_line_count += 1                                   # increment new_line_count 
            g.close()                                                 # close output file
        f.close()                                                     # close input file
