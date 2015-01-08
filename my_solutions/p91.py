
from itertools import product
from math import sqrt

def dot(v1,v2):
    return sum([e1*e2 for e1,e2 in zip(v1,v2)])

def is_right_triangle(pq,op,oq):
    return not dot(pq,op) or not dot(op,oq) or not dot(pq,oq)

def get_angle(p):
    return p[0]/sqrt(p[0]**2+p[1]**2)


def p91(): #O(M^4)
    M = 50
    triangle_ct = 0
    for p in product(range(M+1), range(M+1)):
        if p==(0,0):
            continue
        for q in product(range(M+1), range(M+1)):
            if q==(0,0):
                continue
            if get_angle(q)>= get_angle(p):
                continue
            pq = (q[0]-p[0], q[1]-p[1])
            if is_right_triangle(pq, p, q):
                triangle_ct +=1
    print triangle_ct

if __name__=="__main__":
    p91()
