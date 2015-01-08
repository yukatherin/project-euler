from project_euler_util.number_theory import is_prime, is_square
from math import sqrt

def check_goldbach_cond(n, primes):
    for p in primes:
        if is_square((n-p)/2):
            print n, p
            return True
    return False

def stream_composites():
    n = 3
    primes=[2]
    while(True):
        if is_prime(n):
            primes.append(n)
        else:
            cond_holds = check_goldbach_cond(n, primes)
            if (not cond_holds):
                print "found first", n
                break
        n += 2


if __name__=="__main__":
    stream_composites()
    