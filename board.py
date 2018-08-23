""" Board """

from bricks import *
from config import *

class Board :
    """ Defining Board """

    def __init__ (self, length, width, lives, ground_brick):
        """ Initializing the board """
        self.length = length
        self.width = width
        self.matrix = [[' ' for i in range(width)] for j in range(length)]
        self.score = 0
        self.lives = lives 
        
        gbmatrix = ground_brick.return_matrix() 
        glength = ground_brick.return_length()
        gwidth =ground_brick.return_width()

        for x in range(29,34,3) :
            for y in range(0,80,4) :
                for i in range(0,gwidth) :
                    for j in range(0,glength) :
                        self.matrix[x+j][y+i] = gbmatrix[j][i]
        
        cloud_matrix = return_cloudstuff()

        for x in range(7) :
            for y in range(80) :
                self.matrix[x+2][y] = cloud_matrix[x][y]


    def ReturnStringBoard(self):
        """ Returning the board as a string """
        sBoard = ""
        for i in self.matrix:
            for j in i :    
                sBoard += j
            sBoard +="\n"

        sBoard += "Press 'q' to exit \n"
        
        return sBoard

    def ReturnMatrixBoard(self) :
        """ Returning the board as a matrix """
        return self.matrix

    def UpdateMatrix(self, newMatrix) :
        """  Updating the board matrix """
        self.matrix = newMatrix.ReturnMatrixBoard()
    
    def UpdatePartOfMatrix(self, obj) :
        """ Updating part of board matrix """
        x = obj.return_xpos()
        y = obj.return_ypos() % 80
        tempMatrix = obj.return_matrix()
        for i in range(len(tempMatrix)) :
            for j in range(len(tempMatrix[0])) :
                self.matrix[i+x][j+y] = tempMatrix[i][j]
    
    def UpdatePartOfMatrixForBakcgroundElements(self, obj) :
        """ Updating part of board matrix for background elements """
        x = obj.return_xpos()
        y = obj.return_ypos()
        tempMatrix = obj.return_matrix()

        for i in range(len(tempMatrix)) :
            for j in range(len(tempMatrix[0])) :
                if self.matrix[i+x][y+j] == ' ' :
                    self.matrix[i+x][j+y] = tempMatrix[i][j]

    def ClearingPartOfMatrix(self, obj) :
        """ Cleaning part of board matrix """
        x = obj.return_xpos()
        y = obj.return_ypos() % 80

        for i in range(x, x + obj.length):
            for j in range(y, y + obj.width):
                self.matrix[i][j] = " " 

    def ExtendMap(self, board_object) :
        """ Extending Map """ 

        MapMat = board_object.ReturnMatrixBoard()

        for i in range(len(MapMat)) :
            self.matrix[i].extend(MapMat[i])

    def UpdateFrame (self, mario, bigMap) :
        """ Updating frame based on mario's position, and returns frame's position """

        dist = mario.return_distance() 
        if mario.return_ypos() < 40 :
            dist =  dist - mario.return_ypos()
        else :
            dist = dist - 40

        tempMatrix = []
        bigMapMatrix = bigMap.ReturnMatrixBoard()

        for i in range(36) :
            tempMatrix.append([])
            for j in range(80):
                tempMatrix[i].append(' ')

        for i in range(36) :
            for j in range(80) :
                self.matrix[i][j] = bigMapMatrix[i][j+dist]

        return dist


    def UpdatingEnemiesOnFrame (self,obj,framePointer) :
        """ Updating Enemies on Frame """ 
        x = obj.return_xpos()
        y = obj.return_ypos()  
        length = obj.return_length()
        tempMatrix = obj.return_matrix()

        if y - framePointer > 0 and y + length - framePointer < 80 : 
            for i in range(len(tempMatrix)) :
                for j in range(len(tempMatrix[0])) :
                    self.matrix[i+x][j+y-framePointer] = tempMatrix[i][j]



class Boss_Board(Board) :
    """ Defining board for boss area """

    def __init__(self, length, width, lives, ground_brick) :
        Board.__init__(self, length, width, lives, ground_brick)

        gbmatrix = ground_brick.return_matrix() 
        glength = ground_brick.return_length()
        gwidth =ground_brick.return_width()

        for x in range(26,34,3) :
            for y in range(0,80,4) :
                for i in range(0,gwidth) :
                    for j in range(0,glength) :
                        self.matrix[x+j][y+i] = gbmatrix[j][i]    


        for x in range(0,12,3) :
            for y in range(0,80,4) :
                for i in range(0,gwidth) :
                    for j in range(0,glength) :
                        self.matrix[x+j][y+i] = gbmatrix[j][i]   
    