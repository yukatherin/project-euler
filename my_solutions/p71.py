from project_euler_util.number_theory import gcd, reduce_frac


def p71():
    max_d = 10**6
    target_fl = float(3)/7
    curr_cand_fl = float(2)/5
    curr_cand = 5,2
    for d in range(1,max_d+1):
        for n in range(int(curr_cand_fl*d)-1, int(target_fl*d)+1):  
            fl_val = float(n)/d       
            if fl_val< target_fl and fl_val > curr_cand_fl:
                curr_cand_fl = fl_val
                curr_cand = d,n
    return reduce_frac(*curr_cand)

if __name__=="__main__":
    print p71()


