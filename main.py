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
    cube[2] = temp
    clockwise(cube[1])
    counterclockwise(cube[3])
    
def rotate_x_prime(): # x' rotation
    rotate_x()
    rotate_x()
    rotate_x()

def rotate_y(): # y rotation
    # Front --> Right --> Back --> Left 0 1 2 3
    temp = clockwise(cube[0])
    cube[0] = cube[1]
    cube[1] = cube[2]
    cube[2] = cube[3] 
    cube[3] = temp
    clockwise(cube[4])
    counterclockwise(cube[5])

def rotate_y_prime(): # y' rotation
    rotate_y()
    rotate_y()
    rotate_y()

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

def rotate_z_prime(): # z' rotation
    rotate_z()
    rotate_z()
    rotate_z()
    
def push_right(): # R -- Note: Every other push/pull move is defined based off this function + rotations
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
    rotate_z()
    rotate_z()
    push_right()
    rotate_z()
    rotate_z()

def pull_left(): # L'
    push_left()
    push_left()
    push_left()

def push_up(): # U
    rotate_z()
    push_right()
    rotate_z_prime

def pull_up(): # U'
    push_up()
    push_up()
    push_up()

def push_front(): # F
    rotate_y()
    push_left()
    rotate_y_prime()

def pull_front(): # F'
    push_front()
    push_front()
    push_front()

def push_down(): # D
    rotate_x()
    rotate_x()
    push_up()
    rotate_x()
    rotate_x()

def pull_down(): # D'
    push_down()
    push_down()
    push_down()

def push_back(): # B
    rotate_y()
    push_right()
    rotate_y_prime()

def pull_back(): # B'
    push_back()
    push_back()
    push_back()

def m_slice(): # M
    pass

def m_slice_prime(): # M' this is the one that goes the same direction with R... it's weird lol
    pass

# probably will define the S and E layers... but who uses those anyways?




# ========== TESTING ========== # 
rotate_x()
rotate_x()
rotate_x()
rotate_x()


