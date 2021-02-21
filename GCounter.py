from itertools import chain

GCounter = dict

def zero():
    return GCounter()

def value(c: GCounter):
    return sum(c.values())

def inc(c: GCounter, key):
    c[key] = c.get(key, 0) + 1

def merge(a: GCounter, b:GCounter):
    ret = GCounter()
    for k, v in chain(a.items(), b.items()):
        ret[k] = max(ret.get(k, 0), v)
    return ret
    