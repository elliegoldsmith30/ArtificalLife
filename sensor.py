import numpy
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim


class SENSOR:

	def __init__(self, linkname):
		self.linkname = linkname
		self.values = numpy.zeros(1000)

	def Prepare_To_Sense(self):
		pass


	def Get_Value(self,t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)



	def Save_Values(self, sensor):
		numpy.save("data/" + sensor + ".npy", sensor)
