
import pandas as pd
import numpy as np
import itertools
from collections import defaultdict

# strategy, walk back from magic node at (n,n)

class SquareGrid():
    def __init__(self, M):
        assert M.shape[0]==M.shape[1]
        self.M=M
        self.n = M.shape[0]
        self.i_moves = [-1]
        self.j_moves = [-1,1]

    def in_grid(self,i,j):
        return (i>=0 and i<self.n and j>=0 and j<self.n)

    def get_adjacencies(self,(i,j)):
        if i==j==self.n:
            return [(self.n-1, j) for j in range(self.n)]
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

def dijkstras(gr, source_pos, unvisited_queue):
    dist = dict()
    previous = defaultdict(lambda:None)
    dist[source_pos]= 0
    while unvisited_queue:
        u = min(unvisited_queue, key=lambda x:dist.get(x,np.inf))
        unvisited_queue.remove(u)
        for v in gr.get_adjacencies(u):
            alt_dist = dist[u] + gr.M[v]
            if alt_dist < dist.get(v,np.inf):
                dist[v]=alt_dist
                previous[v] = u
    return dist, previous


def findShortestPath(gr):
    magic_end_pos = (gr.n, gr.n)
    unvisited_queue = set((i,j) for i,j in itertools.product(range(gr.n), range(gr.n)))
    unvisited_queue.add(magic_end_pos)
    dist, previous = dijkstras(gr, magic_end_pos, unvisited_queue)
    grid_min = min([dist[0,j] for j in range(gr.n)])
    return grid_min


def p82():

    try:
        M = np.array(pd.read_csv('p082_matrix.txt', header=None))
    except IOError:
        print 'cannot find matrix file'
        return
    grid = SquareGrid(M)
    print findShortestPath(grid)
    


if __name__=="__main__":
    #test_get_adjacencies()
    p82()






