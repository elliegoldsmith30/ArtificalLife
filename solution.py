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


	def Evaluate(self, state):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		self.file = "python3 simulate.py " + state +" " + str(self.myID) + "2&>1 &"
		os.system(self.file)
		while not os.path.exists(fitnessFileName):
			time.sleep(0.01)
		fitnessFileName = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float((fitnessFileName.read()))
		fitnessFileName.close()


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
		pyrosim.Start_URDF("body.urdf")
		self.totalNum = numpy.random.randint(3,10)
		sizex = numpy.random.rand()+0.1
		sizey = numpy.random.rand()+0.1
		sizez = numpy.random.rand()+0.1
		self.sensorOrNot[0] = numpy.random.randint(0,2)
		#pyrosim.Send_Joint(name = "Link0_Link1", parent = "Link0", child = "Link1", type = "revolute", position = [-1+sizex/2, 0 ,0], jointAxis = "1 0 0")
		self.links[0] = [sizex, sizey, sizez, 0,0,0,0, 0]
		if (self.sensorOrNot[0] == 0):
			pyrosim.Send_Cube(name = "Link0", pos = [-1, 0, 0.5], size = [sizex, sizey, sizez], color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
		else:
			pyrosim.Send_Cube(name = "Link0", pos = [-1, 0, 0.5], size = [sizex, sizey, sizez], color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')


		for i in range(self.totalNum):
			x = i+1
			self.sensorOrNot[x] = numpy.random.randint(0,2)
			sizex = numpy.random.rand()+ 0.1
			sizey = numpy.random.rand() + 0.1
			sizez = numpy.random.rand() + 0.1
			loc = numpy.random.randint(0,5)
			
			while(self.links[i][loc + 3] != 0):
				loc = numpy.random.randint(0,4)


			self.sensorOrNot[x] = numpy.random.randint(0,2)
			self.links[x] = [sizex, sizey, sizez, 0,0,0,0, 0]

			# 3 = "right"
			# 4= "left"
			# 5 = "forward"
			# 6 = "back"
			# 7 = "up"

			if (loc == 0):
				#Joint
				if(i == 0):
					self.jointP[0] = "right"
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1+self.links[i][0]/2, 0 ,0.5], jointAxis = "1 0 0")
				else:
					self.jointP[i] = "right"
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
				#Cube
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

				self.links[x][4] = 1

			elif (loc == 1):
				#Joint
				if(i == 0):
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1 - self.links[i][0]/2, 0 ,0.5], jointAxis = "1 0 0")
					self.jointP[0] = "left"
				else:
					self.jointP[i] = "left"
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
				#Cube
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [-sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [-sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

				self.links[x][3] = 1

			elif (loc == 2):
				#Joint
				if(i ==0):
					self.jointP[0] = "forward"
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1, self.links[i][1]/2 ,0.5], jointAxis = "1 0 0")
				else:
					self.jointP[i] = "forward"
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
				#Cube
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, -sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, -sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

				self.links[x][6] = 1


			elif (loc == 3):
				#Joint
				if(i == 0):
					self.jointP[0] = "back"
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1, -self.links[i][1]/2 ,0.5], jointAxis = "1 0 0")
				else:
					self.jointP[i] = "back"
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")


				#Cube
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

				self.links[x][5] = 1


			else:
				#Joint
				if (i == 0):
					self.jointP[0] = "up"
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = [-1, 0, 0.5 + self.links[i][2]/2], jointAxis = "1 0 0")

				else:
					self.jointP[i] = "up"
					newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
					
					pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				

				#Cube
				if(self.sensorOrNot[x] == 0):
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, 0, sizez/2], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
				else:
					pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, 0, sizez/2], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

		pyrosim.End()




	def new_Joint_Pos(self, olddir, newdir, size):
	#	print(olddir)
	#	print(newdir)
	#	print(size)
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










	# def Create_Body(self):
	# 	pyrosim.Start_URDF("body.urdf")

	# 	self.totalNum = numpy.random.randint(2,10)

	# 	#self.totalNum = 5
	# 	# # Cube and Joint One
	# 	sizex = numpy.random.rand()+0.1
	# 	sizey = numpy.random.rand()+0.1
	# 	sizez = numpy.random.rand()+0.1

		
	# 	pyrosim.Send_Joint(name = "Link0_Link1", parent = "Link0", child = "Link1", type = "revolute", position = [-1+sizex/2, 0 ,0], jointAxis = "1 0 0")
	# 	pyrosim.Send_Cube(name = "Link1", pos = [sizex/2, 0, 0], size = [sizex, sizey, 1])
	# 	self.sensorOrNot[0] = numpy.random.randint(0,2)
	# 	if (self.sensorOrNot[0] == 0):
	# 		pyrosim.Send_Cube(name = "Link0", pos = [-1, 0, 0.5], size = [sizex, sizey, sizez], color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
	# 	else:
	# 		pyrosim.Send_Cube(name = "Link0", pos = [-1, 0, 0.5], size = [sizex, sizey, sizez], color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')



	# 	for i in range(self.totalNum):
	# 		x = i+1
	# 		self.sensorOrNot[x] = numpy.random.randint(0,2)
	# 		sizex = numpy.random.rand()+0.1
	# 		sizey = numpy.random.rand()+0.1
	# 		sizez = numpy.random.rand()+0.1
	# 		newposCube = sizex/2
	# 		newposJoint = sizex
	# 		if(self.sensorOrNot[x] == 0):
	# 			pyrosim.Send_Cube(name = "Link" + str(x), pos = [newposCube, 0, 0.5], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
	# 			#print("Link" + str(x))
	# 		else:
	# 			pyrosim.Send_Cube(name = "Link" + str(x), pos = [newposCube, 0, 0.5], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')
	# 			#print("Link" + str(x))
	# 		if (x != self.totalNum):
	# 			pyrosim.Send_Joint(name = "Link" + str(x) + "_Link" + str(x+1), parent = "Link" + str(x), child = "Link" + str(x+1), type = "revolute", position = [newposJoint, 0 ,0], jointAxis = "1 0 0")


	# 	pyrosim.End()


	def Create_Brain(self):
		# links with sensors are green
		# links without sensors are blue
		#green is a 0
		# blue is a 1
		## 0 HAS SENSORS
		self.weights = numpy.random.rand(self.totalNum,self.totalNum)
		self.weights = self.weights * 2 - 1

		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		a = 0
		self.numSensor = 0
		for i in range(self.totalNum):
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
					#print(self.weights[c][d])

			

		pyrosim.End()



	def Mutate(self):
		change = numpy.random.randint(0,2)
		# if (change == 0):
		# 	self.Add_Block()
		# else:
		# 	self.Brain_Mutate()
		self.Brain_Mutate()
	

	def Set_ID(self, ID):
		self.ID = ID



	def Brain_Mutate(self):
		randomRow = random.randint(0,self.numSensor- 1)
		randomCol = random.randint(0, self.totalNum- 1)
		self.weights[randomRow,randomCol] = random.random()*2 - 1


