import itertools

def p191():
    marks_list = ['L','O','A']
    tup_list = list(itertools.product(marks_list, marks_list, marks_list, [True,False]))
    count_dict = { (i,j,k,l): 0 if ([i,j,k].count('L')>1)  or (l and [i,j,k].count('L')>0) or ([i,j,k].count('A')==3) 
                                else 1 
                                for i,j,k,l in tup_list }
    for t in range(27):
        next_count_dict = {(i,j,k,l): 0 if ([i,j,k].count('L')>1)  or (l and [i,j,k].count('L')>0) or ([i,j,k].count('A')==3)
                                        else sum([count_dict[(j,k,x,i=='L' or l)] for x in marks_list ])
                                        for i,j,k,l in tup_list }
        count_dict = next_count_dict
    tot_sum = sum([count_dict[(i,j,k,0)] for i,j,k in itertools.product(marks_list,marks_list,marks_list)])
    print tot_sum

if __name__ == "__main__":
    p191()