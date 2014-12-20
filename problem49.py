from project_euler_util.number_theory import is_prime
from collections import defaultdict
import pdb

UPPER_BOUND = 10**3
LOWER_BOUND = 10**4

def tuple_dig(n):
    return tuple(sorted(str(n)))

def hash_primes():
    prime_dict = defaultdict(list)
    for n in xrange(UPPER_BOUND, LOWER_BOUND):
        if is_prime(n):
            prime_dict[tuple_dig(n)].append(n)
    return prime_dict

def print_arithseq(sorted_int, chosen):
    if len(chosen)==3:
        print chosen
        return True
    if len(sorted_int)+len(chosen)<3:
        return False
    new_sorted_int = list(sorted_int)
    if len(chosen)<2:
        while(True):
            n = new_sorted_int.pop(0)
            new_chosen= chosen+[n]
            return print_arithseq(new_sorted_int, chosen) or print_arithseq(new_sorted_int, new_chosen)
    elif len(chosen)>=2:
        delta = chosen[1]-chosen[0]
        while(new_sorted_int):
            n = new_sorted_int.pop(0)
            new_chosen= chosen+[n]
            if n == chosen[len(chosen)-1]+delta:
                return print_arithseq(new_sorted_int, new_chosen)


def prob_49():
    prime_dict = hash_primes()
    for k in prime_dict:
        print_arithseq(sorted(prime_dict[k]),[])


if __name__=="__main__":
    prob_49()
    





