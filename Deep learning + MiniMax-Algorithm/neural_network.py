from keras.models import Model
from keras.layers import Dense,Flatten,Reshape
from keras.layers.convolutional import Conv2D
from keras.callbacks import EarlyStopping
from keras.models import load_model
from board_conversion import *
import chess

class NeuralNetwork():
    '''
    def __init__(self):
        self.optimizer = 'Adam'
        self.loss = 'categorical_crossentropy'
        
    def define(self):
        input_layer= Input(shape=(8,8,12))
        x = Conv2D(filters=64,kernel_size = 2,strides = (2,2))(input_layer)
        x = Conv2D(filters=128,kernel_size=2,strides = (2,2))(x)
        x = Conv2D(filters=256,kernel_size=2,strides = (2,2))(x)
        x = Flatten()(x)

        x = Dense(4096,activation = 'softmax')(x)
        output = Reshape((1,64,64))(x)

        model = Model(inputs=input_layer,outputs=output)
        model.compile(optimizer = self.optimzier,loss = self.loss)
        self.model = model
    '''
        
    def train(self,X,y,epochs,EarlyStop = True):
        if EarlyStop:
            es = EarlyStopping(monitor='loss')

        self.model.fit(X,y,epochs = epochs,callbacks = [es])
        self.model.save('chess_model')
        

    def predict(self,board,side):
        model = load_model("chess_model")
        translated = translate_board(board)

        move_matrix = model(translated.reshape(1,8,8,12))[0][0]
        move_matrix = filter_legal_moves(board,move_matrix)
        move= np.unravel_index(np.argmax(move_matrix, axis=None), move_matrix.shape)
        move = chess.Move(move[0],move[1])
        return move,1