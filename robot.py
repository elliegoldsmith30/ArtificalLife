from sensor import SENSOR
from motor import MOTOR

import pybullet_data
import pybullet as p



class ROBOT:
	def __init__(self):
		self.sensors = {}
		self.motors = {}
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
