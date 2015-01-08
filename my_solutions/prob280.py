#Soln using absorbing markov chains: http://en.wikipedia.org/wiki/Absorbing_Markov_chain */
from __future__ import division
import numpy as np
import itertools
from transitionmatrix import generateTransitionMatrix, index

def walk_ant(top_set, bottom_avail, curr_row, curr_col, going_up, k=5):
    if (len(bottom_avail)==0) and (len(top_set)==0):
        return 0;
    absorb_row = top_set if going_up else bottom_avail
    P = generateTransitionMatrix(absorb_row);
    transient_indices = [i for i in range(k**2) if i not in map(lambda x:index(0,x),absorb_row)]
    absorb_indices = map(lambda x:index(0,x), absorb_row)
    Q = P.take(transient_indices, axis=0).take(transient_indices, axis=1)
    R = P.take(transient_indices, axis=0).take(absorb_indices,axis=1)
    N = np.linalg.inv(np.identity(len(transient_indices)) - Q);
    t = np.dot(N, np.ones(len(transient_indices))); # t[i] is expected time to absorption starting from transient state i
    B = np.dot(N,R); # B[i][j] is prob. of absorption in absorbing state j starting from transient state i

    i = index(curr_row, curr_col) - len(absorb_row) # transient index is index after removing absorbing states
    exp_steps_from_curr_pos = t[i] # exp. time to absorption 
    for j,col in enumerate(absorb_row):
        new_top_set = list(top_set)
        new_bottom_avail = list(bottom_avail)
        new_top_set.pop(j) if going_up else new_bottom_avail.pop(j)
        exp_steps_from_curr_pos +=  B[i][j] * walk_ant(new_top_set, new_bottom_avail, k-1, col, not going_up)
    return exp_steps_from_curr_pos



if __name__=="__main__":
    print ('expected num. steps:'); print walk_ant(range(5), range(5), 2, 2, False)
	
