# CS396 Assignment 8 - Ellie Goldsmith

Goal: Evolve the brain and body of 3D creatures in order to maximize locomotion. The initial creatues have a random number of randomly shaped links with random sensor placement. Links with sensors are colored green and links without sensors are colored blue. 

Body Generation:

<img width="350" alt="Screen Shot 2023-02-28 at 3 28 19 PM" src="https://user-images.githubusercontent.com/92822567/221984236-c47539f4-e78a-4a7f-bb54-f69c799c4dc2.png">

Random number generators are used to determine the size and location of new links.

Brain Generation:
In order to determine which links have sensors, every time a link is generated, a random number either 0 or 1 is generated and if the number is 0, the link will have a sensor and if the number is 1, the link will not have a sensor.

All joints have motor neurons. All combinations of sensor neurons and motor neurons have a synapse between them. The value of the synaptic weight is determined by a random number generator for a value of -1 to 1.

Mutation Function:

<img width="433" alt="Screen Shot 2023-02-28 at 3 36 12 PM" src="https://user-images.githubusercontent.com/92822567/221986165-7d99e8a7-0dd2-490f-aaee-ee1a66a22675.png">

Installation: Use the instructions from the first part of r/ludobots to download python3, pip, and other packages needed.

Running the Code: Open the terminal (for Mac users) and go to the directory containing the folder with the code files. Run the code by typing "python3 search.py" into the command window on terminal and the simulation should run beginning with a random robot showing and then parent and child fitnesses will display and it will end by simulating the best (evolved) robot. In order to see the best robot again, the ID number of that robot is printed when the code finishes executing. In order to rerun that, run the following command: python3 simulate.py GUI ID&. In order to run the code to produce the fitness curve, run the following command: python3 graph.py

Citation: Instructions taken from r/ludobots and code from pyrosim is used. Northwestern CS396 - Winter 2023 (Artificial Life)
