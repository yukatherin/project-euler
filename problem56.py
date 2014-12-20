

from itertools import product

def sum_digits(n):
    return sum([int(c) for c in str(n)])

def p56():
    max_digital_sum = 0
    for a,b in product(range(100), range(100)):
        if a%10==0:
            continue
        n = a**b ## using python long type
        test_sum = sum_digits(n)
        if test_sum>max_digital_sum:
            print a,b
            max_digital_sum= test_sum
    return max_digital_sum


if __name__=="__main__":
    print p56()


