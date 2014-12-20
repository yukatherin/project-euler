from project_euler_util.number_theory import is_prime


def poly(s,n):
    return (n**2*(s-2)-n*(s-4))/2

def generate_figurate_wi_range(deg, pmin=10**3, pmax=10**4):
    n = 10
    p = 0
    while (p<pmax):
        if p>pmin:
            print p
        n+=1
        p = poly(deg,n)

if __name__=="__main__":
    generate_figurate_wi_range(8)

