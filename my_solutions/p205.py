from __future__ import division
from collections import defaultdict

def fill_dict(d, dice_remaining, k, sum):
    if dice_remaining == 0:
        d[sum] += 1
        return
    for i in range(k):
        fill_dict(d, dice_remaining - 1, k, sum + 1 + i)

def p205():
    """Probability peter beats colin to 7 decimal places."""

    # set up 
    peterd = defaultdict(int)
    fill_dict(peterd, 9, 4, 0)
    colind = defaultdict(int)
    fill_dict(colind, 6, 6, 0)
    petertot = sum(peterd.values())
    colintot = sum(colind.values())

    # sum probabilities
    prob = 0.0
    for peterk in peterd:
        colinunderscores = sum([v for (k,v) in colind.iteritems() if k < peterk])
        prob += peterd[peterk]/petertot * colinunderscores/colintot
    return prob

if __name__ == "__main__":
    print p205()
    