# 	def Add_Block(self):
# 		x = self.totalNum + 1
# 		self.totalNum = self.totalNum + 1
# 		loc = numpy.random.randint(0,5)
# 		while(self.links[i][loc + 3] != 0):
# 			loc = numpy.random.randint(0,4)
# 		newSensor = numpy.random.randint(0,2)
# 		if(newSensor == 0):
# 			self.numSensor = self.numSensor + 1
# 			for a in range(self.totalNum):
# 				self.weights[self.numSensor][a] = numpy.random.randint(0,2)
# 			for b in range(self.numSensor):
# 				self.weights[b][self.totalNum] = numpy.random.randint(0,2)
# 		else:
# 			for a in range(self.totalNum):
# 				self.weights[self.numSensor][a] = numpy.random.randint(0,2)
# 		for a in range(self.totalNum)
		
# 		self.sensorOrNot[x] = newSensor
# 		self.links[x] = [sizex, sizey, sizez, 0,0,0,0, 0]
# 		if (loc == 0):
# 			self.jointP[i] = "right"
# 			newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
# 			pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
# 			if(self.sensorOrNot[x] == 0):
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
# 			else:
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')
# 			self.links[x][4] = 1

# 		elif (loc == 1):
# 			self.jointP[i] = "left"
# 			newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
# 			pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
# 				#Cube
# 			if(self.sensorOrNot[x] == 0):
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [-sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
# 			else:
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [-sizex/2, 0, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')
# 			self.links[x][3] = 1

# 		elif (loc == 2):
# 			self.jointP[i] = "forward"
# 			newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
# 			pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
# 			if(self.sensorOrNot[x] == 0):
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, -sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
# 			else:
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, -sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')

# 			self.links[x][6] = 1


# 		elif (loc == 3):
# 			self.jointP[i] = "back"
# 			newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])
# 			pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
			
# 			if(self.sensorOrNot[x] == 0):
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
# 			else:
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, sizey/2, 0], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')
# 			self.links[x][5] = 1


# 		else:
# 			self.jointP[i] = "up"
# 			newPos = self.new_Joint_Pos(self.jointP[i-1], self.jointP[i], [self.links[i][0], self.links[i][1], self.links[i][2]])		
# 			pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(x), parent = "Link" + str(i), child = "Link" + str(x), type = "revolute", position = newPos, jointAxis = "1 0 0")
				
# 			if(self.sensorOrNot[x] == 0):
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, 0, sizez/2], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 0 1.0"/>', colorName = '<material name="Green">')
# 			else:
# 				pyrosim.Send_Cube(name = "Link" + str(x), pos = [0, 0, sizez/2], size = [sizex, sizey, sizez],  color = '    <color rgba="0 1.0 1.0 1.0"/>', colorName = '<material name="Cyan">')



