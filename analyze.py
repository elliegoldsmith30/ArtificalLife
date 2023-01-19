import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
print(backLegSensorValues)
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
motorCommandBackLeg = numpy.load("data/motorCommandBackLeg.npy")
motorCommandFrontLeg = numpy.load("data/motorCommandFrontLeg.npy")
matplotlib.pyplot.plot(motorCommandBackLeg, linewidth = 4, label = "Back Leg Motors")
matplotlib.pyplot.plot(motorCommandFrontLeg, label = "Front Leg Motors")

#matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLeg", linewidth = 3)
#matplotlib.pyplot.plot(backLegSensorValues, label = "backLeg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()