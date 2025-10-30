import pygame as pg

# ========== LOGIC ========== # 

G = 0
R = 1
B = 2
O = 3
W = 4
Y = 5

cube = [
    [G, G, G, G, G, G, G, G, G],  # Front face
    [R, R, R, R, R, R, R, R, R],  # Right face
    [B, B, B, B, B, B, B, B, B],  # Back face
    [O, O, O, O, O, O, O, O, O],  # Left face
    [W, W, W, W, W, W, W, W, W],  # Top face
    [Y, Y, Y, Y, Y, Y, Y, Y, Y]   # Bottom face
]

def push_right(): 
    temp = [
        cube[0][2], 
        cube[0][5], 
        cube[0][8]
        ]
    cube[0][2] = cube[5][2]
    cube[0][5] = cube[5][5]
    cube[0][8] = cube[5][8]

    cube[5][2] = cube[2][2]
    cube[5][5] = cube[2][5]
    cube[5][8] = cube[2][8]

    cube[2][2] = cube[4][2]
    cube[2][5] = cube[4][5]
    cube[2][8] = cube[4][8]

    cube[4][2] = temp[0]
    cube[4][5] = temp[1]
    cube[4][8] = temp[2]

# Rotate Right Face
    temp = [
        cube[1][0], 
        cube[1][1], 
        cube[1][2],
        cube[1][3], 
        cube[1][4], 
        cube[1][5],
        cube[1][6], 
        cube[1][7], 
        cube[1][8]
        ]
    cube[1][0] = temp[6]
    cube[1][1] = temp[3]
    cube[1][2] = temp[0]
    cube[1][3] = temp[7]
    cube[1][5] = temp[1]
    cube[1][6] = temp[8]
    cube[1][7] = temp[5]
    cube[1][8] = temp[2]

def pull_right():
    push_right()
    push_right()
    push_right()

def rotate_x():
    pass

def rotate_y():
    pass

def rotate_z():
    pass

# ========== UI ========== # 


# ========== TESTING ========== # 
push_right()
push_right()
push_right()
push_right()


print(cube)