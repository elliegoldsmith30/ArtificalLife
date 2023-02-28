from solution import SOLUTION
import constants as c
import copy
import os 
import numpy
import matplotlib.pyplot

class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		for file in os.listdir("."):
			if (file.startswith("brain") or file.startswith("fitness")) or file.startswith("body"):
				os.system("rm {0}".format(file))
		self.parents = {}
		self.nextAvailableID = 0
		for x in range(c.populationSize):
			self.parents[x] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1
		self.fitnessVal = numpy.zeros(c.numberOfGenerations)
		self.currentGen = 0


	def Evolve(self):
		self.Evaluate(self.parents)
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()
			self.Save_Fitness()

	def Save_Fitness(self):
		best = 0
		for x in self.parents:
			if(self.parents[x].fitness > self.parents[best].fitness):
				best = x
		self.fitnessVal[self.currentGen] = self.parents[best].fitness
		self.currentGen = self.currentGen + 1

	def Save_Fitness_File(self):
		matplotlib.pyplot.plot(self.fitnessVal)
		#show plot
		numpy.save("fitnessValues5.npy", self.fitnessVal)
		fF = open("fitnessValues.txt", "w")
		fF.write(str(self.fitnessVal))
		fF.close()


	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		self.Print()
		self.Select()


	def Spawn(self):
		self.children = {}
		for i in self.parents:
			self.children[i]= copy.deepcopy(self.parents[i])
			self.children[i].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1

	def Mutate(self):
		for child in self.children:
			self.children[child].Mutate()

	def Evaluate(self, solutions):
		for p_size in range(c.populationSize):
			solutions[p_size].Start_Simulation("DIRECT")
		for p_size in range(c.populationSize):
			solutions[p_size].Wait_For_Simulation_To_End()


	def Select(self):
		for x in self.parents:
			if(self.parents[x].fitness < self.children[x].fitness):
				self.parents[x] = self.children[x]

	def Print(self):
		print("\n")
		for key in self.parents:
			print("parent fitness " + str(self.parents[key].fitness) + " child fitness " + str(self.children[key].fitness))
		print("\n")

	def Show_Random(self):
		randomRobot = numpy.random.randint(0,len(self.parents))
		self.parents[randomRobot].Start_Simulation("GUI")

	def Show_Best(self):
		best = 0
		for x in self.parents:
			if(self.parents[x].fitness > self.parents[best].fitness):
				best = x
		self.parents[best].Start_Simulation("GUI")
		self.parents[best].Get_ID()




