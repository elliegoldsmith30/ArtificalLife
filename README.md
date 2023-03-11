# CS 396 Artificial Life Final Project - Ellie Goldsmith

### Goal: Evolve the brain and body of 3D creatures in order to maximize locomotion. 
The initial creatues have a random number of randomly shaped links with random sensor placement. Links with sensors are colored green and links without sensors are colored blue.

## Body Generation
<img width="297" alt="Screen Shot 2023-03-11 at 9 20 38 AM" src="https://user-images.githubusercontent.com/92822567/224492617-b86bfc38-70f5-4a28-93b9-5b755367c3d7.png">

Random number generators are used to determine the size and location of new links.

## Brain Generation 
In order to determine which links have sensors, every time a link is generated, a random number either 0 or 1 is generated and if the number is 0, the link will have a sensor and if the number is 1, the link will not have a sensor.
<img width="435" alt="Screen Shot 2023-03-11 at 9 20 03 AM" src="https://user-images.githubusercontent.com/92822567/224492600-f18fd2ff-dc27-4e60-aaaa-50437f63655f.png">

All joints have motor neurons. All combinations of sensor neurons and motor neurons have a synapse between them. The value of the synaptic weight is determined by a random number generator for a value of -1 to 1.

## Data Storage
Location and sizes of links and joints are stored in two dictionaries. The data from these dictionaries is randomly determined (as explained above) in the initializer of the `SOLUTION` class. Then, these dictionaries are used to actually create the brains and bodies of the creature later in the code using the functions `Create_Body()` and `Create_Brain()`. 

<img width="600" alt="Screen Shot 2023-03-11 at 9 15 06 AM" src="https://user-images.githubusercontent.com/92822567/224492356-7afe2e2c-5f5e-46fb-8318-3fc7db2223d1.png">

## Evolution
The robots evolve in a parallel hill climber structure. Each generation, a deep copy of the robot is generated and the child has one mutation from the parent. Evolution of each robot in a population occurs completely separetely of the other robots in the population. 

<img width="600" alt="Screen Shot 2023-03-11 at 9 02 26 AM" src="https://user-images.githubusercontent.com/92822567/224491790-c958284a-3926-4351-9ac4-9631d1b57d7b.png">

### Fitness and Selection
Each generation, the child and parent simulations are run. Fitness is determined by distance moved from the origin. Whichever robot (parent or child) has the highest fitness is selected to continue evolving.

<img width="400" alt="Screen Shot 2023-03-11 at 9 28 31 AM" src="https://user-images.githubusercontent.com/92822567/224493017-e2ff5cc2-ee1f-4151-86f8-72516d964e72.png">

## Results
<img width="866" alt="Screen Shot 2023-03-11 at 10 41 52 AM" src="https://user-images.githubusercontent.com/92822567/224496649-e0b6a13c-19ee-44b2-bf3a-fbd24bebdc2f.png">

I ran evolution for 500 generations with a population size of 10. Each simulation was running for 1000 time points. But, the robots with the best fitness were not demonstrating locomotion. Large robots were toppling over and ended up travelling farther than robots that walked slowly. This is because of perverse instantiation. The robots were doing what I "asked" mathematically, but not in the way in which I was intending them to. In order to fix this, I ran each simulation for 5000 time points and this completely fixed the issue. Robots that actually demonstrated proper locomotion had more time to move and ultimately, moved farther than robots that quickly fell over and stopped moving.

In the end, the robots with the highest fitness were generally small (4 - 8 links each) and were able to continuously move in one direction. See below for a graph of the fitness of 10 random seeds, a ten second video showing a few random and evolved robots side by side, and a two minute summary video explaining the project and showing various evolved robots.

Fitness Curves for 10 Random Seeds with Population Sizes of 10 and 500 Generations:

<img width="752" alt="Screen Shot 2023-03-11 at 10 02 24 AM" src="https://user-images.githubusercontent.com/92822567/224494704-df5396c3-bef9-43d4-b6ec-fadd228d7fa9.png">

10 Second Teaser Gif: 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/1mkJAYk6i3g/0.jpg)](https://www.youtube.com/watch?v=1mkJAYk6i3g)

2 Minute Summary Video:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/5A2X8wW7dRs/0.jpg)](https://www.youtube.com/watch?v=5A2X8wW7dRs)



## Installation and Running the Code
Use the instructions from the first part of r/ludobots to download python3, pip, and other packages needed.

In order to run the code, open the terminal (for Mac users) and go to the directory containing the folder with the code files. 
Run the code by typing `python3 search.py` into the command window on terminal and the simulation should run beginning with a random robot showing and then parent and child fitnesses will display and it will end by simulating the best (evolved) robot. 

In order to see the best robot again, the ID number of that robot is printed when the code finishes executing. In order to rerun that, run the following command: `python3 simulate.py GUI ID&`. (If the robot ID is 37, the command is `python3 simulate.py GUI 37&`.)

In order to run the code to produce the fitness curve, run the following command: `python3 graph.py`

In order to run the simulation with different population sizes and number of generations, edit the variables `numberOfGenerations` and `populationSize` in `constants.py`.

#### Citation: Instructions taken from r/ludobots and code from pyrosim is used. Northwestern CS396 - Winter 2023 (Artificial Life)
