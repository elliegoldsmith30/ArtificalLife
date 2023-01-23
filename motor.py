import constants as c
import numpy
import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
	def __init__(self, jointName):
		
		self.jointName = jointName
		self.amplitude = 0
		self.frequency = 0
		self.motorValues = {}
		self.phaseOffset = 0
		#self.Prepare_To_Act()
		

	#def Prepare_To_Act(self):
	#	if (self.jointName == b'Torso_BackLeg'):
	#		self.frequency = c.frequency/2
	#	else:
	#		self.frequency = c.frequency
	#	self.amplitude = c.amplitude
	#	self.phaseOffset = c.phaseOffset
	#	self.motorValues = self.amplitude*numpy.sin(self.frequency*c.x + self.phaseOffset)
		


	def Set_Value(self, robot, desiredAngle):
		pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 30)


	#def Save_Values(self, motor):
	#	numpy.save("data/" + motor + ".npy", motor)


