""" Controllers for collision detectors """

# def CollisionFloor(character_object  , board_object ) :
#     x = character_object.return_xpos()
#     y = character_object.return_ypos()
#     board_matrix = board_object.return_matrix()
#     x_length = character_object.return_length()
#     y_width = character_object.return_width()

#     for i in range(0,4) :
#         if board_object[x + x_length][y + i] in ['T', '|'] :
#             return 1
#         else :
#             return 0


def CollisionBricks(new_xpos, new_ypos, clength, cwidth, board_object) :
    x = new_xpos
    y = new_ypos
    board_matrix = board_object.ReturnMatrixBoard()
    length = clength
    width = cwidth

    for i in range(x,x + length) :
        for j in range( y, y+width) :
            if board_matrix[i][j%80] != ' ' and board_matrix[i][j%80] != '_' and board_matrix[i][j%80] != '/' and board_matrix[i][j%80] !='\\' and board_matrix[i][j%80] != 'w' and board_matrix[i][j%80] != '=':
                return 1
            if board_matrix[i][j%80] == '=':
                return 2

    return 0 