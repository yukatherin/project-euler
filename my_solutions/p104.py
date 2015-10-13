# -*- coding: utf-8 -*-
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). 
# And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

import math
import numpy as np
import sys


def is_pandigital(s):
    for i in range(1,10):
        if str(i) not in s:
            return False
    return True

if __name__ == "__main__":
    phi = (1+math.sqrt(5))/2
    n = 2
    f0, f1 = 1, 1
    while(True):
        n+=1
        f0, f1 = f1, (f0+f1) % 10**9 
        if not is_pandigital(str(f1)[-9:]):
            continue
        top_val_est = n*np.log(phi) - np.log(5)/2
        ndig = top_val_est/np.log(10.0)
        top_val_est = top_val_est - (int(ndig)-11)*np.log(10) # divide to get top digits
        top_dig_str = str(np.exp(top_val_est))[:10]
        if is_pandigital(top_dig_str):
            print 'solution', n
            print ndig
            sys.exit(0)
