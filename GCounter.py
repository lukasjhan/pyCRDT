GCounter = dict

def zero():
    return GCounter()

def value(c: GCounter):
    return sum(c.values())

def inc(c: GCounter, key):
    c[key] = c.get(key, 0) + 1
    return c

def merge(a: GCounter, b:GCounter):
    return { key: max(a.get(key, 0), b.get(key, 0)) for key in set(a.keys()) | set(b.keys()) }