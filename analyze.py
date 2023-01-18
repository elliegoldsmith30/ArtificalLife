import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label = "backLeg", linewidth = 3)
matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLeg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()