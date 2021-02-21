import LWWReg, utils

a = LWWReg.zero()

LWWReg.set_val(a, 'hi', utils.now())

b = LWWReg.zero()
LWWReg.set_val(b, 'tese', utils.now())

c = LWWReg.merge(a, b)
print(c)