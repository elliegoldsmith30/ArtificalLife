import constants as c
import copy
import os 
import numpy
import matplotlib.pyplot



fitness = numpy.load("fitnessValues1.npy")
x = numpy.linspace(1,len(fitness), len(fitness))
matplotlib.pyplot.plot(x, fitness)
matplotlib.pyplot.show()

