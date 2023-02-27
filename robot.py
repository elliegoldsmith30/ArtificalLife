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
import math


class ROBOT:
	def __init__(self, solutionID):
		self.robot = p.loadURDF("body" + str(solutionID) + ".urdf")
		self.motors = {}
		self.sensors = {}
		self.ID = solutionID
		self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
		pyrosim.Prepare_To_Simulate(self.robot)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		#os.system("rm brain" + str(solutionID) + ".nndf")
		#os.system("rm body" + str(solutionID) + ".urdf")

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

	def Get_Fitness(self, xPosition, yPosition):
	#	basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
	#	basePosition = basePositionAndOrientation[0]
	#	xPosition = basePosition[0]
		stateOfLinkZero = p.getLinkState(self.robot,0)
		positionOfLinkZero = stateOfLinkZero[0]
		x = positionOfLinkZero[0]
		y = positionOfLinkZero[1]
		fitnessVal = math.sqrt(((x +  1) * (x + 1)) + (y * y))
		f = open("tmp" + str(self.ID) + ".txt", "w")
		f.write(str(fitnessVal))
		f.close()
		os.system("mv tmp" + str(self.ID) + ".txt" + " " + "fitness" + str(self.ID) + ".txt")

	def Think(self):
		self.nn.Update()
		# self.nn.Print()


