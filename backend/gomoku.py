import math
import time
from TicTacToeAi import *
import utils 

def ai_move(ai):
    start_time = time.time()
    ai.alphaBetaPruning(ai.depth, ai.boardValue, ai.nextBound, -math.inf, math.inf, True)
    end_time = time.time()
    print('Nc đi: ', end_time - start_time)
    
    if ai.isValid(ai.currentI, ai.currentJ):
        move_i, move_j = ai.currentI, ai.currentJ
        print(move_i, move_j)
        ai.updateBound(move_i, move_j, ai.nextBound)
        
    else:
        print('Lỗi: i và j không hợp lệ: ', ai.currentI, ai.currentJ)
        ai.updateBound(ai.currentI, ai.currentJ, ai.nextBound)
        bound_sorted = sorted(ai.nextBound.items(), key=lambda el: el[1], reverse=True)
        pos = bound_sorted[0][0]
        move_i = pos[0]
        move_j = pos[1]
        ai.currentI, ai.currentJ = move_i, move_j
        
        print(move_i, move_j)
    
    return (move_i, move_j)
    