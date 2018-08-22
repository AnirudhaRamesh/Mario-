""" Characters """

from collision import *

class Character:
    """ Definition of a basic character """

    def __init__ (self, x, y):
        """ Initializing a person """
        self.length = None
        self.width = None 
        self.lives = 0
        self.matrix = []
        self.x = x
        self.y = y 
        self.overallDist = 0
        

    def move_left(self):
        if self.y >= 1 :
            self.y = self.y - 1
            self.overallDist = self.overallDist - 1  
    

    def return_matrix(self):
        return self.matrix
    
    def return_length(self): 
        return self.length
        
    def return_width(self):
        return self.width

    def return_xpos(self):
        return self.x 

    def return_ypos(self):
        return self.y
        
    def gravity(self, timer,board_object):
        """ continuous decrese in height whenever possible """
        if CollisionBricks(self.x + 1, self.y, self.length,self.width, board_object ) == 0 and timer == 10 :
            self.x = self.x + 1
    
    def destroy(self):
        """ checks if lives are over, if so replaces with empty block of same dimensions """
        if self.lives >= 1 :
            self.lives = 0 
            newMat = []
            length = self.length
            width = self.width
            for i in range(length) :
                newMat.append([])
                for j in range(width) :
                    newMat[i].append(' ')

            self.matrix = newMat

        else :
            self.lives = self.lives - 1 
        
    def return_distance(self) :
        return self.overallDist



class Mario(Character):
    """ Definition of Mario """

    def __init__(self, x, y) :
        """ Initializing Mario """
        Character.__init__(self, x, y)
        super(Mario,self).__init__(x, y)
        self.type = 1
        self.matrix = [[' ','(',')',' '],['/','|','|','\\'],['/',' ',' ','\\']]
        self.lives = 1
        self.length = 3
        self.width = 4
        self.score = 0

    def returnLives(self) :
        """ Returning number of lives left """
        return self.lives 
    
    def move_right(self):
        
        self.overallDist = self.overallDist + 1

        if self.y <= 40 :
            self.y = self.y + 1
            return 1
        else :
            return 2

    def jump_up (self, timer):
        if timer >= 0 :
            self.x = self.x - 1
        # if timer < 0 :
    def ret_score(self) :
        """ Returns overall score """
        return self.score 

    def Increment_score(self, points) :
        """ Increments Mario Score """
        self.score = self.score + points

    def move(self, ch, timer, board_object) :
        """ Read input character and move the character if possible """

        self.gravity(timer,board_object)
        
        if ch == 'a' and CollisionBricks(self.x, self.y - 1, self.length,self.width, board_object ) == 0:
            self.move_left() 
            return 1
        elif CollisionBricks(self.x, self.y - 1, self.length,self.width, board_object ) == 2:
            self.destroy()
            if self.lives == 0:
                print("Game overr, your score is "+ str(self.ret_score()+self.return_distance()))
                exit()

        if ch == 'w' and CollisionBricks(self.x - 1, self.y, self.length,self.width, board_object ) == 0:    
           self.jump_up(timer)
           return 1 

        if ch == 'd' and CollisionBricks(self.x, self.y + 1, self.length,self.width, board_object ) == 0 :
            return self.move_right()
        elif CollisionBricks(self.x, self.y + 1, self.length,self.width, board_object ) == 2 :
            self.destroy()
            if self.lives == 0 :
                print("Game overr, your score is "+ str(self.ret_score()+self.return_distance()))
                exit()



class Mushroom(Character) :
    """ Definition of Mushroom """

    def __init__(self, x, y, leash) :
        """ Initializing Mushroom """
        Character.__init__(self, x, y)
        self.type = 2
        self.matrix = [['=','=','=','='],['[','0','0',']'],['!','|','|','!']]
        self.lives = 1
        self.length = 3 
        self.width = 4
        self.initial_y = y
        self.moveleft = True 
        self.leash = leash
        self.points_For_Killing = 50

    def returnLives(self) :
        """ Returning number of lives left """
        return self.lives 

    def return_initial_y(self) :
        return self.initial_y 

    def move(self, board_object, mario) :
        
        if mario.return_distance()%80 >= self.y % 80-self.width and mario.return_distance()%80 <= (self.y)%80 + self.width and mario.return_xpos() + mario.return_length() == self.x :
            mario.Increment_score(50)
            self.destroy()

        if self.moveleft == True and self.y >= self.initial_y - self.leash :
            self.y = self.y - 1
        else :
            self.moveleft = False 

        if self.moveleft == False and self.y < self.initial_y + self.leash  :
            self.y = self.y + 1
        else :
            self.moveleft = True 

        # collision with mario block on it's head :
        # mushroom.destroy()
    
class Boss(Character) : 
    """ Definition of Boss enemy """  

    def __init__(self, x, y) :
        Character.__init__(self, x, y) 
        self.matrix = [[' ','L','L',' '],[' ','L','L',' '],['L','L','L','L'],['L','L','L','L'],[' ','L','L',' '],[' ','L','L',' ']]
        self.length = 6
        self.width = 4
        self.initial_y = y


    def move(self, board_object, mario) :
        if mario.return_distance() % 80 > self.y%80 :
            self.y = self.y + 2
        
        if mario.return_distance() % 80 < self.y%80 : 
            self.y = self.y - 2 

        if mario.return_distance()%80 >= self.y % 80-self.width and mario.return_distance()%80 <= (self.y)%80 + self.width and mario.return_xpos() + mario.return_length() == self.x :
            mario.Increment_score(150)
            self.destroy()

    def return_initial_y(self) :
        return self.initial_y 
        
        

class EmptyEnemy(Character) :
    """ Definition of an empty character """
    
    def __init__(self,enemy_object) :
        Character.__init__(self, enemy_object.return_xpos() , enemy_object.return_ypos()) 
        self.length = enemy_object.return_length()
        self.width = enemy_object.return_width()
        self.matrix = [[' ' for i in range(self.width)] for j in range(self.length)]
