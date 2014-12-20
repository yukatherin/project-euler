from project_euler_util.number_theory import is_prime


def p58():
    k =0
    diag_ct = 1
    prime_ct = 0
    n = 1
    primes_diag_ratio = 1.0
    while(primes_diag_ratio >=0.1):
        k+=2
        prime_ct += sum(map(is_prime, [n+i*k for i in range(1,5)]))
        diag_ct += 4 
        primes_diag_ratio = prime_ct/float(diag_ct)
        print primes_diag_ratio
        n = n+4*k
    print 'side length:',k+1, primes_diag_ratio


if __name__=="__main__": #5.0s


