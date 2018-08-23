""" Config file, predominantly stores and sets map """

from bricks import *
from characters import Mushroom, Boss 


board_length = 36
board_width = 80
start_lives = 3

brick_length = 3
brick_width = 4

mario_init_x = 12
mario_init_y = 0

sun_x = 1
sun_y = 5

hill_x = 13
hill_y = 1

Mushroom_speed = 2


def return_cloudstuff() :
    """ returns scenery for cloud """    
    clouds_matrix = []

    cloud_list = ["                                      _ _                    ___                ",
                  "                                   _///////\               _////\               ",
                  "            _ __                  //////////\             /////////\_           ",
                  "           /////\_             ///////////////\         /////////////\_ _       ",
                  "        //////////\_          /////////////////\       //////////////////\      ",
                  "        \///////////\         \////////////////         \/////////////////      ",
                  "         \///////////                                    \///////////////       "]


    for i in range(len(cloud_list)) :
        clouds_matrix.append([])
        for j in range(len(cloud_list[0])):
            clouds_matrix[i].append(cloud_list[i][j])

    return clouds_matrix

""" Map holds supplementary design of overall game map, and appending frames, and objects inside them, designs the levels """
""" Bricks, Pipes, signboards are set up in section 1. Enemies in section 2 via a list of objects. Coins in section 3 via a list of objects """
""" Section 1 """
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
frame.append(Beware(2*11 + 1, 4*17))
Map.append(frame)

frame = []

Map.append(frame)

frame = []
frame.append(PrincessHere(2*11 + 1, 4*17))
Map.append(frame)

frame = []
Map.append(frame)
""" End of section 1 """

""" Section 2 """

""" make a list of enemies, with positions on the main map. If a enemy is in current frame, then pull him out of the list, and activate him. If he dies, remove him. If he leaves map, remove him.
Place him in ways such that he doesnt fall into holes lmao"""

enemies = []

enemies.append(Mushroom(2*13, 80 + 4* 6, 10))
enemies.append(Mushroom(2*13, 80 + 4* 10, 3))
enemies.append(Mushroom(2*13, 160 + 4* 6, 3))
enemies.append(Mushroom(2*13, 160 + 4* 10, 3))
enemies.append(Mushroom(2*13, 240 + 4* 8, 3))
enemies.append(Mushroom(2*13, 400 + 4* 6, 3))
enemies.append(Mushroom(2*13, 400 + 4* 10, 3))
enemies.append(Mushroom(2*13, 480 + 4* 8, 5))
enemies.append(Boss(2*10, 880 + 4*14 ))

""" Section 2 """

""" Section 3 """
coins = []

coins.append(Coin(2*10,4*8+81))
coins.append(Coin(2*10,4*7 + 161))
coins.append(Coin(2*10,4*10 + 161))
coins.append(Coin(2*10,401 + 4*4))
coins.append(Coin(2*10,401 + 4*8))
coins.append(Coin(2*10,401 + 4*12))
coins.append(Coin(2*6,401 + 4*8))

""" End of section 3 """
