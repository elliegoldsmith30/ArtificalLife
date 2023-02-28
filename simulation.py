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
	def __init__(self, state, solutionID):
		self.directOrGUI = state
		if(state == "DIRECT"):
			physicsClient = p.connect(p.DIRECT)
		else:
			physicsClient = p.connect(p.GUI)
	#	p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT(solutionID)

	def Run(self):
		for x in range(1000):
			p.stepSimulation()
			self.robot.Sense(x)
			self.robot.Think()
			self.robot.Act(x)
			if (self.directOrGUI == "GUI"):
				time.sleep(1/4800)

	def Get_Fitness(self):
		self.robot.Get_Fitness(self.world.Get_Pos(0), self.world.Get_Pos(1))

	def __del__(self):
		p.disconnect()
