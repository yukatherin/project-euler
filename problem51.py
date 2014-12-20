from project_euler_util.number_theory import is_prime
from itertools import product

def generate_combos_to_check(nd, k, prefix):
    if nd < k:
        return
    if nd == k:
        yield prefix+"*"*k
    else:
        if k>0:
            new_prefix = prefix + "*"
            for comb in generate_combos_to_check(nd-1, k-1, new_prefix):
                yield comb
        for d in range(10):
            if not prefix and not d:
                continue
            new_prefix = prefix + str(d)
            for comb in generate_combos_to_check(nd-1,k, new_prefix):
                yield comb


def count_such_primes(seed):
    ct = 0
    found_primes = []
    for i in range(10):
        if seed[0]=="*" and i==0:
            continue
        generated = int(''.join([c if c!="*" else str(i) for c in seed]))
        if is_prime(generated):
            found_primes.append(generated)
            ct+=1
    return ct, found_primes


def p51():
    for nd,k in product(range(5,7), range(2,4)):
        for comb in generate_combos_to_check(nd,k,""):
            prime_ct, primes = count_such_primes(comb)
            if prime_ct >7:
                print primes
                return


if __name__=="__main__":
    p51() #9.9s



