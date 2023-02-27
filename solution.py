import numpy 
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
class SOLUTION:
	def __init__(self, ID):
		self.myID = ID
		self.weights = {}
		self.totalNum = 0
		self.sensorOrNot = {}
		self.links = {}
		self.jointP = {}
		self.numSensor = 0
		self.loc = {}

		## Number of Links
		self.totalNum = numpy.random.randint(2,5)
		self.totalNum = 1
		self.links[0] = [numpy.random.rand()+ 0.1, numpy.random.rand()+ 0.1, numpy.random.rand()+ 0.1, 0,0,0,0, 0]
		self.sensorOrNot[0] = numpy.random.randint(0,2)
		self.weights = numpy.random.rand(self.totalNum + 1 ,self.totalNum + 1)
		self.weights = self.weights * 2 - 1
		for i in range(self.totalNum):
			x = i+1
			self.sensorOrNot[x] = numpy.random.randint(0,2)
			self.links[x] = [numpy.random.rand()+ 0.1, numpy.random.rand()+ 0.1, numpy.random.rand()+ 0.1, 0,0,0,0, 0]
			loc = numpy.random.randint(0,5)
			while(self.links[i][loc + 3] != 0):
				loc = numpy.random.randint(0,4)
			self.loc[x] = loc
			if (loc == 0):
				self.jointP[i] = "right"
				self.links[x][4] = 1
			elif (loc == 1):
				self.jointP[i] = "left"
				self.links[x][3] = 1
			elif (loc == 2):
				self.jointP[i] = "forward"
				self.links[x][6] = 1
			elif (loc == 3):
				self.jointP[i] = "back"
				self.links[x][5] = 1
			else:
				self.jointP[i] = "up"

	def Start_Simulation(self, state):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
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
		pyrosim.Send_Cube(name = "Ball", pos = [4, 0.5 ,0], size = [0.35, 0.35, 0.35])
		pyrosim.End()


	def Create_Body(self):
		## use a random seed 

		pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
		if (self.sensorOrNot[0] == 0):
			pyrosim.Send_Cube(name = "Link0", pos = [-1, 0, 0.5], size = [self.links[0][0], self.links[0][1], self.links[0][2]], color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
		else:
			pyrosim.Send_Cube(name = "Link0", pos = [-1, 0, 0.5], size = [self.links[0][0], self.links[0][1], self.links[0][2]], color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

		for i in range(self.totalNum):
			x = i + 1
			if (self.loc[x] == 0):
				if(i == 0):
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1+self.links[i][0]/2, 0 ,0.5], jointAxis = "1 0 0")
				else:
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [self.links[x][0]/2, 0, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [self.links[x][0]/2, 0, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

			elif (self.loc[x] == 1):
				if(i == 0):
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1 - self.links[i][0]/2, 0 ,0.5], jointAxis = "1 0 0")
				else:
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [-self.links[x][0]/2, 0, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [-self.links[x][0]/2, 0, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

			elif (self.loc[x] == 2):
				if(i ==0):
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1, self.links[i][1]/2 ,0.5], jointAxis = "1 0 0")
				else:
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, -self.links[x][1]/2, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, -self.links[x][1]/2, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

			elif (self.loc[x] == 3):
				if(i == 0):
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1, -self.links[i][1]/2 ,0.5], jointAxis = "1 0 0")
				else:
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, self.links[x][1]/2, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, self.links[x][1]/2, 0], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')
			else:
				if (i == 0):
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1, 0, 0.5 + self.links[i][2]/2], jointAxis = "1 0 0")

				else:
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
			
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, 0, self.links[x][2]/2], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, 0, self.links[x][2]/2], size = [self.links[x][0], self.links[x][1], self.links[x][2]],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')
		pyrosim.End()




	def new_Joint_Pos(self, olddir, newdir, size):
		if(olddir == newdir):
			if(olddir == "left"):
				result = [-size[0], 0, 0]
				return result
			if(olddir == "right"):
				result = [size[0], 0, 0]
				return result

			if (olddir == "up"):
				result =  [0, 0, size[2]]
				return result

			if(olddir == "back"):
				result = [0, size[1], 0]
				return result

			if(olddir == "forward"):
				result = [0, -size[1], 0]
				return result

		elif(olddir == "left"):
			if(newdir == "forward"):
				result = [-size[0]/2, -size[1]/2, 0]
				return result
			if(newdir == "back"):
				result = [-size[0]/2, size[1]/2, 0]
				return result
			if(newdir == "up"):
				result = [-size[0]/2, 0, size[2]/2]
				return result


		elif(olddir == "right"):
			if(newdir == "up"):
				result =  [size[0]/2, 0, size[2]/2]
				return result
			if(newdir == "forward"):
				result = [size[0]/2, -size[1]/2, 0]
				return result
			if(newdir == "back"):
				result = [size[0]/2, size[1]/2, 0]
				return result


		elif(olddir == "up"):
			if(newdir == "left"):
				result =  [-size[0]/2, 0, size[2]/2]
				return result
			if(newdir == "right"):
				result = [size[0]/2, 0, size[2]/2]
				return result
			if(newdir == "forward"):
				result = [0, -size[1]/2, size[2]/2]
				return result
			if(newdir == "back"):
				result = [0, size[1]/2 ,size[2]/2]
				return result


		elif(olddir == "forward"):
			if(newdir == "left"):
				result = [-size[0]/2, -size[1]/2, 0]
				return result
			if(newdir == "right"):
				result = [size[0]/2, -size[1]/2, 0]
				return result
			if(newdir == "up"):
				result = [0, -size[1]/2, size[2]/2]
				return result


		elif(olddir == "back"):
			if(newdir == "left"):
				result = [-size[0]/2, size[1]/2, 0]
				return result
			if(newdir == "right"):
				result = [size[0]/2, size[1]/2, 0]
				return result
			if(newdir == "up"):
				result = [0, size[1]/2 ,size[2]/2]
				return result



	def Create_Brain(self):
		# links with sensors are green
		# links without sensors are blue
		#green is a 0
		# blue is a 1
		## 0 HAS SENSORS
		self.numSensor = 0
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		a = 0
		for i in range(self.totalNum+1):
			if (self.sensorOrNot[i] == 0):
				pyrosim.Send_Sensor_Neuron(name = a , linkName = "Link" + str(i))
				a = a + 1
				self.numSensor = self.numSensor + 1

		for b in range(self.totalNum):
			if(b != self.totalNum-1):
				pyrosim.Send_Motor_Neuron(name = a, jointName = "Link" + str(b) + "_Link" + str(b+1))
				a = a + 1
				
		for c in range(self.numSensor):
			if(self.sensorOrNot[c] == 0):
				for d in range(self.totalNum):
					pyrosim.Send_Synapse(sourceNeuronName= c, targetNeuronName= d + self.numSensor, weight= self.weights[c][d])
		pyrosim.End()


	def Mutate(self):
		change = numpy.random.randint(0,2)
		if (change == 0):
			self.Add_Block()
		else:
			#self.Brain_Mutate()
			self.Add_Block()
	
	def Set_ID(self, ID):
		self.ID = ID

	def Brain_Mutate(self):
		if(self.numSensor < 2):
			return
		randomRow = random.randint(0,self.numSensor- 1)
		randomCol = random.randint(0, self.totalNum- 1)
		self.weights[randomRow,randomCol] = random.random()*2 - 1

	def Add_Block(self):

		print("before")
		print(self.weights)
		x = self.totalNum + 1
		self.totalNum = self.totalNum + 1

		weights = numpy.random.rand(self.totalNum+1,self.totalNum+1)
		for a in range(self.totalNum-1):
			for b in range(self.totalNum-1):
				weights[a][b] = self.weights[a][b]
		for c in range(self.totalNum):
			weights[self.totalNum][c] = numpy.random.rand()*2 - 1
		for d in range(self.totalNum):
			weights[d][self.totalNum] = numpy.random.rand()*2 - 1


		self.weights = weights


		self.sensorOrNot[x] = numpy.random.randint(0,2)
		self.links[x] = [numpy.random.rand()+ 0.1, numpy.random.rand()+ 0.1, numpy.random.rand()+ 0.1, 0,0,0,0, 0]
		loc = numpy.random.randint(0,5)
			
		while(self.links[x-1][loc + 3] != 0):
			loc = numpy.random.randint(0,4)

		self.loc[x] = loc
		if (loc == 0):
			self.jointP[x-1] = "right"
			self.links[x][4] = 1
		elif (loc == 1):
			self.jointP[x-1] = "left"
			self.links[x][3] = 1
		elif (loc == 2):
			self.jointP[x-1] = "forward"
			self.links[x][6] = 1
		elif (loc == 3):
			self.jointP[x-1] = "back"
			self.links[x][5] = 1
		else:
			self.jointP[x-1] = "up"


## links 
	# sizex
	# sizey
	# sizez
	# "right"
	# "left"
	# "forward"
	# "back"
	# "up"





