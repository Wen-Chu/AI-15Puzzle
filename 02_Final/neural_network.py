import numpy as np
import time
import random
from board import Board
from intelligence import a_star, manhattan_heuristic
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
import time

np.random.seed(1)
# 訓練模型
# model = Sequential()
# model.add(Dense(units=512, input_dim=256, activation='relu'))
# model.add(Dropout(0.1))
# model.add(Dense(units=1024, activation='relu'))
# model.add(Dropout(0.1))
# model.add(Dense(units=512, activation='relu'))
# model.add(Dense(units=1, activation='linear'))
# model.compile(optimizer='adam', loss='mse')

# 已訓練好的模型
model = load_model("neural_network - 512x1024x512 - 35.h5") 


def transform(state):
    vector_state = state.flatten()

    output = []
    for i in range(16):
        one_hot = np.zeros(16)
        one_hot[np.argwhere(vector_state == i)] = 1
        output.append(one_hot)

    return np.array(output).flatten().reshape(256)


def training_data(n_boards, n_scrambles, heuristic):
    states = []
    values = []
    boards = []
    for _ in range(n_boards):
        this_board = Board(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]))
        this_board.scramble(n_scrambles)
        boards.append(this_board)
    for board in boards:
        solution,_ = a_star(board, heuristic)
        solution = solution[:-1]
        length = len(solution)
        for i,state in enumerate(solution):
            states.append(state.get_board())
            values.append(length - i)
    for i,state in enumerate(states):
        states[i] = transform(state)
    return np.array(states), np.array(values)


def neural_heuristic(board):
    return model.predict(transform(board.get_board()).reshape((1,256)))


def train(max_scrambles, nn_dim_string):
    complete_x = []
    complete_y = []
    for i in range(1, max_scrambles+1):
        t0 = time.time()
        x_train, y_train = training_data(200, i, neural_heuristic)
        for x in x_train:
            complete_x.append(x)
        for y in y_train:
            complete_y.append(y)
        model.fit(np.array(complete_x), np.array(complete_y), epochs=25)
        if i % 5 == 0:
            model.save("neural_network - {} - {}.h5".format(nn_dim_string, i))
        print("迭代完成了 {}/{}".format(i, max_scrambles))
        print("本次迭代時間一共:", time.time() - t0)


if __name__ == "__main__":

    train(35, "512x1024x512")
