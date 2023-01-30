# import time
# import pybullet_data
# import pybullet as p
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import matplotlib.pylab as plt

import sys
import constants as c
from simulation import SIMULATION


directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()







