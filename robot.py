from sensor import SENSOR
from motor import MOTOR

import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy



class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense
		self.motors = {}

	def Prepare_To_Sense():
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense():
		frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
		backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
