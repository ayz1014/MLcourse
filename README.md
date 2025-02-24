# MLcourse
Maze Game with Q-Learning AI

1.Overview

This project is a maze-solving game implemented in Python using the tkinter library for the graphical user interface (GUI). The game supports two modes:

(1)Player Mode : The player can manually navigate through the maze using keyboard controls.
(2)AI Mode : An AI agent uses Q-Learning to automatically solve the maze.
The maze is generated using a Depth-First Search (DFS) algorithm, and the AI agent learns to solve the maze by updating its Q-Table based on rewards and penalties.

2.Features

Dynamic Maze Generation : A random maze is generated each time the game starts using DFS.

Two Game Modes :
Player Mode : Control the player using arrow keys (Up, Down, Left, Right).
AI Mode : Watch the AI solve the maze autonomously.
Q-Learning AI :
Learns optimal paths through the maze using reinforcement learning.
Evaluates performance based on steps taken and total rewards.
Score Tracking : Tracks the player's score or the AI's evaluation metrics.

3.Installation
Prerequisites
Python 3.x
Required libraries: tkinter, numpy
You can install the required libraries using the following command:
pip install numpy
(Note: tkinter is included with most Python installations. If it's not available, you may need to install it via your system package manager (e.g., sudo apt-get install python3-tk on Ubuntu). )

Clone the Repository
To clone this repository, run the following command:
git clone https://github.com/your-username/maze-game-q-learning.git
cd maze-game-q-learning

4.Usage
Run the game script:
python mazegame.py

Once the game window opens, you will see two buttons:
Player's Game : Start the game in manual mode.
AI AutoGame : Let the AI solve the maze automatically.
In Player Mode , use the arrow keys (Up, Down, Left, Right) to move the player through the maze.
In AI Mode , the AI will automatically navigate the maze, and its performance (steps and rewards) will be displayed after completion.

5.How It Works
Maze Generation
The maze is generated using a Depth-First Search (DFS) algorithm. Walls are carved out randomly to create a solvable path from the start to the end.

Q-Learning AI
The AI agent uses Q-Learning to learn the optimal path:

States : Represented by the player's position in the maze.
Actions : Moving in one of four directions (Up, Down, Left, Right).
Rewards :
+100 for reaching the goal.
-10 for hitting a wall.
-1 for each step taken.
Q-Table Update : The Q-Table is updated using the Bellman equation.
Scoring
Player Mode : The score decreases by 1 for each step and increases by 100 upon reaching the goal.
AI Mode : Displays the number of steps taken and the total reward accumulated.

6.Example
Here’s an example of how the game looks when running in AI Mode :

AI Mode Example
![MAZE](https://github.com/user-attachments/assets/12c693f4-47bf-4ad8-8bbe-b92adfa849e7)


7.Ideas for Improvement
Add more complex maze generation algorithms (e.g., Prim's Algorithm).
Implement additional AI algorithms (e.g., Deep Q-Learning).
Add difficulty levels (e.g., larger mazes or more obstacles).
Improve the GUI with better visuals or animations.
