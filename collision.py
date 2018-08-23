""" Controllers for collision detectors """
from colorama import Fore

def CollisionBricks(new_xpos, new_ypos, clength, cwidth, board_object) :
    """ Function that checks and controls collisions """
    x = new_xpos
    y = new_ypos
    board_matrix = board_object.ReturnMatrixBoard()
    length = clength
    width = cwidth

    for i in range(x,x + length) :
        for j in range( y, y+width) :
            if board_matrix[i][j%80] == '=':
                return 2
            if board_matrix[i][(j+1)%80] == '?':
                return 3
            if board_matrix[i][j%80] != ' ' and board_matrix[i][j%80] != '_' and  board_matrix[i][j%80] != '/' and board_matrix[i][j%80] != '\\' and board_matrix[i][j%80] != 'w' and board_matrix[i][j%80] != Fore.BLUE + 'w' + Fore.RESET and board_matrix[i][j%80]!='$' and board_matrix[i][j%80] != Fore.YELLOW + '$' + Fore.RESET :
                return 1

    return 0 