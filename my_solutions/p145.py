


def reverse(n):
    '''Input: int; Output: int'''
    return int(str(n)[::-1])

def is_reversible(n):
    sum = n + reverse(n)
    for c in str(sum):
        if int(c) % 2 == 0:
            return False
    return True

if __name__=="__main__":

    print is_reversible(36)
    print is_reversible(63)
    print is_reversible(409)
    print is_reversible(904)
    print is_reversible(905)

    for i in range(50**8):
        if i % 10**8 == 0:
            print i
        pass


   (0-1,0-9,0-9)     

