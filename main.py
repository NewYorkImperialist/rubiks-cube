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

def clockwise(face): # not an actual move, just a helper move to clean code
    temp = face.copy()
    face[0] = temp[6]
    face[1] = temp[3]
    face[2] = temp[0]
    face[3] = temp[7]
    # face[4] stays the same (center)
    face[5] = temp[1]
    face[6] = temp[8]
    face[7] = temp[5]
    face[8] = temp[2]

def counterclockwise(face): # not an actual move, just a helper move to clean code
    clockwise(face)
    clockwise(face)
    clockwise(face)

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
    clockwise(cube[1])

def pull_right():
    push_right()
    push_right()
    push_right()

def rotate_x():
    pass

def rotate_y():
    temp = cube[0]
    cube[0] = cube[1]
    cube[1] = cube[2]
    cube[2] = cube[3] 
    cube[3] = temp

def rotate_z():
    pass

# ========== UI ========== # 


# ========== TESTING ========== # 
rotate_y()
rotate_y()
rotate_y()
rotate_y()

print(cube)