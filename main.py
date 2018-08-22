""" Main game loop program """

import os, sys, time
from board import Board, Boss_Board
from bricks import Brick, Ground_Brick, Special_Brick
from characters import *
from input import *
from collision import *
from config import * 
import random

""" Config """

board_length = 36
board_width = 80
start_lives = 3

brick_length = 3
brick_width = 4

mario_init_x = 3
mario_init_y = 0

sun_x = 1
sun_y = 5

hill_x = 13
hill_y = 1

""" End of config """

sun = Sun(sun_x,sun_y)
hills = Hills(hill_x,hill_y)

gBrick = Ground_Brick(26,20)
# gBrick.setPos(26, 20)

aBrick = Air_Brick(10,10)

bigMap = Board(board_length,board_width,start_lives, gBrick)

# 3 frames big rn 
frameCount = 0
for i in Map :
    frameCount = frameCount + 1

tempCount = 1 
for i in Map:
    if tempCount == frameCount - 2:
        break
    tempCount = tempCount + 1
    tempFrame = Board(board_length,board_width,start_lives, gBrick)
    for j in i :
        tempFrame.UpdatePartOfMatrix(j)

    bigMap.ExtendMap(tempFrame)


tempFrame = Boss_Board(board_length,board_width,start_lives, gBrick)
for i in range(frameCount-3, frameCount) :
    for j in Map[i] :
        tempFrame.UpdatePartOfMatrix(j)
    bigMap.ExtendMap(tempFrame)

screenBoard = Board(board_length,board_width,start_lives, gBrick)
mario = Mario(mario_init_x,mario_init_y)


sGround = ""

framePointer = 0

BrickMat = gBrick.return_matrix()

flagToCheckIfLineHasASomething = False 

GameRuns = True 

getch = Get()

jump_timer = 10 # number of seconds for jump to last


while GameRuns!=False:
    input = input_to(getch)
    os.system('clear')
    
    """ Mario movement """
    screenBoard.ClearingPartOfMatrix(mario)

    
    moveType = mario.move(input, jump_timer, screenBoard)

    #gotta limit jump 
    if jump_timer != 10 or (input == 'w' and jump_timer == 10) :
        jump_timer = jump_timer - 1 
        mario.move('w',jump_timer, screenBoard)

    if jump_timer == 0 :
        jump_timer = 10

    framePointer = screenBoard.UpdateFrame(mario, bigMap)
    screenBoard.UpdatePartOfMatrix(mario)

    if moveType == 2 :
        """ Move screen, and not mario """
        framePointer = screenBoard.UpdateFrame(mario, bigMap)

    # if moveType == 3 :
    #     """ Special block hit, replace block """
    #     block_x = mario.return_xpos()-2
    #     block_y = mario.return_distance()-3
    #     aBrick.setPos(block_x,block_y)
    #     bigMap.UpdatePartOfMatrix(aBrick)
    #     screenBoard.UpdatePartOfMatrix(aBrick)

    """ Mario movement ends """

    #insert enemy updating in frame function 
    #make this into a function
    DistFromStart = mario.return_distance()
    for i in enemies :
        empty = EmptyEnemy(i)
        if empty.return_matrix() == i.return_matrix() :
            enemies.remove(i)
            continue 

        if i.return_initial_y() >= framePointer and i.return_initial_y() < framePointer + 80 :
            screenBoard.UpdatingEnemiesOnFrame(empty, framePointer)
            i.move(screenBoard, mario)
            screenBoard.UpdatingEnemiesOnFrame(i, framePointer)
            

    if input == 'q':
        os.system('clear')
        sys.exit()

    screenBoard.UpdatePartOfMatrixForBakcgroundElements(sun)
    if framePointer <= 700 : 
        screenBoard.UpdatePartOfMatrixForBakcgroundElements(hills)
    screenBoard.UpdatePartOfMatrix(mario)
    screenBoard.UpdateMatrix(screenBoard)
    print(screenBoard.ReturnStringBoard()+'\n'+"Distance covered :"+str(mario.return_distance()) + '\n' + "Score :" + str(mario.ret_score()+mario.return_distance()))
    if mario.return_distance() >= 960 :
        print("Game over, you win!")
        break 
    time.sleep(0.025)
    

