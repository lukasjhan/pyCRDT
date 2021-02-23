import ORSet

a = ORSet.zero()
b = ORSet.zero()

ORSet.add(a, 'a', 1)
ORSet.add(a, 'a', 2)
ORSet.rem(a, 'a', 1)
print(a)

ORSet.add(b, 'b', 1)
ORSet.add(b, 'b', 2)
ORSet.rem(b, 'b', 2)
print(b)

c = ORSet.merge(a, b)
print(c)