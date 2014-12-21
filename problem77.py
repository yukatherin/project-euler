from project_euler_util.number_theory import is_prime

def count_prime_partitions(n, primes):
    if n==0:
        return 1
    if n<0 or not primes:
        return 0
    ct=0
    ct+= count_prime_partitions(n, primes[1:])
    while(n>=0):
        n -= primes[0]
        ct+= count_prime_partitions(n, primes[1:])
    return ct

def p77():
    primes = [2]
    max_n = 10**4
    for n in xrange(max_n):
        partition_ct = count_prime_partitions(n, primes)
        if partition_ct > 4000:
            print n, partition_ct
        if partition_ct > 5000:
            print "first:", n
            return 
        if n%2==1 and is_prime(n):
            primes.append(n)

if __name__=="__main__": #7.2s
    p77()