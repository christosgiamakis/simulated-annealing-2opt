import time
start_time = time.time()
from math import sin, cos, sqrt, atan2, radians
import sys
from scipy.spatial.distance import pdist, squareform
import numpy as np

class ReadData():
    def __init__(self, filename):

        self.name = filename[:-4]
        self.size = self.getSize()
        self.EdgeWeightType = self.getEdgeWeightType()
        #self.format_ = self.getFormat()  # for EXPLICIT data only
        self.time_to_read = 0

    def getEdgeWeightType(self):
        EdgeType = "None"
        try:
            with open(f'TSP_Data/{self.name}.tsp') as data:
                datalist = data.read().split()
                for ind, elem in enumerate(datalist):
                    if elem == "EDGE_WEIGHT_TYPE:":
                        EdgeType = datalist[ind + 1]
                        #print(EdgeType)
                        break
                    elif elem == "EDGE_WEIGHT_TYPE":
                        EdgeType = datalist[ind + 2]
                        #print(EdgeType)
                        break
            return EdgeType

        except IOError:
            print("Input file not found")
            sys.exit(1)

    def getSize(self):
        """
        Return size of instances (i.e. Number of
        cities)
        
        """
        size = 0
        try:
            with open(f'TSP_Data/{self.name}.tsp') as data:
                datalist = data.read().split()
                for ind, elem in enumerate(datalist):
                    if elem == "DIMENSION:":
                        size = datalist[ind + 1]
                        #print(size)
                        break
                    elif elem == "DIMENSION":
                        size = datalist[ind + 2]
                        #print(size)
                        break
            return int(size)
        except IOError:
            print("Input file not found")
            sys.exit(1)

    def read_Data(self):
        with open(f'TSP_Data/{self.name}.tsp') as data:
            cities = []
            Isdata = True
            while (Isdata):
                line = data.readline().split()
                if len(line) <= 0:
                    break
                tempcity = []
                for i, elem in enumerate(line):
                    try:
                        temp = float(elem)
                        tempcity.append(temp)
                    except ValueError:
                        break
                if len(tempcity) > 0:
                    cities.append(np.array(tempcity))
        return np.array(cities)

    def GetDistanceMat(self):
        if self.EdgeWeightType == "EUC_2D" :
            DistanceMat = self.EuclidDist()
            self.time_to_read = time.time() - start_time
            return DistanceMat

    def EuclidDist(self):
        cities = self.read_Data()
        #DistanceDict = {}
        A = cities[:, 1:3]
        DistanceMat = np.round(squareform(pdist(A)))
        return DistanceMat



