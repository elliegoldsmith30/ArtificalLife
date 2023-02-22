# CS396 Assignment 7 - Ellie Goldsmith
Goal: The code will produce a 3D creature with the following:
Random number of randomly shaped links with random sensor placement. Links with sensors are colored green and links without sensors are colored blue. Links must also be able to fill 3D space.

In order to determine which links have sensors, every time a link is generated, a random number either 0 or 1 is generated and if the number is 0, the link will have a sensor and if the number is 1, the link will not have a sensor. 

Random number generators are used to determine the size and location of new links.

The diagram below outlines the process for adding links to the chain. 

<img width="219" alt="Screen Shot 2023-02-21 at 8 07 20 PM" src="https://user-images.githubusercontent.com/92822567/220502511-e7ffdbc2-0dd9-43e3-bee3-d93f8daef6fa.png">


Installation: Use the instructions from the first part of r/ludobots to download python3, pip, and other packages needed.

Running the Code: Open the terminal (for Mac users) and go to the directory containing the folder with the code files. Run the code by typing "python3 search.py" into the command window on terminal and the simulation should run beginning with a random robot showing and then parent and child fitnesses will display and it will end by simulating the best (evolved) robot.

Citation: Instructions taken from r/ludobots and code from pyrosim is used. Northwestern CS396 - Winter 2023 (Artificial Life)


