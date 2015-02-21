
import copy

def is_complete(curr_ring, k):
	return sum([len(group) for group in curr_ring])==3*k

def form_groups(curr_ring, k, remaining_dig, ring_list):
	if not remaining_dig:
		if is_complete(curr_ring,k):
			ring_list.append(curr_ring)
		return
	m = len(curr_ring)-1
	if m == 0:
		for i,d in enumerate(remaining_dig):
			new_curr_ring = copy.deepcopy(curr_ring)
			new_curr_ring[m].append(d)
			if len(new_curr_ring[m])==3:
				new_curr_ring.append(list())
			form_groups(new_curr_ring, k, remaining_dig[:i]+remaining_dig[i+1:], ring_list)
		return
	if m<(k-1):
		for i,d in enumerate(remaining_dig):
			new_curr_ring = copy.deepcopy(curr_ring)
			if len(new_curr_ring[m])==0:
				if d<new_curr_ring[0][0]:
					continue
				new_curr_ring[m] = [d, new_curr_ring[m-1][2]]
				form_groups(new_curr_ring, k, remaining_dig[:i]+remaining_dig[i+1:], ring_list)
				continue
			if len(new_curr_ring[m])==2:
				new_curr_ring[m].append(d)
				form_groups(new_curr_ring,k,remaining_dig[:i]+remaining_dig[i+1:], ring_list)
				continue
			else:
				if sum(new_curr_ring[m])!=sum(new_curr_ring[m-1]):
					return
				new_curr_ring.append(list())
				form_groups(new_curr_ring,k,remaining_dig, ring_list)
	else: #m=k-1
		assert len(remaining_dig)==1
		d = remaining_dig[0]
		if d < curr_ring[0][0]:
			return
		new_curr_ring = copy.deepcopy(curr_ring)
		new_curr_ring[m] = [d, new_curr_ring[m-1][2],new_curr_ring[0][1]]
		if sum(new_curr_ring[m])!=sum(new_curr_ring[m-1]):
			return
		form_groups(new_curr_ring, k, list(), ring_list)

def ndig(n):
	return len(str(n))


def p68():
	ring_list=list()
	form_groups([list()], 5, range(1,11), ring_list)
	for r in ring_list:
		if reduce(lambda accum_val, x: accum_val if sum(x)==accum_val else 0 , r, sum(r[0])):
			print r

if __name__=="__main__":
	p68()
