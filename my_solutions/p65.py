
def p65():
    generators = [2]
    for k in range(1,35):
        generators.extend([1,2*k,1])
    n=99
    cf = (1, generators[n])
    for i in range(1,n)[::-1]:
        cf = cf[1], generators[i]*cf[1]+cf[0]
    cfn = generators[0]*cf[1]+cf[0], cf[1]
    print cfn[0]/float(cfn[1])
    return sum([int(d) for d in str(cfn[0])])


if __name__=="__main__":

    print p65()
