from __future__ import division
from math import factorial, floor
from operator import mul

# perm_unique was taken from here: http://stackoverflow.com/questions/6284396/permutations-with-unique-values
class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return list(perm_unique_helper(listunique,[0]*u,u-1))

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

def win_prob(k):
    p = 0
    blue_prob = [1/(i+1) for i in range(1,k+1)]
    for n_red in range(int((k-1)/2)+1):
        combo = [1 for i in range(k-n_red)] + [0 for i in range(n_red)]
        for perm in perm_unique(combo):
            p += reduce(mul, [blue_prob[i] if perm[i] else 1-blue_prob[i] for i in range(k) ])
    return p

if __name__ == "__main__":
    k=15
    print 'winning prob', win_prob(k)
    print 'maximum prize', 1/win_prob(k)