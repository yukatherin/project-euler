
from collections import defaultdict

def p62():
    n = 345
    target_ncubes = 5
    d = defaultdict(list)
    while(True):
        cube_n = n**3
        k = str(sorted(str(cube_n)))
        d[k].append(cube_n)
        if len(d[k])==target_ncubes:
            print d[k]
            return
        n+=1

if __name__=="__main__":
    p62()
