
from math import factorial

"""
Algorithm: 
    For j in {1,...k-1} //position where ascending
        count S1,S2 partitions of choice k out of 26 such that min(S1) < max(S2)
        (given selected k, there is only one choice that doesn't work where S1 is the max set)
"""

def comb(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))

if __name__ == "__main__":

    k = 18
    ct = 0
    for j in range(1, k):
        ct += comb(26, k) *(comb(k, j) - 1)
    print ct

