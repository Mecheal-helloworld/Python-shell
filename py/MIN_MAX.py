import os
import sys
import time
import copy
import random
from reprint import output

MAX_oo = 65535
MIN_MAX = 65280
MIN_oo = -65535

'''
print("1111111",end="")
print("\r222222",end="")

╳〇

─━│┃┄┅┆┇┈┉┊┋┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛
├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻
┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋
═║╒╓╔╕╖╗è]╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╳
╔ ╗╝╚ ╬ ═ ╓ ╩ ┠ ┨┯ ┷┏ ┓┗ ┛┳⊥﹃﹄┌

'''
turn = 0
max_win = 0
min_win = 0
Max=" 〇"
Min=" ╳ "
empty="   "
symbols=[Max, Min, empty]
alpha=[MIN_oo,MIN_oo]
Chess_Board=[[2]*5, [2]*5, [2]*5, [2]*5, [2]*5]


def check_win(chess_board,role):
  for i in range(5):
    sign = 1
    for j in range(5):
      if chess_board[i][j]!=role:
        sign = 0
        break
    if sign:
      return True
    sign = 1
    for j in range(5):
      if chess_board[j][i]!=role:
        sign = 0
        break
    if sign:
      return True
  sign = 1
  for i in range(5):
    if chess_board[i][i]!=role:
      sign = 0
      break
  if sign:
    return True
  sign = 1
  for i in range(5):
    if chess_board[i][4-i]!=role:
      sign = 0
      break
  if sign:
    return True
  return False


def search(chess_board, role):
  value = 0
  for i in range(5):
    sign = 1
    for j in range(5):
      if chess_board[i][j]!=role and chess_board[i][j]!=2:
        sign = 0
        break
    value += sign
    sign = 1
    for j in range(5):
      if chess_board[j][i]!=role and chess_board[j][i]!=2:
        sign = 0
        break
    value += sign
  sign = 1
  for i in range(5):
    if chess_board[i][i]!=role and chess_board[i][i]!=2:
      sign = 0
      break
  value += sign
  sign = 1
  for i in range(5):
    if chess_board[i][4-i]!=role and chess_board[i][4-i]!=2:
      sign = 0
      break
  value += sign
  return value
  

def getGuess(chess_board, role):
  enemy = (role+1)%2
  if check_win(chess_board,role):
    return MAX_oo
  if check_win(chess_board,enemy):
    return MIN_oo
  myself_rate = search(chess_board,role)
  enemy_rate = search(chess_board,enemy)
  return myself_rate - enemy_rate

def MinMax(role):
  global Chess_Board
  open_list = []
  for i in range(5):
    for j in range(5):
      if Chess_Board[i][j]==2:
        new_chess_board = copy.deepcopy(Chess_Board)
        new_chess_board[i][j] = role
        open_list.append([new_chess_board,MAX_oo])
  if len(open_list)==0:
    return MIN_MAX
  for index, min_node in enumerate(open_list):
    alpha_beta_cut = False
    new_Chess_board = min_node[0]
    beta = min_node[1]
    for min_i in range(5):
      for min_j in range(5):
        if new_Chess_board[min_i][min_j] == 2:
          min_chess_board = copy.deepcopy(new_Chess_board)
          min_chess_board[min_i][min_j] = (role+1)%2
          guess = getGuess(min_chess_board, role)
          beta = min(beta,guess)
          open_list[index][1] = beta
          if beta <= alpha[role]:
            alpha_beta_cut = True
            break
      if alpha_beta_cut:
        break
    if alpha_beta_cut:
      continue
    alpha[role] = max(alpha[role],beta)
  open_list.sort(key=lambda x:x[1],reverse=True)
  #print(open_list)
  status = open_list[0]
  Chess_Board = status[0]
  time.sleep(0.5)
  if check_win(Chess_Board,role) == MAX_oo:
    return 1
  else:
    return 0

output_list=[
  "┌───┬───┬───┬───┬───┐",
  "│{}│{}│{}│{}│{}│",
  "├───┼───┼───┼───┼───┤",
  "│{}│{}│{}│{}│{}│",
  "├───┼───┼───┼───┼───┤",
  "│{}│{}│{}│{}│{}│",
  "├───┼───┼───┼───┼───┤",
  "│{}│{}│{}│{}│{}│",
  "├───┼───┼───┼───┼───┤",
  "│{}│{}│{}│{}│{}│",
  "└───┴───┴───┴───┴───┘"
  ]

with output(output_type='list', initial_len=11) as out:
  while True:
    #with output(output_type='list', initial_len=11) as out:
    for index,value in enumerate(output_list):
      if index%2 == 1:
        vals = [symbols[x] for x in Chess_Board[index//2]]
        out[index]=value.format(*vals)
      else:
        out[index]=value
    if max_win != 0 or min_win != 0:
      break
    turn_win = MinMax(turn)
    max_win = turn_win if turn==0 else 0
    min_win = turn_win if turn==1 else 0
    turn = (turn+1)%2
if max_win==1:
  print("Max win!!!")
if min_win==1:
  print("Min win!!!")
if min_win==MIN_MAX or max_win==MIN_MAX:
  print("It ends in a draw!!!")