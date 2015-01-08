
from fractions import gcd
from math import sqrt
from collections import defaultdict

# euclid's formula
def p75():
    max_L = 1500*10**3
    lcounts = defaultdict(int)
    max_m = int(sqrt(max_L/2))
    for m in range(2,max_m):
        for n in range(1,m):
            if gcd(m,n)>1 or (m-n)%2==0: # check m,n coprime, m-n odd
                continue 
            primitive_L = 2*m**2 + 2*m*n
            if primitive_L>max_L:
                break
            for k in range(1,int(max_L/primitive_L)+1):
                lcounts[k*primitive_L] += 1
    singular_triangle_ct = sum([ct==1 for ct in lcounts.values()])
    print singular_triangle_ct

if __name__=="__main__": #1.0s
    p75()


