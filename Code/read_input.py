### read the input_file
import numpy as np

def readfile(filename):
    infile = open(filename, 'r')
    Name = infile.readline().strip().split()[2] # NAME
    FileType = infile.readline().strip().split()[2] # TYPE
    Comment = infile.readline().strip().split()[2] # COMMENT
    Dimension = infile.readline().strip().split()[2] # DIMENSION
    EdgeWeightType = infile.readline().strip().split()[2] # EDGE_WEIGHT_TYPE
    infile.readline()

    nodelist = []
    print(Dimension)
    N = int(Dimension)
    for i in range(0, N):
        x,y = infile.readline().strip().split()[1:]
        nodelist.append([float(x), float(y)])

    nodelist = np.array(nodelist, dtype="int")
    return nodelist