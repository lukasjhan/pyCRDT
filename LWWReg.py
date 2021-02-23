def LWWReg():
    return {'value': None, 'timestamp': 0}

def zero():
    return LWWReg()

def value(r: LWWReg):
    return r['value']

def set_val(r: LWWReg, value, timestamp):
    if (r['timestamp'] < timestamp):
        r['value'] = value
        r['timestamp'] = timestamp
    return r

def merge(r1: LWWReg, r2: LWWReg):
    if (r1['timestamp'] > r2['timestamp']):
        return r1
    else:
        return r2
