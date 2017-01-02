import sys
sys.path.append("..")
from project_euler_util.number_theory import primes_leq
from itertools import product
from collections import defaultdict


def p87():
    m = 50*10**6
    d = defaultdict(list)
    for a,b,c in product(primes_leq(m**(1.0/2)),
                         primes_leq(m**(1.0/3)),
                         primes_leq(m**(1.0/4))):
        n = a**2+b**3+c**4
        if n<m:
            d[n].append((a,b,c))
    print len(d.keys())

if __name__=="__main__":
    p87()

