import _test

assert _test.tojson(None) == "null\n", _test.tojson(None)
assert _test.tojson(True) == "true\n", _test.tojson(True)
assert _test.tojson(False) == "false\n", _test.tojson(False)
