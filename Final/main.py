import os
import random
import numpy as np
from neural_network import neural_heuristic, transform 
from board import Board
from intelligence import a_star,num_print, manhattan_heuristic, Judge_Whether_Have_A_Solution
import time

def main(epoch):
  epoch = str(epoch)
  gamelist=[]
  num = input("num:") 
  numlist = num.split(',') 
  for i in range(0,16):
      gamelist.append(int(numlist[i]))
      gamelist[i] += 1
      if(gamelist[i] == 16):
          gamelist[i]=0
  game = gamelist
  goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
  game = np.array(game).reshape(4,4)
  game = Board(game)


  if not Judge_Whether_Have_A_Solution(game.board.flatten(), goal):
    return 'fail'
  else:
    game.board = game.board -1
    for i in range(4):
          for j in range(4):
              if(game.board[i][j] == -1):
                  game.board[i][j] = 15
    game.board = game.board +1
    for i in range(4):
          for j in range(4):
              if(game.board[i][j] == 16):
                  game.board[i][j] = 0

  neural_start = time.time()
  path = a_star(game, neural_heuristic)
  neural_end_time = time.time()
  info = "\nNeural time {}\nMove: {} ".format(neural_end_time-neural_start, len(path)-1) 
  strs = ''
  for i, board in enumerate(path):
      numlist=[]
      board.board = board.board -1
      for p in range(4):
          for k in range(4):
              if(board.board[p][k] == -1):
                 board.board[p][k] = 15
      strs += "Step {}：\n {}\n".format(i, board.board.flatten())
   
  strs += info
  print("\n"+strs)
  num_print()

for epoch in range(1):
  while main(epoch) == 'fail':
    continue 