
from collections import defaultdict

class Card(object):
    @staticmethod
    def parseVal(s):
        if s=='T':
            return 10
        elif s=='J': 
            return 11
        elif s=='Q': 
            return 12
        elif s=='K': 
            return 13
        elif s=='A': 
            return 14
        else: 
            return int(s)

    def __init__(self, ident):
        self.ident = ident
        self.val = Card.parseVal(ident[0])
        self.suit = ident[1]

    def __lt__(self, other):
        return self.val < other.val


class Hand(object):

    def __init__(self, str_list):
        self.cards = {Card(s) for s in str_list}
        self.val_dict = defaultdict(set)
        self.suit_dict = defaultdict(set)
        self.hand_value = self.compute_value()

    def compute_value(self):

        for c in self.cards:
            self.val_dict[c.val].add(c.suit)
            self.suit_dict[c.suit].add(c.val)

        max_val = max(self.val_dict.keys())
        val_cnts = {k: len(v) for k,v in self.val_dict.iteritems()}

        if len(self.suit_dict.keys()) == 1:
            if min(sorted(self.val_dict.keys())) == 10:
                return (10, max_val)
            if min(sorted(self.val_dict.keys())) +4 == max(sorted(self.val_dict.keys())):
                return (9, max_val)
        four_keys = [k for k, v in val_cnts.iteritems() if v==4]
        if four_keys:
            return (8, max(four_keys))
        if tuple(sorted(val_cnts.values())) == (2,3):
            return (7, max_val)
        if len(self.suit_dict.keys()) == 1:
            return (6, max_val)
        if min(sorted(self.val_dict.keys())) +4 == max(sorted(self.val_dict.keys())) and max(val_cnts.values())==1:
            return (5, max_val)
        three_keys = [k for k, v in val_cnts.iteritems() if v==3]
        if three_keys:
            return (4, max(three_keys))
        pair_keys = [k for k, v in val_cnts.iteritems() if v==2]
        if len(pair_keys)==2:
            return (3, max(pair_keys))
        if len(pair_keys)==1:
            return (2, max(pair_keys))
        return (1, max_val)

def score(h1, h2):
    return 1 if h1.hand_value > h2.hand_value else 0


if __name__ == "__main__":

    h1 = Hand('TD JD QD KD AD'.split())
    h2 = Hand('2D 9C AS AH AC'.split())
    print h1.hand_value, h2.hand_value, h1.hand_value > h2.hand_value

    with open('../p054_poker.txt') as f:
        instance_record1 = defaultdict(int)
        instance_record2 = defaultdict(int)
        ct = 0

        for i, line in enumerate(f.readlines()):
            cards = line.split()
            h1, h2 = Hand(cards[:5]), Hand(cards[5:])
            if i <5:
                print h1.hand_value, h2.hand_value
            instance_record1[h1.hand_value[0]] += 1
            instance_record2[h2.hand_value[0]] += 1
            ct += score(h1, h2)
        print instance_record1
        print instance_record2
        print ct
