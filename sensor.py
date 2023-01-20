class SENSOR:
	def __init__(self):
		self.linkname = linkname
		self.values = numpy.zeros(1000)


	def Get_Value(self,t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
