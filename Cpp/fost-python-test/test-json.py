import _test

def do_test(value, expected):
    assert _test.tojson(value) == "%s\n" % expected, _test.tojson(value)

do_test(None, "null")
do_test(True, "true")
do_test(False, "false")
do_test(0, "0")
do_test(123, "123")
do_test(123.45, "123.45")
do_test('some string', '"some string"')
