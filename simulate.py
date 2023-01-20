# import time
# import pybullet_data
# import pybullet as p
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import matplotlib.pylab as plt
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
SIMULATION.Run()




# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
# for x in range(1000):
# 	p.stepSimulation()
# 	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.motorCommandBackLeg[x], maxForce = 30)
# 	pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.motorCommandFrontLeg[x], maxForce = 30)
# 	time.sleep(1/1000)
# p.disconnect()


#targetAngles = numpy.pi/4*numpy.sin(x)

