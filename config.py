""" Config file, predominantly stores and sets map """

from bricks import *
from characters import Mushroom, Boss 

def return_cloudstuff() :
    """ returns scenery for cloud """    
    clouds_matrix = []

    cloud_list = ["                                      _ _                    ___                ",
                  "                                   _///////\               _////\               ",
                  "            _ __                  //////////\             /////////\_           ",
                  "           /////\_             ///////////////\         /////////////\_ _       ",
                  "        //////////\_          /////////////////\       //////////////////\      ",
                  "        \///////////|         \////////////////         \/////////////////      ",
                  "         \//////////                                     \///////////////       "]


    for i in range(len(cloud_list)) :
        clouds_matrix.append([])
        for j in range(len(cloud_list[0])):
            clouds_matrix[i].append(cloud_list[i][j])

    return clouds_matrix

# creating map
Map = []

frame = []
frame.append(Air_Brick(2*10,4*7))
frame.append(Air_Brick(2*10,4*9))
frame.append(Air_Brick(2*6,4*8))
frame.append(Special_Brick(2*10,4*8))
frame.append(Pipe(2*10, 4*16 -2))

Map.append(frame)

frame = []
frame.append(Air_Brick(2*10, 4*6))
frame.append(Special_Brick(2*10,4*7))
frame.append(Air_Brick(2*10,4*8))
frame.append(Air_Brick(2*10,4*9))
frame.append(Special_Brick(2*10,4*10))
frame.append(Air_Brick(2*10,4*11))
frame.append(Pipe(2*10, 4*16-2))

Map.append(frame)

frame = []

frame.append(Pipe(2*10, 4*16-2))
Map.append(frame)

frame = []

frame.append(Air_Brick(2*10 , 4*13))

for i in range(2) :
    for j in range(2) :
        frame.append(EmptyGround_Brick(29 + i*3, 36 + j*4))

frame.append(Air_Brick(2*10 , 4*14))
frame.append(Air_Brick(2*10 , 4*15))

Map.append(frame)

frame = []

frame.append(Special_Brick(2*10,4*4))
frame.append(Special_Brick(2*10,4*8))
frame.append(Special_Brick(2*10,4*12))
frame.append(Special_Brick(2*6,4*8))
frame.append(Pipe(2*10, 4*15+2))

Map.append(frame)

frame = []
frame.append(Air_Brick(2*10,4*4))
frame.append(Air_Brick(2*10,4*6))
frame.append(Special_Brick(2*10, 4*5))

for i in range(7):
  for j in range(7-i-1, 7):
    frame.append(Air_Brick( 5*3 + 2*i , 4*13 + 4*j))

Map.append(frame)

frame = []

for i in range(2):
  for j in range(3):
    frame.append(EmptyGround_Brick( 29 + i*3, j*4 ))
	
for i in range(7):
  for j in range(i+1):
    frame.append(Air_Brick(3*5 + i*2 , 4*j+ 4*3))

frame.append(Pipe(2*10,12*4 + 2))

Map.append(frame)

frame = []

frame.append(Air_Brick(2*10,4*2))
frame.append(Air_Brick(2*10,4*4))
frame.append(Air_Brick(2*10,4*5))
frame.append(Air_Brick(2*10,4*7))
frame.append(Special_Brick(2*10,4*3))
frame.append(Special_Brick(2*10,4*6))

for i in range(8):
  for j in range(8-i-1, 8):
    frame.append(Air_Brick( 5*3 + 2*i - 1, 4*11 + 4*j))

Map.append(frame)


frame = []

frame.append(Air_Brick(9*3 + 1, 4*4))
frame.append(Air_Brick(9*3 + 1, 4*5))
frame.append(Waterfall_Bricks(0,4*8))
#frame.append(poleFlag(10,15))
Map.append(frame)

frame = []
Map.append(frame)

frame = []
Map.append(frame)

""" make a list of enemies, with positions on the main map. If a enemy is in current frame, then pull him out of the list, and activate him. If he dies, remove him. If he leaves map, remove him.
Place him in ways such that he doesnt fall into holes lmao"""

enemies = []
enemies.append(Boss(2*11 + 1, 4*19 ))
enemies.append(Mushroom(2*13, 80 + 4* 6, 10))
enemies.append(Mushroom(2*13, 80 + 4* 10, 3))
enemies.append(Mushroom(2*13, 160 + 4* 6, 3))
enemies.append(Mushroom(2*13, 160 + 4* 10, 3))
enemies.append(Mushroom(2*13, 240 + 4* 8, 3))
enemies.append(Mushroom(2*13, 400 + 4* 6, 3))
enemies.append(Mushroom(2*13, 400 + 4* 10, 3))
enemies.append(Mushroom(2*13, 480 + 4* 8, 5))
# enemies.append(Boss(2*11, 800 + 4*2 ))
