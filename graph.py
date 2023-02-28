import constants as c
import copy
import os 
import numpy
import matplotlib.pyplot



fitness = numpy.load("fitnessValues.npy")
#fitness1 = numpy.load("fitnessValues1.npy")
# fitness2 = numpy.load("fitnessValues2.npy")
# fitness3 = numpy.load("fitnessValues3.npy")
# fitness4 = numpy.load("fitnessValues4.npy")
# fitness5 = numpy.load("fitnessValues5.npy")

x = numpy.linspace(1,len(fitness), len(fitness))
matplotlib.pyplot.plot(x, fitness, label = "Seed 1")
#matplotlib.pyplot.plot(x, fitness1, label = "1")
# matplotlib.pyplot.plot(x, fitness2, label = "Seed 2")
# matplotlib.pyplot.plot(x, fitness3, label = "Seed 3")
# matplotlib.pyplot.plot(x, fitness4, label = "Seed 4")
# matplotlib.pyplot.plot(x, fitness5, label = "Seed 5")
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Fitness")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

