import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
print(backLegSensorValues)
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles = numpy.load("data/targetAngles.npy")
#matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLeg", linewidth = 3)
matplotlib.pyplot.plot(backLegSensorValues, label = "backLeg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()