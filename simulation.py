from world import WORLD
from robot import ROBOT
import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import random
import matplotlib.pylab as plt

class SIMULATION:
	def __init__(self, state):
		if(state == "DIRECT"):
			physicsClient = p.connect(p.DIRECT)
		else:
			physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT()

	def Run(self):
		for x in range(200):
			p.stepSimulation()
			self.robot.Sense(x)
			self.robot.Think()
			self.robot.Act(x)
			time.sleep(1/500)

	def Get_Fitness(self):
		self.robot.Get_Fitness()

	def __del__(self):
		p.disconnect()
