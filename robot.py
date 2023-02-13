from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import time
import os 
import constants as c


class ROBOT:
	def __init__(self, solutionID):
		self.robot = p.loadURDF("body.urdf")
		self.motors = {}
		self.sensors = {}
		self.ID = solutionID
		self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
		pyrosim.Prepare_To_Simulate(self.robot)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		#os.system("rm brain" + str(solutionID) + ".nndf")

	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sense in self.sensors:
			self.sensors[sense].Get_Value(t)

	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)


	def Act(self, t):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRage
				self.motors[jointName].Set_Value(self.robot, desiredAngle)

	def Get_Fitness(self, yPosition):
	#	basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
	#	basePosition = basePositionAndOrientation[0]
	#	xPosition = basePosition[0]
		f = open("tmp" + str(self.ID) + ".txt", "w")
		f.write(str(yPosition))
		f.close()
		os.system("mv tmp" + str(self.ID) + ".txt" + " " + "fitness" + str(self.ID) + ".txt")

	def Think(self):
		self.nn.Update()
		# self.nn.Print()


