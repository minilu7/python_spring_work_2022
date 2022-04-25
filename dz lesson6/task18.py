import itertools
import random

storona = 4
chislo = 6

hand = tuple(sorted(random.randint(1, chislo) for x in range(storona)))
for x in range(1, storona+1):
    print(set(itertools.permutations(hand, x)))