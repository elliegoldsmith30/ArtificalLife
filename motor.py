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
		self.Prepare_To_Act()
		

	def Prepare_To_Act(self):
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		self.phaseOffset = c.phaseOffset
		self.motorValues = self.amplitude*numpy.sin(self.frequency*c.x + self.phaseOffset)
		print(self.motorValues)


	def Set_Value(self, robot, t):
		pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[t], maxForce = 30)


	def Save_Values(self, motor):
		numpy.save("data/" + motor + ".npy", motor)


