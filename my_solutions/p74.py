
from math import factorial
from collections import defaultdict

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def get_next(n):
    return sum([factorial(int(i)) for i in str(n)])

@Memoize
def len_chain(n, chain):
    nn = get_next(n)
    if nn in chain:
        return 1
    new_chain=chain +(nn,)
    return 1 + len_chain(nn, new_chain)


if __name__=="__main__":
    ct = 0
    for n in range(1,10**6):
        if n%(10**4)==0:
            print n
        if(len_chain(n, (n,)) ==60):
            ct +=1
            print ct

