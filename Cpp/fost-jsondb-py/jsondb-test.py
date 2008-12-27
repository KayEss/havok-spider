import _jsondb

blob1 = _jsondb.jsonblob()
assert blob1.filename == None, "filename: '%s'" % blob1.filename
blob2 = _jsondb.jsonblob("filename.json")
assert blob2.filename == "filename.json", "filename: '%s'" % blob2.filename
blob3 = _jsondb.jsonblob("filename.json", "{}")
