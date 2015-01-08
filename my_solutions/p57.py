
from project_euler_util.number_theory import reduce_frac
import math
import sys

def get_next(n,d):
    return n+2*d, d+n

def p57():
    n,d = 1,1
    ct = 0
    for i in range(10**3):
        n,d = get_next(n,d)
        if int(math.log10(n))>int(math.log10(d)):
            # print n,d, i
            ct += 1
    print ct

if __name__=="__main__":
    p57()


