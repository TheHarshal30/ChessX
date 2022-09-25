from neural_network import *  
from minimax import *
import random

class ChessEngine():
    
    def __init__(self,algorithms = [MinMaxTree,NeuralNetwork]):
        self.algorithms = algorithms
    
    def generate_move(self,board,side):
        moves = []
        effes = []
        for algorithm in self.algorithms:
            move,effe = algorithm().predict(board,side)
            moves.append(move)
            effes.append(effe)
            
        effes = np.array(effes)
        idx = np.argmax(effes)
        
        final_move = moves[idx]
        print(self.algorithms[idx])
        print(effes)
        return final_move
            