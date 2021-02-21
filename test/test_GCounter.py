import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import GCounter

def test_GCounter():
    a = GCounter.GCounter()
    assert a is not None
    print("{} passed!".format(sys._getframe().f_code.co_name))

def test_GCounter_zero():
    a = GCounter.zero()
    assert len(a) == 0
    print("{} passed!".format(sys._getframe().f_code.co_name))

def test_GCounter_inc():
    a = GCounter.zero()
    GCounter.inc(a, 'test')
    assert a['test'] == 1
    print("{} passed!".format(sys._getframe().f_code.co_name))

def test_GCounter_value():
    a = GCounter.zero()
    GCounter.inc(a, 'test')
    GCounter.inc(a, 'test2')
    assert GCounter.value(a) == 2
    print("{} passed!".format(sys._getframe().f_code.co_name))

def test_GCounter_merge():
    a = GCounter.zero()
    GCounter.inc(a, 'test')
    GCounter.inc(a, 'test')
    GCounter.inc(a, '342')
    GCounter.inc(a, '342')

    b = GCounter.zero()
    GCounter.inc(b, 'test')
    GCounter.inc(b, '123')
    GCounter.inc(b, '342')
    GCounter.inc(b, '342')
    GCounter.inc(b, '342')

    c = GCounter.merge(a, b)
    assert c == {'test': 2, '342': 3, '123': 1}
    print("{} passed!".format(sys._getframe().f_code.co_name))

def test():
    test_GCounter()
    test_GCounter_zero()
    test_GCounter_inc()
    test_GCounter_value()
    test_GCounter_merge()

test()