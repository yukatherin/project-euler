
import pandas as pd
import numpy as np

from squaregrid import *


def findShortestPath(grid, print_path=True):
    source_pos = (0,0)
    end_pos = (grid.n-1, grid.n-1)
    unvisited_queue = set((i,j) for i,j in itertools.product(range(grid.n), range(grid.n)))
    dist, previous = dijkstras(grid, end_pos, unvisited_queue, source_val=grid.M[end_pos])
    node = source_pos
    if print_path:
        while True:
            print node, dist[node]
            if node==end_pos:
                break
            node = previous[node]
    return dist[source_pos]

def p83():

    try:
        M = np.array(pd.read_csv('p083_matrix.txt', header=None))
        #M = np.array(pd.read_csv('test_grid.txt', header=None))

    except IOError:
        print 'cannot find matrix file'
        return
    grid = SquareGrid(M, i_moves = [-1,1], j_moves =[-1,1])
    print findShortestPath(grid, print_path=True)
    


if __name__=="__main__":
    #test_get_adjacencies()
    p83()

