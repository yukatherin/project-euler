
import pandas as pd
import numpy as np

from squaregrid import *

# strategy, walk back from magic node at (n,n)
def findShortestPath(gr, print_path=False):
    magic_end_pos = (gr.n, gr.n)
    unvisited_queue = set((i,j) for i,j in itertools.product(range(gr.n), range(gr.n)))
    unvisited_queue.add(magic_end_pos)
    dist, previous = dijkstras(gr, magic_end_pos, unvisited_queue, source_val=0)
    grid_min = min([dist[i,0] for i in range(gr.n)])
    min_i = np.argmin([dist[i,0] for i in range(gr.n)])
    node = (min_i,0)
    print dist
    while(True):
        if print_path:
            print node, dist[node]
        if node==magic_end_pos:
            break
        node = previous[node]
    return grid_min

def p82():

    try:
        M = np.array(pd.read_csv('p082_matrix.txt', header=None))
    except IOError:
        print 'cannot find matrix file'
        return
    grid = SquareGrid(M, i_moves = [-1,1], j_moves =[-1])
    print findShortestPath(grid,  print_path=True)
    


if __name__=="__main__":
    #test_get_adjacencies()
    p82()






