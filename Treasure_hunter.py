import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore") #
NORMAL = -0.50
TREASURE = 10
OBSTICLE = 0
OPPONENT = -10
def Map(M, path=None):
    cmap = mpl.colors.ListedColormap(['red', 'black', 'aqua','lightgrey'])
    M_copy = np.copy(M)



    minimum = int(np.amin(M))-1
    M_copy[abs(M_copy - NORMAL) < .01]   = minimum-1
    M_copy[abs(M_copy - TREASURE) < .01] = minimum-2
    M_copy[abs(M_copy - OBSTICLE) < .01] = minimum-3
    M_copy[abs(M_copy - OPPONENT) < .01] = minimum-4

    M_copy[M_copy is minimum-1] = 0
    M_copy[M_copy is minimum-2] = 1
    M_copy[M_copy is minimum-3] = 2
    M_copy[M_copy is minimum-4] = 3


    plt.pcolormesh(M_copy, cmap=cmap)

    lightgrey_patch = mpl.patches.Patch(color='lightgrey', label='Normal Ground')
    aqua_patch = mpl.patches.Patch(color='aqua', label='Treasure')
    black_patch = mpl.patches.Patch(color='black', label='Obsticle')
    red_patch = mpl.patches.Patch(color='red', label='Opponent')
    handles = [lightgrey_patch, aqua_patch, black_patch, red_patch]
    plt.subplots_adjust(right=0.7)
    if path is not None:
        plt.plot(*path.T, color='yellow')
        red_patch = mpl.patches.Patch(color='yellow', label='Path')
        handles.append(red_patch)
    plt.legend(handles=handles ,loc='upper left', bbox_to_anchor=(1.04,1), borderaxespad=0)
    plt.axes().set_aspect('equal') #set the x and y axes to the same scale
    plt.xticks(np.arange(0, len(M), 1))
    plt.yticks(np.arange(0, len(M[0]), 1))
    plt.grid()
    plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top


height = 15
width = 15
M = np.full((width,height), NORMAL)
shape = M.shape
M = M.flatten()
np.random.seed(2)
treasureIndecies = np.random.choice(M.size, size=20)
M[treasureIndecies] = TREASURE
M = M.reshape(shape)

M[1][0] = TREASURE; M[2][1] = TREASURE; M[3][2] = TREASURE; M[4][3] = TREASURE

M[5,1] = OBSTICLE; M[6,1] = OBSTICLE; M[7,1] = OBSTICLE; M[8,1] = OBSTICLE
M[11,1] = OBSTICLE; M[12,1] = OBSTICLE; M[13,1] = OBSTICLE; M[14,1] = OBSTICLE
M[11,2] = OBSTICLE; M[11,3] = OBSTICLE; M[11,4] = OBSTICLE; M[11,5] = OBSTICLE

M[10,4] = OPPONENT; M[4,3] = OPPONENT; M[5,10] = OPPONENT; M[14,4] = OPPONENT

M[0,0] = NORMAL
M[14,14] = TREASURE


def move_direction(state, move):

    if move == 0:
        return state - width
    elif move == 1:
        return state + 1
    elif move == 2:
        return state + width
    elif move == 3:
        return state - 1
    else:
        raise Exception



def possible_moves(s, M):

    poss_moves = []
    valid_moves = []
    x, y = stateToXY(s)
    if y > 0:
        valid_moves.append(0)
    if x < len(M[0]) - 1:
        valid_moves.append(1)
    if y < len(M) - 1:
        valid_moves.append(2)
    if x > 0:
        valid_moves.append(3)
    for move in valid_moves:
            poss_state = move_direction(s,move)
            x,y = stateToXY(poss_state)
            if M[y][x] != OBSTICLE: poss_moves.append(move)
    return poss_moves
def best_next_move(s, M, Q):

    poss_next_moves = possible_moves(s, M)
    if len(poss_next_moves) == 0:
            return None
    max_m = poss_next_moves[0]
    max_q = Q[s][max_m]

    for move in poss_next_moves[1::]:
        if(Q[s][move] > max_q):
            max_q, max_m = Q[s][move], move
    return max_m

def next_move(s, M, Q):
    '''
    Gets the next move for either exploring or exploiting
    '''
    poss_next_moves = get_poss_moves(s, M)
    if len(poss_next_moves) == 0:
            return None
    if np.random.rand() <= exploitation_probability:
        return get_best_next_move(s, M, Q)
    else:
        next_move = \
            poss_next_moves[np.random.randint(0,\
            len(poss_next_moves))]
        return next_move


def stateToPos(s):
    return s % width, s // width
def PosToState(x,y):
    return y*width+x


def move(start, goal, Q, M, max_steps):

    M_copy = np.copy(M)

    steps = 1
    curr = start
    curr_x, curr_y = stateToXY(curr)
    points = M_copy[curr_y][curr_x]
    M_copy[curr_y][curr_x] = OBSTICLE
    print(str((curr_x,curr_y)), end="")
    path = [[.5,.5]]
    while curr != goal and steps < max_steps:
        next_m = next_move(curr, M_copy, Q)
        if next_m is None:
            break
        next = move_direction(curr,next_m)
        curr_x, curr_y = stateToXY(curr)
        x, y = stateToXY(next)
        path.append([x+.5,y+.5])
        print("->" + str((x,y)), end="")
        points += M_copy[y,x]
        M_copy[y][x] = OBSTICLE

        curr = next
        steps += 1

    return np.array(path),point)

start_state = 0
state_count = M.size
final_state = state_count - 1
move_options = 4
gamma = .5
lrn_rate = .2
max_epochs = 1000
max_steps = 100
exploitation_probability = .8

Q = np.zeros(shape=[state_count,move_options], dtype=np.float32)  # Quality
train(M, Q, gamma, lrn_rate, final_state, state_count, max_epochs, 0, max_steps)


print("Path from", stateToPos(start_state), "to", stateToPos(final_state))
path,points = walk(start_state, final_state, Q, M, max_steps)

Map(M,path)
print("Total rewards for path is:", points)



Q = np.zeros(shape=[state_count,move_options], dtype=np.float32)
train(M, Q, gamma, lrn_rate, final_state, state_count, max_epochs, 0, max_steps)
print("Path from", stateToPos(start_state), "to", stateToPos(final_state))
path,points = walk(start_state, final_state, Q, M, max_steps)
Map(M,path)
print("\nTotal rewards for path is:", points)



M = np.full((width,height), NORMAL)
shape = M.shape
M = M.flatten()
treasureIndecies = np.random.choice(M.size, size=15)
obsticleIndecies = np.random.choice(M.size, size=20)
opponentIndecies = np.random.choice(M.size, size=5)

M[treasureIndecies] = TREASURE
M[obsticleIndecies] = OBSTICLE
M[opponentIndecies] = OPPONENT

M = M.reshape(shape)

M[0,0] = NORMAL
M[14,14] = TREASURE


Q = np.zeros(shape=[state_count,move_options], dtype=np.float32)
train(M, Q, gamma, lrn_rate, final_state, state_count, max_epochs, 0, max_steps)
print("Path from", stateToPos(start_state), "to", stateToPos(final_state))
path,points = walk(start_state, final_state, Q, M, max_steps)
Map(M,path)
print("\nTotal rewards for path is:", points)
