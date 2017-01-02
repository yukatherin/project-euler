

from math import sqrt
import numpy as np

def is_square(n):
    return sqrt(n)==int(sqrt(n))

def solvable_for(x,D):
    y = (x**2-1)/float(D)
    return is_square(y) and y>0

def argmax_min(maxD):
    max_x = 10**8
    Ds = set([i for i in range(2,maxD+1) if not is_square(i) ])
    for x in range(1,max_x):
        newDs = Ds.copy()
        for D in Ds:
            if solvable_for(x,D):
                newDs.remove(D)
                if (len(Ds)==1):
                    print Ds
                    return
        Ds = newDs
    print Ds

def min_x_soln(D):
    assert not is_square(D)
    max_x=10**7
    for x in range(1,max_x):
        if solvable_for(x,D):
            return x
    print 'no soln found for', D

def argmax_D(maxD):
    curr_max_D = None
    curr_max_min = 1
    for D in range(2,maxD+1):
        #print D
        if is_square(D):
            continue
        min_x = min_x_soln(D)
        if min_x > curr_max_min:
            curr_max_D= D
            curr_max_min=min_x
    return curr_max_D, curr_max_min


if __name__=="__main__":
    print argmax_min(100)

