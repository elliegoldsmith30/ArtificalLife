import constants as c

class MOTOR:
	def __init__(self):
		
		self.jointName = jointName
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		self.offset = c.offset
		self.Prepare_To_Act()
		#pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.motorCommandBackLeg[x], maxForce = 30)
 		#pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.motorCommandFrontLeg[x], maxForce = 30)


	def Prepare_To_Act(self, robotId ):
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		self.offset = c.offset


	def Set_Value

