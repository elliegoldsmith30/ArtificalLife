import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x=1
y=1
z=1
for x in range(5):
	for y in range(5):
		length=1
		width=1
		height=1
		for i in range(10):
			pyrosim.Send_Cube(name = "Box" + str(i), pos = [x,y, i + 0.5], size = [length,width,height])
			length = 0.9*length
			width = 0.9*width
			height = 0.9*height
pyrosim.End()
