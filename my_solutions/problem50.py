from project_euler_util.number_theory import is_prime

UPPER_BOUND=10**6

def contains_prime(primes, k):
    test_sum=0
    primes_for_k=[]
    for i in xrange(k,len(primes)+1):
        test_sum = sum(primes[i-k:i])
        if test_sum>UPPER_BOUND:
            return primes_for_k
        if is_prime(test_sum):
            primes_for_k.append(test_sum)
    return primes_for_k

def prime_stream():
    primes=[2]
    n=3
    k = 501
    max_k = k
    max_prime = 0
    test_sum=0
    while(test_sum<UPPER_BOUND):
        if is_prime(n):
            primes.append(n)
            if len(primes)>k:
                test_sum = sum(primes[-k:])
                if is_prime(test_sum):
                    max_prime = test_sum
                    max_k = k
        n+=2

    while(k<600):
        k += 2
        primes_for_k = contains_prime(primes,k)
        if primes_for_k:
            print k
            print primes_for_k
            max_prime = primes_for_k[0]
            max_k = k

if __name__=="__main__":
    prime_stream()


