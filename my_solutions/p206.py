import math
import sys
sys.path.append('../project_euler_util')
from number_theory import is_square

def form_number(d, val):
    if d == 1:
        if is_square(val):
            print val
            print val**(0.5)
        return
    if d % 2 == 0:
        dig = 10-(d/2)
        return form_number(d - 1, val + dig*(10**d))
    for i in range(10):
        form_number(d - 1, val + i*(10**d))

def p206():
    """10^8 operations"""
    form_number(18, 0)

if __name__ == "__main__":
    p206()