# game_of_life

## Description:
The purpose of this program is to Implement Conway's Game of Life in 64-bit integer space using Python. 


## Rules:
1. Consider a 2d grid where each cell is either Alive or Dead
2. In our case `Alive` cells will contain a 1 and dead cells will contain a 0
3. The cells can exist *Anywhere* in the 64bit Integer space
4. The simulation will start with input from STDIN
5. The input will be a list of (x,y) pairs representing an individual cell in the grid
6. All of the represented cells will be considered `Alive` when the game starts
7. Every subsequent `tick` of the simulation is called a `Generation`
8. With each generation the existing cells will follow these rules:
    1. A tally of `Alive` cells will be made around each cell in the grid
    2. That tally will be taken from the 8 cells directly around the `cell`
    3. During the tally `out of range` cells are considered to be `Dead`
    4. 2 > `alive_neighbors` > 3 If an existing `alive` cell meets this criteria it will now be considered `dead`
    5. 3 == `alive_neighbors` If an existing `dead` cell meets this criteria it is now `alive`
    
9. Simulation will run 10 generations
10. At the end of 10 generations we will print out the board in life.1.06 format


## How to Run:

### Command Line:
From the command line this version of game of life is setup to take its initial input from STDIN.
Included in the `game` directory is a sample input file named `input1.txt`. Using a terminal from 
within the `game` folder the following command will run the game of life simulation using the test
file as its initial input:

    python3 game_of_life.py < input1.txt


Additionally there is a small set of unit tests that have been added to the package that helped
navigate some initial POC things as well as acting as basic regression tests as functionality was 
added. These can be run from the command line in the root directory of the project with 
the following command:

    python3 -m unittest test/testGame.py
