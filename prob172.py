from math import factorial
from itertools import permutations

def list_combo(rd, rs, tup, max_d, tup_list):
    if (rd==0):
        if rs==0:
            tup_list.append(tup)
        return
    for d in range(max_d+1):
        if d <= rs:
            new_tup = tup + (d,)
            list_combo(rd-1, rs-d, new_tup, d, tup_list)

def count_restricted_perm(rep_tup):
    n_perm = 0
    for perm in set(permutations(rep_tup)): # permutation assigns rep count to digit
        p = sum(perm[1:])*factorial(sum(perm)-1)
        for val in perm:
            p /= factorial(val)
        n_perm += p
    return n_perm

def p172():
    tup_list = []
    list_combo(10, 18, (), 3, tup_list)
    count_n = 0
    for tup in tup_list:
        count_n += count_restricted_perm(tup)
    print count_n
    

if __name__=="__main__":
   p172()