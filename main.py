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

def rotate_x(): # x rotation
    # Top --> Front --> Bottom --> Back --> Top 4 0 5 2
    temp = cube[4]
    cube[4] = cube[0]
    cube[0] = cube[5]
    cube[5] = cube[2]
    cube[2] = cube[4]
    clockwise(1)
    counterclockwise(3)
    

def rotate_y(): # y rotation
    temp = clockwise(cube[0])
    cube[0] = cube[1]
    cube[1] = cube[2]
    cube[2] = cube[3] 
    cube[3] = temp
    clockwise(cube[4])
    counterclockwise(cube[5])

def rotate_z(): # z rotation
    clockwise(cube[0])
    clockwise(cube[1])
    counterclockwise(cube[2]) # back face is reflected upside down
    clockwise(cube[3])
    clockwise(cube[4])
    clockwise(cube[5])
    # Top --> Right --> Bottom --> Left --> Top 4 1 5 3
    temp = cube[4]
    cube[4] = cube[3]
    cube[3] = cube[5]
    cube[5] = cube[1]
    cube[1] = temp
    
def push_right(): # R
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

def pull_right(): # R'
    push_right()
    push_right()
    push_right()

def push_left(): # L
    pass

def pull_left(): # L'
    pass

def push_up(): # U
    pass

def pull_up(): # U'
    pass

def push_front(): # F
    pass

def pull_front(): # F'
    pass

def push_down(): # D
    pass

def pull_down(): # D'
    pass

def push_back(): # B
    pass

def pull_down(): # B'
    pass


# ========== UI ========== # 


# ========== TESTING ========== # 
rotate_y()


print(cube)