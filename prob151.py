from __future__ import division
import time


def tear(sheets, idx):
	torn = list(sheets)
	torn[idx] -= 1
	if idx<4:
		for i in range(idx+1,5):
			torn[i] += 1

	return torn

def rec(sheets):
	if sum(sheets)==0: return 0
	n = sum(sheets)
	one_sum = 1 if n==1 else 0
	return one_sum + sum([sheets[i]/n * rec(tear(sheets,i)) for i in range(5) if sheets[i]>0])

def p151():
	print('expected value: ', rec((1,0,0,0,0))-2.0)

if __name__=="__main__":
	b=time.clock()
	p151()
	e = time.clock()
	print('time elapsed',e-b)

        

