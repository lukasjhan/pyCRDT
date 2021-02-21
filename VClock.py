from enum import Enum
import GCounter

class Ord(Enum):
    Lt = -1 # lower
    Eq = 0  # equal
    Gt = 1  # greater
    Cc = 2  # councurrent

VClock = GCounter.GCounter
zero = GCounter.zero
inc = GCounter.inc
merge = GCounter.merge

def compare(a: VClock, b:VClock):
    compare_list = [a.get(key, 0) - b.get(key, 0) for key in set(a.keys()) | set(b.keys())]
    eq = True; le = True; ge = True
    for ret in compare_list:
        if (ret != 0):
            eq = False
        if (ret > 0):
            le = False
        if (ret < 0):
            ge = False
    
    if (eq):
        return Ord.Eq
    if (le):
        return Ord.Lt
    if (ge):
        return Ord.Gt
    return Ord.Cc
