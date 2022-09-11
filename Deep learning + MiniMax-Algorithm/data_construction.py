import pickle
import chess
from board_conversion import *
import os
os.chdir('C:\Users\v_sim\Desktop\Files\Data')
with open('magnus_moves.pkl', 'rb') as f:
    moves = pickle.load(f)

dataset = []
counter =0
for game in moves:
    board = chess.Board()
    counter+=1
    print('GAME:',counter)
    for move in game:
        data_board = translate_board(board)
        data_move = translate_move(move)
        dataset.append([data_board,data_move])
        board.push(move)
        
with open('dataset.pkl', 'wb') as f:
    pickle.dump(np.array(dataset), f)
