from math import sqrt
from itertools import combinations, permutations
import time
def formFromDigits(numlist):
    s = ''.join(map(str,numlist))
    return int(s)

def isprime(n):
    if n==1: return False
    if n==2: return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: return False
    return True

def set_global():
    global pdset
    pdset = 0


def count_pdset(max_used,rdig_list,min_ndig):
    # rdig_list is a set
    global pdset
    if len(rdig_list)==0 : 
        pdset += 1
        #print('nsets',pdset)
        return
    if min_ndig>len(rdig_list):
        return


    for n in range(min_ndig,len(rdig_list)+1):
        avail=list(combinations(rdig_list,n))
        for l in avail:
            for ll in list(permutations(l)):
                p = formFromDigits(ll)
                if (p>max_used) & (isprime(p)):
                    #print(p, rdig_list)
                    newrdig_list = rdig_list - set(l)
                    count_pdset(p, newrdig_list, n)
    return


if __name__=="__main__":
    b = time.clock()
    set_global();
    global pdset
    count_pdset(0,set(range(1,10)),1)
    print pdset
    e = time.clock()
    print('time elapsed', e-b)