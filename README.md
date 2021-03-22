# Sudoku Game 

A simple Sudoku game created in python.  

## Sudoku Generator 

Program can create random UNIQUE Sudoku bord. It also allows user to select difficulty level.

###### How it works?
At the beginning we start with empty grid. Next we fill few boxes with random values. 
Of course these values must fulfill the sudoku criteria. Then we run Solving algorithm on our board. 
At this point we have complete sudoku. Last Step is taking out randomly values one by one 
and check if Sudoku still has only one solution. We repeat this process until the number of empty fields
in the grid will suit the difficulty level.

## Sudoku Solver

Program can solve the remaining sudoku at any point of game. It uses backtracking algorithm

## GUI

There is simple graphical user interface made in pygame added to Sudoku. 

### Requirements:

* Python 3

### Dependencies:

* pygame

## Sample Images:

Slash Art                                                                 |  Select Difficulty
:------------------------------------------------------------------------:|:------------------------------------------------------------------------:
![](https://github.com/krob2610/Sudoku/blob/master/images/SplashArt.png)  |  ![](https://github.com/krob2610/Sudoku/blob/master/images/DiffLevel.png)

Gameplay                                                                  |  Select Difficulty
:------------------------------------------------------------------------:|:------------------------------------------------------------------------:
![](https://github.com/krob2610/Sudoku/blob/master/images/Gameplay.png)   |  ![](https://github.com/krob2610/Sudoku/blob/master/images/Solver.png)
