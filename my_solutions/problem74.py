from math import factorial

def get_next(n):
    return sum([factorial(int(c)) for c in str(n)])


def count_chain(n, d):
    ct = 0
    nn = n
    while(True):
        if nn in set(d.keys()):
            ct = ct + d[nn]
            d[n] = ct
            return ct
        nn = get_next(nn)
        ct+=1
    return ct

def initialize_dict():
    d = dict() # number of (unrepeated) digits remaining in the chain including that number
    return d


def p74():
    d = initialize_dict()
    n = 4
    print len(d.keys())
    print count_chain(78,d)



if __name__=="__main__":
    p74()