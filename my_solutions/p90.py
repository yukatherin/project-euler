
from itertools import product

def special_contain(tuple, dice_list):
    otherd = dict([(6,9),(9,6)])
    to_try = [tuple]
    try:
        to_try.append((otherd[tuple[0]],tuple[1]))
        to_try.append((otherd[tuple[0]], otherd[tuple[1]]))
    except KeyError:
        pass
    try:
        to_try.append((tuple[0], otherd[tuple[1]]))
    except KeyError:
        pass
    return any([t in dice_list for t in to_try])

def symm_special_contain(tuple, dice_list):
    return special_contain(tuple, dice_list) or special_contain(tuple[::-1], dice_list)

def test_special_contain():
    print special_contain((9,9), [(6,6)])


def generate_combo( chosen, available_dig, generated):
    if len(chosen)==6:
        generated.append(chosen)
        return
    if not available_dig:
        return

    if not generated and not chosen:
        for i,d in enumerate(available_dig):
            start = [d]
            generate_combo(start, available_dig[i+1:], generated)
        return

    for i,d in enumerate(available_dig):
        next_chosen = chosen+[d]
        generate_combo(next_chosen, available_dig[i+1:], generated)
    return

def test_containment(target):
    d1 = [0, 5, 6, 7, 8, 9]
    d2 = [1, 2, 3, 4, 8, 9]
    print list(product(d1,d2))
    for t in target:
        print t, symm_special_contain(t, list(product(d1,d2)))


def p90():
    target = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]
    generated = list()
    generate_combo([], range(10), generated)
    die1combos = list(generated)
    die2combos = list(generated)

    
    two_die_combos = list()
    for i, d1 in enumerate(die1combos):
        for d2 in die2combos[i:]:
            two_die_combos.append((d1,d2))

    ct = 0
    for d1,d2 in two_die_combos:
        dice_list = list(product(d1,d2))
        if all([symm_special_contain(t,dice_list) for t in target]):
            ct+=1
    print ct

if __name__=="__main__": #2.1s
    p90()



