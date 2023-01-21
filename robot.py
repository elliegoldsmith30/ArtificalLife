from sensor import SENSOR
from motor import MOTOR

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import time


class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		self.motors = {}
		self.sensors = {}
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sense in self.sensors:
			self.sensors[sense].Get_Value(t)

	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.sensors[jointName] = SENSOR(jointName)


	def Act(self, t):
		for motor in self.motors:
			self.motors[motor].Set_Value(t)


