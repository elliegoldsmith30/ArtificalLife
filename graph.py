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
# fitness6 = numpy.load("fitnessValues6.npy")
# fitness7 = numpy.load("fitnessValues7.npy")
# fitness8 = numpy.load("fitnessValues8.npy")
# fitness9 = numpy.load("fitnessValues9.npy")
# fitness10 = numpy.load("fitnessValues10.npy")
# fitness11 = numpy.load("fitnessValues11.npy")


x = numpy.linspace(1,len(fitness), len(fitness))
matplotlib.pyplot.plot(x, fitness, label = "Seed 1")
# matplotlib.pyplot.plot(x, fitness11, label = "Seed 2")
# #matplotlib.pyplot.plot(x, fitness1, label = "Seed 2")
# matplotlib.pyplot.plot(x, fitness2, label = "Seed 3")
# matplotlib.pyplot.plot(x, fitness3, label = "Seed 4")
# matplotlib.pyplot.plot(x, fitness4, label = "Seed 5")
# matplotlib.pyplot.plot(x, fitness5, label = "Seed 6")
# matplotlib.pyplot.plot(x, fitness6, label = "Seed 7")
# matplotlib.pyplot.plot(x, fitness7, label = "Seed 8")
# matplotlib.pyplot.plot(x, fitness8, label = "Seed 9")
# matplotlib.pyplot.plot(x, fitness9, label = "Seed 10")
# matplotlib.pyplot.plot(x, fitness10, label = "Seed 10")
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Fitness")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

