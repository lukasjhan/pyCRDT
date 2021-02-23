import GSet

def PSet():
    return (GSet.zero(), GSet.zero())

def zero():
    return PSet()

def value(a: PSet):
    add, rem = a
    return add - rem

def add(a: PSet, value):
    add, rem = a
    return add.add(value)

def rem(a: PSet, value):
    add, rem = a
    return rem.add(value)

def merge(a: PSet, b: PSet):
    add_a, rem_a = a
    add_b, rem_b = b
    return (GSet.merge(add_a, add_b), GSet.merge(rem_a, rem_b))