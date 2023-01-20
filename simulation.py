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
	def __init__(self):
		physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT()

	def Run():
		for x in range(1000):
			p.stepSimulation()
			robot.Sense()
			time.sleep(1/1000)


	def __del__(self):
		p.disconnect()

# 	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.motorCommandBackLeg[x], maxForce = 30)
# 	pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.motorCommandFrontLeg[x], maxForce = 30)
