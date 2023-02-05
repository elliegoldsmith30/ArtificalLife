import numpy 
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
class SOLUTION:
	def __init__(self, ID):
		self.myID = ID
		self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
		self.weights = self.weights * 2 - 1


	def Evaluate(self, state):
		self.Create_World()
		self.Create_Brain()
		self.Create_Body()
		self.file = "python3 simulate.py " + state +" " + str(self.myID) + "2&>1 &"
		print("hello")
		os.system(self.file)
		while not os.path.exists(fitnessFileName):
			time.sleep(0.01)
		fitnessFileName = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float((fitnessFileName.read()))
		fitnessFileName.close()


	def Start_Simulation(self, state):
		self.Create_World()
		self.Create_Brain()
		self.Create_Body()
		self.file = "python3 simulate.py " + state +" " + str(self.myID) + "&"
		os.system(self.file)

	def Wait_For_Simulation_To_End(self):
		while not os.path.exists("fitness" + str(self.myID)+".txt"):
			time.sleep(0.1)
		fitnessFileName = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float((fitnessFileName.read()))
		fitnessFileName.close()
		os.system("rm fitness" + str(self.myID) + ".txt")




	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name = "Ball", pos = [0.5, 0.5 ,0], size = [0.35, 0.35, 0.35])
		pyrosim.End()


	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		
		# pyrosim.Send_Cube(name = "Torso", pos = [0, 0, 1], size = [1,1,1])
		
		# pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name = "BackLeg", pos = [0,-0.5, 0], size = [0.2,1,0.2])
		
		# pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name = "FrontLeg", pos = [0, 0.5, 0], size = [0.2,1,0.2])
		
		# pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name = "LeftLeg", pos = [-0.5, 0, 0], size = [1,0.2,0.2])
		
		# pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name = "RightLeg", pos = [0.5, 0, 0], size = [1,0.2,0.2])
		
		# pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name = "FrontLowerLeg", pos = [0, 0, -0.5], size = [0.2,0.2,1])
		
		# pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name = "BackLowerLeg", pos = [0, 0, -0.5], size = [0.2,0.2,1])
		
		# pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
		# pyrosim.Send_Cube(name = "LeftLowerLeg", pos = [0, 0, -0.5], size = [0.2,0.2,1])
		
		# pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0, 0], jointAxis = "0  1 0")
		# pyrosim.Send_Cube(name = "RightLowerLeg", pos = [0, 0, -0.5], size = [0.2,0.2,1])

		pyrosim.Send_Cube(name = "Torso", pos = [0, 0, 1.625], size = [0.75, 0.4, 1])
		pyrosim.Send_Cube(name = "Head", pos = [0,0, 0.25], size = [0.4,0.4,0.4])
		pyrosim.Send_Joint(name = "Torso_Head", parent = "Torso", child = "Head", type = "revolute", position = [0, 0 , 2.1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name =  "LeftLeg", pos = [0, 0, -.625], size = [0.4,0.4, 1.25])
		pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-0.375, 0 , 1.25], jointAxis = "1 0 0")


		pyrosim.Send_Cube(name =  "RightLeg", pos = [0, 0, -.625], size = [0.4,0.4, 1.25])
		pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [0.375, 0 , 1.25], jointAxis = "1 0 0")


		pyrosim.Send_Cube(name = "LeftShoulder", pos = [-0.15, 0, 0], size = [0.3, 0.4, 0.2])
		pyrosim.Send_Joint(name = "Torso_LeftShoulder", parent = "Torso", child = "LeftShoulder", type = "revolute", position = [-0.2, 0 , 2.05], jointAxis = "1 0 0")


		pyrosim.Send_Cube(name = "RightShoulder", pos = [0.15, 0, 0], size = [0.3, 0.4, 0.2])
		pyrosim.Send_Joint(name = "Torso_RightShoulder", parent = "Torso", child = "RightShoulder", type = "revolute", position = [0.2, 0 , 2.05], jointAxis = "1 0 0")

		pyrosim.Send_Cube(name = "LeftArm", pos = [-0.1, 0, -0.3], size = [0.2, 0.4, 0.6])
		pyrosim.Send_Joint(name = "LeftShoulder_LeftArm", parent = "LeftShoulder", child = "LeftArm", type = "revolute", position = [-0.3, 0 ,0], jointAxis = "1 0 0")

		pyrosim.Send_Cube(name = "RightArm", pos = [0.1, 0, -0.3], size = [0.2, 0.4, 0.6])
		pyrosim.Send_Joint(name = "RightShoulder_RightArm", parent = "RightShoulder", child = "RightArm", type = "revolute", position = [0.3, 0 ,0], jointAxis = "1 0 0")




		pyrosim.End()


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightLeg")
		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_LeftLeg")
		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_RightLeg")
		pyrosim.Send_Motor_Neuron( name = 5 , jointName = "LeftShoulder_LeftArm")
		pyrosim.Send_Motor_Neuron( name = 6 , jointName = "RightShoulder_RightArm")
		# pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "BackLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Torso")

		# pyrosim.Send_Motor_Neuron( name = 5 , jointName = "FrontLeg_FrontLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 6 , jointName = "BackLeg_BackLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 7 , jointName = "LeftLeg_LeftLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 8, jointName = "RightLeg_RightLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_FrontLeg")
		# pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_BackLeg")
		# pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
		# pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")


		for currentRow in range(c.numSensorNeurons):
			for currentColumn in range(c.numMotorNeurons):
				pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn + c.numSensorNeurons, weight= self.weights[currentRow][currentColumn])
		pyrosim.End()



	def Mutate(self):
		randomRow = random.randint(0,c.numSensorNeurons - 1)
		randomCol = random.randint(0, c.numMotorNeurons - 1)
		self.weights[randomRow,randomCol] = random.random()*2 - 1

	def Set_ID(self, ID):
		self.ID = ID

