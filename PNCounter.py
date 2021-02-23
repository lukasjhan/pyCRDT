import GCounter

def PNCounter():
    return (GCounter.GCounter(), GCounter.GCounter())

def zero():
    return GCounter.zero(), GCounter.zero()

def value(pn: PNCounter):
    inc, dec = pn
    return {key: inc.get(key, 0) - dec.get(key, 0) for key in set(inc.keys()) | set(dec.keys())}

def inc(pn: PNCounter, key):
    inc, dec = pn
    return GCounter.inc(inc, key)

def dec(pn: PNCounter, key):
    inc, dec = pn
    return GCounter.inc(dec, key)

def merge(a: PNCounter, b: PNCounter):
    inc_a, dec_a = a
    inc_b, dec_b = b
    return (GCounter.merge(inc_a, inc_b), GCounter.merge(dec_a, dec_b))