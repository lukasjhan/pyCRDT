GSet = set

def zero():
    return set()

def value(s: GSet):
    return s

def add(s: GSet, value):
    s.add(value)

def merge(a: GSet, b: GSet):
    return a | b