""" Bricks """

import random

class Brick :
    """ Defining a basic brick """

    def __init__(self, x, y) :
        """ Initializing  Bricks """
        self.x = x 
        self.y = y
        self.matrix = None 
        self.breakable = True 
        self.destroyed = False 
        self.special = False
        self.length = None
        self.width = None
    def return_matrix(self) :
        """ Returing matrix """
        return self.matrix 

    def return_xpos(self) :
        """ Returning x coordinate of brick """
        return self.x 

    def return_ypos(self) :
        """ Returning y coordinate of brick """
        return self.y

    def return_length(self) :
        return self.length
        
    def return_width(self) :
        return self.width

    def setPos(self, x, y):
        self.x = x
        self.y = y


class Ground_Brick(Brick):
    """ Brick for floor """

    def __init__(self,x, y) :
        """ Initializing Ground Brick """
        Brick.__init__(self, x, y)
        self.length = 3
        self.width = 4
        self.matrix = [['T','T','T','|'],['%','%','%','|'],['W','W','W','|']]  
        self.breakable = False


class Special_Brick(Brick) :
    """ Brick for a star """ 

    def __init__(self, x, y) :
        """ Initializing Special Brick """
        Brick.__init__(self,x, y)
        self.length = 2
        self.width = 4
        self.matrix = [["|","?","?","|"],["|","?","?","|"]]
        self.breakable = False
        self.special = True

    def hit(self) :
        """ Changing brick once hit """
        self.matrix = [["|","x","x","|"],["|","x","x","|"]]
        self.special = False

class EmptyGround_Brick(Brick) :
    """ Empty brick for ground """

    def __init__(self, x, y) :
        """ Initializing Empty Ground block """
        Brick.__init__(self, x, y)
        self.length = 3
        self.width = 4
        self.matrix = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
        self.breakable = False
        self.special = False


class Air_Brick(Brick) :
    """ Floating brick """

    def __init__(self,x,y) :
        Brick.__init__(self,x,y)
        self.matrix = [['|','x','x','|'],['|','x','x','|']]
        self.length = 2
        self.width = 4
        self.breakable = False
        self.special = False



class Pipe(Brick) :
    """ Pipe """

    def __init__(self,x,y) :
        
        a = random.randrange(3, 9, 1)
        Brick.__init__(self,x+(9-a-1),y)
        self.matrix = []
        self.matrix.append(['|','|',':',':',':',':',':',':',':',':',':',':','|','|'])
        for i in range(a) :
            self.matrix.append([' ',' ','|','|',':',':',':',':',':',':','|','|',' ',' '])
        self.length = 2
        self.width = 4
        self.breakable = False
        self.special = False


class Sun(Brick) :
    """ Sun """

    def __init__(self, x,y) :

        Brick.__init__(self,x,y)
        self.matrix = [ [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', '0', '0', '0', '0', '0', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', ' '],
                        ['-', '-', '0', '0', '0', '0', '|', '0', '0', '0', '0', '-', '-'],
                        [' ', ' ', ' ', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', '0', '0', '0', '0', '0', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' '],]
        self.width = 13
        self.length = 9
        self.breakable = False
        self.special = False
 
class Hills(Brick) :
    """ Hills """

    def __init__(self, x, y) :

        Brick.__init__(self,x,y) 
        self.width = 80
        self.length = 18
        self.matrix = []
        Hilareous =[    
         "                        wwwwwwwwwwwwwwwwwwwwwwww                              ",
         "                       /                        \_____                        ",
         "                ______/                               \                       ",
         "               /                                       \                      ",
         "              /                                         \                     ",
         "             /                                           \                    ",
         "            /                                             \                   ",
         "           /                                               \                  ",
         "          /                                                 \wwwwwwwww        ",
         "         /                                                            \       ",
         "        /                                                              \      ",
         "      _/                                                                \     ",
         "\    /                                                                   \    ",
         " \  /                                                                     \___",
         "  \/                                                                          ",
         "  /                                                                           ",
         " /                                                                            ",
         "/                                                                             "
         ]
        for i in range(len(Hilareous)):
            self.matrix.append([])
            for j in range(len(Hilareous[1])):
                self.matrix[i].append(Hilareous[i][j])


class Waterfall_Bricks(Brick) :
    """ Waterfall bricks """

    def __init__(self,x,y) :

        Brick.__init__(self,x,y)
        self.length = 29
        self.width = 30
        self.matrix = [['w' for i in range(self.width)] for j in range(self.length)]

class Beware(Brick) :
    """ Beware signboard """

    def __init__(self, x, y) :

        Brick.__init__(self,x,y)
        self.matrix = [['-','-','-','-','-','-','-','-','-','-','-'],['|',' ','B','E','W','A','R','E','!',' ','|'],['|',' ','L','U','I','G','I','\'','S',' ','|'],['|',' ',' ','L','A','I','R',' ',' ',' ','|'],['-','-','-','-','-','-','-','-','-','-','-'],[' ',' ',' ',' ','|','|','|',' ',' ',' ',' ']]
        self.length = 6
        self.width = 11

class PrincessHere(Brick) :
    """ Princess signboard """

    def __init__(self, x, y) :

        Brick.__init__(self,x,y)
        self.matrix = [['-','-','-','-','-','-','-','-','-','-','-'],['|','P','R','I','N','C','E','S','S',' ','|'],['|',' ',' ',' ','H','E','R','E','!',' ','|'],['|',' ',' ','J','U','M','P','!',' ',' ','|'],['-','-','-','-','-','-','-','-','-','-','-'],[' ',' ',' ',' ','|','|','|',' ',' ',' ',' ']]
        self.length = 6
        self.width = 11
