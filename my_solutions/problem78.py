from project_euler_util.memoize import Memoize

def pent(k):
    return k*(3*k-1)/2


def part(n,m, ndig = 6): # pentagonal number theorem
    if m==1:
        return 1
    ct = 0

    k=1
    while(True):
        if pent(k)>n:
            break
        ct = (ct + (-1)**(k-1) * part(n-pent(k),n-pent(k)) ) % 10**ndig
        k+=1

    k=-1
    while(True):
        if pent(k)>n:
            break
        ct = (ct + (-1)**(k-1) * part(n-pent(k),n-pent(k)) ) % 10**ndig
        k-=1
    return ct

part = Memoize(part)

def p78():
    n=6
    ndig=6
    max_iter = 10**7

    for i in xrange(max_iter):
        try:
            part_ct = part(n,n)
        except:
            print 'stopped at ',n
            import traceback; traceback.print_exc()
            return
        #print n, part_ct%10**ndig
        if part_ct%10**ndig ==0:
            print n, int(part_ct)
            return 
        n+=1

if __name__=="__main__": #35.1s
    p78()


