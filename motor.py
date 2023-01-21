import constants as c
import numpy
import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
	def __init__(self):
		
		self.jointName = jointName
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		print(self.amplitude)
		self.offset = c.offset
		self.Prepare_To_Act()
		self.motorValues = {}
		

	def Prepare_To_Act(self, robot):
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		self.offset = c.offset
		self.motorValues[robot] = self.amplitude * numpy.sin(self.frequency * c.x + self.phaseOffset) 


	def Set_Value(self, robot, t):
		pyrosim.Set_Motor_For_Joint( bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[robot], maxForce = 30)


	def Save_Values(self, motor):
		numpy.save("data/" + motor + ".npy", motor)


