

def get_next(n):
    return n + int(str(n)[::-1])

def is_lychrel(n):
    max_iter = 50
    nn = get_next(n)
    for i in range(max_iter):
        if str(nn)==str(nn)[::-1]:
            return False
        nn = get_next(nn)
    print n
    return True

def p55():
    ct_lychrel = 0
    for n in xrange(1,10**4):
        if is_lychrel(n):
            ct_lychrel += 1
    return ct_lychrel



if __name__=="__main__":
    print p55()