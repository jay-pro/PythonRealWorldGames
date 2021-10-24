import os
import sys
import cfg 
import random #pip install random hoặc random2
import pygame

def isGameOver(board, size):
    assert isinstance(size, int)
    num_cells = size*size
    for i in range(num_cells):
        if board[i] != i: False
    return True

#Move to the right
def moveR(board, blank_cell_idx, num_cols):
    if blank_cell_idx%num_cols ==0: return blank_cell_idx
    board[blank_cell_idx-1],board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-1]
    return blank_cell_idx-1
#Move to the left
def moveL(board, blank_cell_idx, num_cols):
    if (blank_cell_idx+1)%num_cols ==0: return blank_cell_idx
    board[blank_cell_idx+1],board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+1]
    return blank_cell_idx+1
#Move down
def moveD(board, blank_cell_idx, num_cols):
    if blank_cell_idx < num_cols ==0: return blank_cell_idx
    board[blank_cell_idx-num_cols],board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-num_cols]
    return blank_cell_idx-num_cols


fff




if __name__ == '__main':
    main()
