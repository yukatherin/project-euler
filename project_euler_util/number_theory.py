
from math import sqrt

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True   

def is_square(n):
    return int(sqrt(n))==sqrt(n)

def gcd(n,m): 
    '''gcd of two ints'''
    if n<m:
        return gcd(m,n)
    if m==0:
        return n
    return gcd(m,n%m)

def reduce_frac(n,d):
    c_gcd = gcd(n,m)
    while(cgd >1):
        n /= c_gcd
        d /= c_gcd
    return n,d


if __name__=="__main__":
    print is_prime(4804)
    print 'gcd 3,4', gcd(3,4)
    print 'gcd 4,3', gcd(4,3)
    print 'gcd 4,6', gcd(4,6)
    print 'gcd 15,30', gcd(15,30)
    print reduce_frac(15,30)
