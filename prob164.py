
import itertools

def p164():
    tup_list = list(itertools.product(range(10), range(10), range(10)))
    count_dict = {(i,j,k): 1 if i+j+k<=9 else 0 for i,j,k in tup_list }
    for t in range(17):
        count_dict = {(i,j,k):0 if i+j+k>9 else sum([count_dict[(j,k,x)] for x in range(10)]) for i,j,k in tup_list}
    tot_sum = sum([count_dict[(i,j,k)] for i,j,k in count_dict if i>0])
    print tot_sum

if __name__ == "__main__":
    p164()