# 		if(newSensor == 0):
# 			for d in range(self.totalNum):
# 				pyrosim.Send_Synapse(sourceNeuronName= self.numSensor-1, targetNeuronName= d + self.numSensor, weight= self.weights[c][d])


# for c in range(self.numSensor):
# 			if(self.sensorOrNot[c] == 0):
# 				for d in range(self.totalNum):
# 					pyrosim.Send_Synapse(sourceNeuronName= c, targetNeuronName= d + numSensor, weight= self.weights[c][d])
# 					#print(self.weights[c][d])







## Quadruped		
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


## Bipedal robot

		# pyrosim.Send_Cube(name = "Torso", pos = [0, 0, 1.625], size = [0.75, 0.4, 1])
		# pyrosim.Send_Cube(name = "Head", pos = [0,0, 0.25], size = [0.4,0.4,0.4])
		# pyrosim.Send_Joint(name = "Torso_Head", parent = "Torso", child = "Head", type = "revolute", position = [0, 0 , 2.1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name =  "LeftLeg", pos = [0, 0, -.625], size = [0.4,0.4, 1.25])
		# pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-0.375, 0 , 1.25], jointAxis = "1 0 0")


		# pyrosim.Send_Cube(name =  "RightLeg", pos = [0, 0, -.625], size = [0.4,0.4, 1.25])
		# pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [0.375, 0 , 1.25], jointAxis = "1 0 0")


		# pyrosim.Send_Cube(name = "LeftShoulder", pos = [-0.15, 0, 0], size = [0.3, 0.4, 0.2])
		# pyrosim.Send_Joint(name = "Torso_LeftShoulder", parent = "Torso", child = "LeftShoulder", type = "revolute", position = [-0.2, 0 , 2.05], jointAxis = "1 0 0")


		# pyrosim.Send_Cube(name = "RightShoulder", pos = [0.15, 0, 0], size = [0.3, 0.4, 0.2])
		# pyrosim.Send_Joint(name = "Torso_RightShoulder", parent = "Torso", child = "RightShoulder", type = "revolute", position = [0.2, 0 , 2.05], jointAxis = "1 0 0")

		# pyrosim.Send_Cube(name = "LeftArm", pos = [-0.1, 0, -0.3], size = [0.2, 0.4, 0.6])
		# pyrosim.Send_Joint(name = "LeftShoulder_LeftArm", parent = "LeftShoulder", child = "LeftArm", type = "revolute", position = [-0.3, 0 ,0], jointAxis = "1 0 0")

		# pyrosim.Send_Cube(name = "RightArm", pos = [0.1, 0, -0.3], size = [0.2, 0.4, 0.6])
		# pyrosim.Send_Joint(name = "RightShoulder_RightArm", parent = "RightShoulder", child = "RightArm", type = "revolute", position = [0.3, 0 ,0], jointAxis = "1 0 0")



		# Quadruped
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

		#Bipedal Robot
		#pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		# pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		# pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftLeg")
		# pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightLeg")
		# pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_LeftLeg")
		# pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_RightLeg")
		# pyrosim.Send_Motor_Neuron( name = 5 , jointName = "LeftShoulder_LeftArm")
		# pyrosim.Send_Motor_Neuron( name = 6 , jointName = "RightShoulder_RightArm")
		#pyrosim.Send_Sensor_Neuron(name = 1, linkName = "Link0")
		# for currentRow in range(c.numSensorNeurons):
		# 	for currentColumn in range(c.numMotorNeurons):
		# 		pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn + c.numSensorNeurons, weight= self.weights[currentRow][currentColumn])
		#pyrosim.End()


