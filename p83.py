
import pandas as pd
import numpy as np

from squaregrid import *


def findShortestPath(grid, printpath=True):
    source_pos = (0,0)
    end_pos = (grid.n-1, grid.n-1)
    unvisited_queue = set((i,j) for i,j in itertools.product(range(grid.n), range(grid.n)))
    dist = dict([(end_pos,grid.M[end_pos])])
    previous = dict()
    dijkstras(grid, end_pos, unvisited_queue, dist, previous)

    if printpath:
        print_path(source_pos, dist, previous, end_pos)
        
    return dist[source_pos]

def p83():

    try:
        M = np.array(pd.read_csv('p083_matrix.txt', header=None))
        #M = np.array(pd.read_csv('test_grid.txt', header=None))

    except IOError:
        print 'cannot find matrix file'
        return
    grid = SquareGrid(M, i_moves = [-1,1], j_moves =[-1,1])
    print findShortestPath(grid, printpath=True)
    


if __name__=="__main__":
    #test_get_adjacencies()
    p83()

