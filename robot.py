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
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.motors = {}
		self.sensors = {}

	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sense in self.sensors:
			self.sensors[sense].Get_Value(t)

	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)


	def Act(self, t):
		for motor in self.motors:
			self.motors[motor].Set_Value(t)


