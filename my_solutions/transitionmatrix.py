from __future__ import division
import numpy as np

def index(row, col, k=5):
    return k*row+col;

def generateTransitionMatrix(absorb_row, k=5):
    # The transition matrix gets flipped every time so that the absorbing states are always row 0
    P = np.zeros((k**2, k**2));
    for row in range(k):
        for col in range(k):
            idx = index(row,col);
            #absorbing:
            if (row==0) and (col in absorb_row):
                P[idx][idx] = 1;
                continue;
            #corner cases:
            if (row==0) and (col==0):
                P[idx][[index(row,col+1),index(row+1,col)]]=1/2;
                continue;
            if (row==0) and (col==4):
                P[idx][[index(row,col-1),index(row+1,col)]]=1/2;
                continue;
            if (row==4) and (col==0):
                P[idx][[index(row,col+1),index(row-1, col)]] = 1/2;
                continue;
            if (row==4) and (col==4):
                P[idx][[index(row,col-1),index(row-1,col)]]=1/2;
                continue;
            #edge cases:
            if (row==0):
                P[idx][[index(row,col+1),index(row,col-1),index(row+1,col)]]=1/3;
                continue;
            if (row==4):
                P[idx][[index(row,col+1),index(row,col-1),index(row-1,col)]]=1/3;
                continue;
            if (col==0):
                P[idx][[index(row+1,col),index(row-1,col),index(row,col+1)]]=1/3;
                continue;
            if (col==4):
                P[idx][[index(row+1,col), index(row-1,col), index(row,col-1)]]=1/3;
                continue;
            P[idx][[index(row+1,col),index(row-1,col),index(row,col+1),index(row,col-1)]]=1/4;
    return P;
