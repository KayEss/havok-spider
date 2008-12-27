import _test

assert _test.annotate("Some string") == "Passed in 'Some string'", _test.annotate("Some string")
assert _test.annotate(u"Some string") == "Passed in 'Some string'", _test.annotate(u"Some string")
try:
    _test.annotate( None )
    assert False
except:
    assert True
class SomeClass:
    def __unicode__(self):
        return u"Some class instance"
assert _test.annotate(unicode(SomeClass())) == "Passed in 'Some class instance'", _test.annotate(unicode(SomeClass()))

