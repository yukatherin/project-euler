
# found a bound on power p=100 since ndig(9**100)=96
from itertools import product

def ndig(n):
    return len(str(n))

def p63():
    ct = 0
    for d,p in product(range(1,10), range(1,100)):
        if ndig(d**p)==p:
            ct += 1
            if p==9:
                print d,p
    print ct


if __name__=="__main__":
    p63()

