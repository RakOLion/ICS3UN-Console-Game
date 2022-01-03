import msvcrt
import numpy as np
import time
import random
import os

#GAME FUNCTIONS
def cls():
  os.system('cls')

def render(board): 
  cls()
  for x in range(0, board.shape[0]):
    row = "\r"
    for y in range(0, board.shape[1]):
      row+=str(board[x][y])+" "
    print(row)
  print("\rSCORE: "+str(int((score/(x_dimension*y_dimension))*100))+"%") 
 
def move_up(x, y): 
  y = (y-1)%y_dimension
  return [x,y]
def move_down(x, y): 
  y = (y+1)%y_dimension
  return [x,y]
def move_left(x, y): 
  x = (x+1)%x_dimension
  return [x,y]
def move_right(x, y): 
  x = (x-1)%x_dimension
  return [x,y]

def instructions(): 
  print("INSTRUCTIONS")
  print("Use the keys w,a,s,d to move your player [O] around the grid")
  print("Avoid the obstacles [X] that spawn randomly across the field. As you walk, you will leave a trail on the floor of obstacles")
  print("Score is calculated by the percentage number of moves you are able to make before dying compared to the area")

def game_end(): 
  print("\rGAME OVER!")

def is_obstacle(x,y,locations): 
  for i in obstacleLocations:
    if(y == i[1] and x == i[0]):
      return True
  return False

#CUSTOMIZATION
difficulty_spawnrates = [0.0025, 0.005, 0.01, 0.05, 0.1]
score = 1
obstacleLocations = []

instructions() 
print()
x_dimension = int(input("Enter the x-dimension (reccomended for first-time -> 10): "))
y_dimension = int(input("Enter the y-dimension (reccomended for first-time -> 10): "))
print()
print("There are 5 different difficulty settings ranging from 1 (very easy) to 5 (very hard).")
difficulty = int(input("Which difficulty would you like to play at (reccomended for first-time -> 2): "))-1 

currentBoard = np.empty((x_dimension,y_dimension), dtype='object') 
currentBoard[:] = '□'
currX = int(x_dimension/2)
currY = int(y_dimension/2)

#MAIN GAME LOOP
while True:
  if msvcrt.kbhit():
    char = msvcrt.getch()
    if char==b'd': 
      obstacleLocations.append([currX,currY]) 
      currX = move_left(currX, currY)[0]
      score+=1 
    elif char==b'a':
      obstacleLocations.append([currX,currY])
      currX = move_right(currX, currY)[0]
      score+=1
    elif char== b'w':
      obstacleLocations.append([currX,currY])
      currY = move_up(currX, currY)[1]
      score+=1
    elif char==b's':
      obstacleLocations.append([currX,currY])
      currY = move_down(currX, currY)[1]
      score+=1
    char = '' 

  for x in range(0, currentBoard.shape[0]):
    for y in range(0, currentBoard.shape[1]):
      if (not ((x == currX or x == currX+1 or x==currX-1) and (y == currY or y == currY+1 or y==currY-1)) and not is_obstacle(x,y,obstacleLocations)):
        if(random.random()<difficulty_spawnrates[difficulty]): 
          currentBoard[y][x] = 'X'
          obstacleLocations.append([x,y])

  if(is_obstacle(currX, currY, obstacleLocations)): 
    break

  currentBoard[currY, currX] = 'O'
  render(currentBoard)
  currentBoard[currY, currX] = 'X' 

  time.sleep(0.25)

game_end() 


 