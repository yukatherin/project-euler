from project_euler_util.number_theory import is_prime
from collections import defaultdict

def poly(s,n):
    return (n**2*(s-2)-n*(s-4))/2

def generate_figurate_wi_range(deg, pmin=10**3, pmax=10**4):
    d = defaultdict(list)
    n = 10
    p = 0
    while (p<pmax):
        if p>pmin:
            d[p/(10**2)].append(p)
        n+=1
        p = poly(deg,n)
    return d

def make_cycle(cycle_sofar, deg_used, dd, results):
    n = len(dd.keys())
    if len(deg_used) == n:
        if cycle_sofar[n-1]%10**2 == cycle_sofar[0]/10**2:
            results.append(cycle_sofar)
        return

    if not cycle_sofar:
        first_deg = dd.keys()[0]
        for temp_key in dd[first_deg]:
            for n in dd[first_deg][temp_key]:
                make_cycle([n], [first_deg],dd, results)
        return

    curr_key = cycle_sofar[len(cycle_sofar)-1] % 10**2
    for deg in dd.keys():
        if deg in set(deg_used):
            continue
        for n in dd[deg][curr_key]:
            updated_cycle = cycle_sofar + [n]
            make_cycle(cycle_sofar+[n], deg_used+[deg], dd, results)





def p61():
    dd = dict()
    for i in range(3,9):
        dd[i] = generate_figurate_wi_range(i)
    results = []
    make_cycle([], [], dd, results)
    print results, sum(results[0])


if __name__=="__main__":
    p61()


