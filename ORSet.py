import VClock

def ORSet():
    return (dict(), dict())

def zero():
    return ORSet()

def value(s: ORSet):
    add, rem = s
    return {key for key in set(add.keys()) | set(rem.keys()) 
        if VClock.compare(add.get(key, VClock.zero()), rem.get(key, VClock.zero())) != VClock.Ord.Lt}

def add(s: ORSet, replica_id, value):
    add, rem = s
    add[value] = VClock.inc(add.get(value, VClock.zero()), replica_id)

def rem(s: ORSet, replica_id, value):
    add, rem = s
    rem[value] = VClock.inc(rem.get(value, VClock.zero()), replica_id)

def merge(s1: ORSet, s2: ORSet):
    add_1, rem_1 = s1
    add_2, rem_2 = s2

    merged_add = { key: VClock.merge(add_1.get(key, VClock.zero()), add_2.get(key, VClock.zero())) 
        for key in set(add_1.keys()) | set(add_2.keys()) }

    merged_rem = { key: VClock.merge(rem_1.get(key, VClock.zero()), rem_2.get(key, VClock.zero())) 
        for key in set(rem_1.keys()) | set(rem_2.keys()) }

    cleared_merged_rem = { key: merged_rem[key] for key in set(merged_rem.keys())
        if VClock.compare(merged_add.get(key, VClock.zero()), merged_rem[key]) == VClock.Ord.Gt or 
        VClock.compare(merged_add.get(key, VClock.zero()), merged_rem[key]) == VClock.Ord.Eq }

    return (merged_add, cleared_merged_rem)