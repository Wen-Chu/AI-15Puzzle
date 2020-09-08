import numpy as np
from utils import PriorityQueue, Node
import time

class Board:

    def __init__(self, board=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])):
        self.board = board
        self.blank_position = np.argwhere(self.board == 0)[0]

    def move(self, direction):
        x, y = self.blank_position 

        if direction == 1:
            # moving right
            if direction in self.legal_moves():
                self.board[x][y] = self.board[x][y + 1]
                self.board[x][y + 1] = 0
                self.blank_position[1] += 1

        elif direction == 2:
            # moving up
            if direction in self.legal_moves():
                self.board[x][y] = self.board[x - 1][y]
                self.board[x - 1][y] = 0
                self.blank_position[0] -= 1

        elif direction == 3:
            # moving left
            if direction in self.legal_moves():
                self.board[x][y] = self.board[x][y - 1]
                self.board[x][y - 1] = 0
                self.blank_position[1] -= 1

        elif direction == 4:
            # moving down
            if direction in self.legal_moves():
                self.board[x][y] = self.board[x + 1][y]
                self.board[x + 1][y] = 0
                self.blank_position[0] += 1

    def get_board(self):
        return self.board

    def scramble(self, n=1000):
        def inverse(x):
            return ((x + 5) % 4) + 1
        last_inverse = 0
        for _ in range(n):
            move = np.random.choice([action for action in self.legal_moves() if action != last_inverse])
            self.move(move)
            last_inverse = inverse(move)


    def is_solved(self):
        if (self.board == np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])).all():
            return True
        return False

    def legal_moves(self):
        moves = []
        if self.blank_position[1] != 3:
            moves.append(1)
        if self.blank_position[0] != 0:
            moves.append(2)
        if self.blank_position[1] != 0:
            moves.append(3)
        if self.blank_position[0] != 3:
            moves.append(4)
        return moves


    def forecast(self, action):
        new_board = Board(np.copy(self.board))
        new_board.move(action)
        return new_board
