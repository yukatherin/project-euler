
from project_euler_util.number_theory import reduce_frac
import math
from collections import defaultdict

def get_next(nr,ni,dr,di): 
    '''fractions of form: (sqrt(nr)+ni)/(sqrt(dr)+di)'''
    n,d = reduce_frac(ni,dr-di**2)
    a = int(float(n*(math.sqrt(dr) -di))/d)
    di = -di - a*d/n
    return a, dr, di, 0, d # result: a - n*(sqrt(dr)+di)/d

def get_period(n):
    d = defaultdict(list)
    a = int(math.sqrt(n))
    a,nr,ni,dr,di = get_next(0,1,n,-a)
    max_per = 1000
    for i in range(max_per):
        a,nr,ni,dr,di = get_next(0,di,nr,ni)
        k = (a,nr,ni,dr,di)
        d[k].append(i)
        if len(d[k])>1:
            return d[k][1]-d[k][0]

def p64():
    N = 10**4
    ct_odd_per = 0
    for n in range(2,N+1):
        if math.sqrt(n)==int(math.sqrt(n)):
            continue
        if get_period(n) is None:
            print n
        ct_odd_per += get_period(n)%2==1
    print ct_odd_per


if __name__=="__main__":
    p64()