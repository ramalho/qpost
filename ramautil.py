"""
from ramautil import shuffle_range

print(shuffle_range([1,2,3,4,5], 30))


"""

import random


def hello():
    print 'Hello'


def endless_shuffle(items):
    original_items = list(items)
    items = []
    last_yield = None
    while True:
        if not items:
            items = list(original_items)
            random.shuffle(items)
            if items[-1] == last_yield:  # avoid yielding duplicate
                choice = items.pop(0)
            else:
                choice = items.pop()
        else:
            choice = items.pop()
        yield choice
        last_yield = choice


def shuffle_range(items, stop):
    return [i for _, i in zip(xrange(stop), endless_shuffle(items))]


if __name__ == '__main__':

    items = [1, 2, 3, 4]
    for i in shuffle_range(items, 30):
        print i,

    print
