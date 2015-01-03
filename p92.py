
from project_euler_util.memoize import Memoize

def get_next(n):
    return sum([int(d)**2 for d in str(n) ])

def get_key(n):
    return tuple(sorted([int(d) for d in str(n)]))

def ends_in_89(n, d):
    k = get_key(n)
    try:
        return d[k]
    except KeyError:
        d[k] = ends_in_89(get_next(n),d)
        return d[get_key(n)]

def p92():
    starting_num_ct= 0
    d = dict([((8,9),True), ((1,),False)])
    for n in range(1,10**7):
        if ends_in_89(n,d):
            starting_num_ct +=1 
    print starting_num_ct

if __name__=="__main__": #72.7s, should be better!
    p92()


