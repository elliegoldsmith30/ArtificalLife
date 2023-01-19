import numpy


amplitudeBL = numpy.pi/4
frequencyBL = 10
phaseOffsetBL = 0
amplitudeFL = numpy.pi/4
frequencyFL = 10
phaseOffsetFL = 0


backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
x = numpy.linspace(0, 2*numpy.pi, 1000)
motorCommandBackLeg = amplitudeBL*numpy.sin(frequencyBL*x+phaseOffsetBL) 
motorCommandFrontLeg = amplitudeFL*numpy.sin(frequencyFL*x+phaseOffsetFL) 

numpy.save("data/motorCommandBackLeg.npy", motorCommandBackLeg)
numpy.save("data/motorCommandFrontLeg.npy", motorCommandFrontLeg)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
