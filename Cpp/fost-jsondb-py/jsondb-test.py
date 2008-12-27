import _jsondb

blob1 = _jsondb.jsonblob()
assert blob1.filename == None, "filename: '%s'" % blob1.filename
blob2 = _jsondb.jsonblob("Cpp/fost-jsondb-py/testfile.json")
assert blob2.filename == "Cpp/fost-jsondb-py/testfile.json", "filename: '%s'" % blob2.filename
#blob3 = _jsondb.jsonblob("Cpp/fost-jsondb-py/testfile.json", dict(
#    hello = 'nightclub',
#    goodbye = 'country'
#))
#assert blob3.filename == "Cpp/fost-jsondb-py/testfile.json", "filename: '%s'" % blob3.filename

blob4 = blob2
assert blob4.filename == "Cpp/fost-jsondb-py/testfile.json", "filename: '%s'" % blob4.filename
