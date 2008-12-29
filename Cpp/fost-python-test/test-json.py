import _test, sys

def to_json(value, expected):
    print value, expected
    sys.stdout.flush()
    assert _test.tojson(value, False) == "%s" % expected, _test.tojson(value, True)

to_json(None, "null")
to_json(True, "true")
to_json(False, "false")
to_json(0, "0")
to_json(123, "123")
to_json(123.45, "123.45")
to_json('some string', '"some string"')
to_json("""some string\twith a tab""", '"some string\\twith a tab"')
to_json([], "[]")
to_json([1,2], "[1,2]")
to_json([1,2,[3,"hello"]], "[1,2,[3,\"hello\"]]")
