""" Main game loop program """

import os, sys, time
from board import Board, Boss_Board
from bricks import Brick, Ground_Brick, Special_Brick, UnderGround_Brick, EmptyCoin
from characters import *
from input import *
from collision import *
from config import * 
import random
from colorama import Fore


sun = Sun(sun_x,sun_y)
hills = Hills(hill_x,hill_y)

gBrick = Ground_Brick(26,20)
ugBrick = UnderGround_Brick(26,20)

aBrick = Air_Brick(10,10)

bigMap = Board(board_length,board_width,start_lives, gBrick)

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


tempFrame = Boss_Board(board_length,board_width,start_lives, ugBrick)
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

jump_timer = 10 # number of frames for jump to last

os.system('aplay -q main_theme.wav&')
os.system('sleep 2 &aplay -q Its_a_me_mario.wav&')
os.system('sleep 7 && aplay -q Mamma_mia.wav&')

while GameRuns!=False:
    input = input_to(getch)
    os.system('clear')
    
    """ Mario movement """
    screenBoard.ClearingPartOfMatrix(mario)

    
    moveType = mario.move(input, jump_timer, screenBoard)

    if jump_timer != 10 or (input == 'w' and jump_timer == 10) :
        os.system('aplay -q jump.wav&')
        jump_timer = jump_timer - 1 
        mario.move('w',jump_timer, screenBoard)

    if jump_timer == 0 :
        jump_timer = 10

    framePointer = screenBoard.UpdateFrame(mario, bigMap)
    screenBoard.UpdatePartOfMatrix(mario)

    if moveType == 2 :
        """ Move screen, and not mario """
        framePointer = screenBoard.UpdateFrame(mario, bigMap)

    """ Mario movement ends """

    """ Enemies Updation """
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
    """ Enemies done """

    """ Coins """
    for i in coins :
        empty = EmptyCoin(i)
        if empty.return_matrix() == i.return_matrix() :
            coins.remove(i) 
            continue
        if i.return_ypos() >= framePointer and i.return_ypos() < framePointer + 80 :
            screenBoard.UpdatingEnemiesOnFrame(empty, framePointer)
            i.test(screenBoard, mario)
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
    

