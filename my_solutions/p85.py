
from itertools import product

def count(N,M,n,m):
    return (N-n+1)*(M-m+1)

def count_for_grid(N,M):
    ct = 0
    for n,m in product(range(1,N+1), range(1,M+1)):
        ct += count(N,M,n,m)
    return ct

def p85():
    try_max = 10**2
    target = 2*10**6
    smallest_diff = 100000
    best = tuple()
    for N in range(1,try_max):
        for M in range(1,N+1):
            ct = count_for_grid(N,M)
            if ct > .999*target and abs(ct-target)<smallest_diff
                best= N,M
                smallest_diff = abs(ct-target)
                print N,M,smallest_diff # kill it when you see 2, code obviously needs work
            if ct > target:
                break
    print best
    print 'Area', best[0]*best[1]
                    


if __name__=="__main__":
    p85()
