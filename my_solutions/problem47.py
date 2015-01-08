from project_euler_util.number_theory import is_prime

def count_dividing_primes(n, primes):
    prime_ct = 0 
    for p in primes:
        if n%p ==0:
            prime_ct += 1
    return prime_ct

def identify_consecutive():
    n=3
    primes=[2]
    target_n_dividingprimes = 4
    target_n_conseq = 4
    conseq_n = []
    while(True):
        if (n%2==1 and is_prime(n)):
            primes.append(n)
        prime_ct = count_dividing_primes(n, primes)
        if prime_ct==target_n_dividingprimes:
            conseq_n.append(n)
            if len(conseq_n)==target_n_conseq:
                print conseq_n
                break
        else:
            conseq_n = list()
        n+=1


if __name__=="__main__":
    identify_consecutive()


# Brian's amazing solution: (https://projecteuler.net/thread=47)
# Limit=1000000     # Search under 1 million for now
# factors=[0]*Limit # number of prime factors.
# count=0
# for i in xrange(2,Limit):
#     if factors[i]==0:
#         # i is prime
#         count =0
#         val =i
#         while val < Limit:
#             factors[val] += 1
#             val+=i
#     elif factors[i] == 4:
#         count +=1
#         if count == 4:
#             print i-3 # First number
#             break
#     else:

