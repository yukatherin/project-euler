
import pandas as pd
import numpy as np
import itertools


class SquareGrid():
    def __init__(self, M, i_moves, j_moves):
        assert M.shape[0]==M.shape[1]
        self.M=M
        self.n = M.shape[0]
        self.i_moves = i_moves 
        self.j_moves = j_moves

    def in_grid(self,i,j):
        return (i>=0 and i<self.n and j>=0 and j<self.n)

    def get_adjacencies(self,(i,j)):
        if i==j==self.n:
            return [(i, self.n-1) for i in range(self.n)]
        adj = list()
        for delta_i in self.i_moves:
            if (self.in_grid(i+delta_i, j)):
                adj.append((i+delta_i, j))
        for delta_j in self.j_moves:
            if (self.in_grid(i,j+delta_j)):
                adj.append((i,j+delta_j))
        return adj

def test_get_adjacencies():
    gr = SquareGrid(np.identity(3))
    print gr.get_adjacencies((0,0))
    print gr.get_adjacencies((0,1))
    print gr.get_adjacencies((0,2))
    print gr.get_adjacencies((2,1))
    print gr.get_adjacencies((3,3))

def dijkstras(gr, source_pos, unvisited_queue, source_val):
    dist = dict()
    previous = dict()
    dist[source_pos]= source_val
    while unvisited_queue:
        u = min(unvisited_queue, key=lambda x:dist.get(x,np.inf))
        unvisited_queue.remove(u)
        for v in gr.get_adjacencies(u):
            alt_dist = dist[u] + gr.M[v]
            if alt_dist < dist.get(v,np.inf):
                dist[v] = alt_dist
                previous[v] = u
    return dist, previous








