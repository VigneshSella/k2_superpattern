from __future__ import generators
import numpy as np
import random


def KnuthMorrisPratt(text, pattern):

    '''Yields all starting positions of copies of the pattern in the text.
Calling conventions are similar to string.find, but its arguments can be
lists or iterators, not just strings, it returns all matches, not just
the first one, and it does not need the whole text in memory at once.
Whenever it yields, it will have read the text exactly up to and including
the match that caused the yield.'''

    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos
            
names = ["Hassan","Sandeep","Kevin","Kazim","Ali","Aaron", "Ogi", "Zeeshan", "Vignesh"]
max_size = 0
final_order = []
for _ in range(10):
    order = ["Hassan"] + random.sample(names[1:],len(names)-1)
    for __ in range(100):
        for i in range(len(names)):
            s = 0
            k = 0
            for s in KnuthMorrisPratt(order, [order[-1],names[i]]): s=1
            if order[-1] != names[i] and order[-2] != names[i] and order[-3] != names[i]: #and order[-4] != names[i]:
                if s != 1 and k != 1:
                    order.append(names[i])
    if len(order) > max_size:
        max_size = len(order)
        final_order = order
print(*final_order, sep='\n')
print('Length = {}'.format(len(final_order)))
