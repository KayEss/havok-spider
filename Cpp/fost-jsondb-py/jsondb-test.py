import _jsondb, os

def rmfile(f):
    if os.path.isfile(f):
        os.remove(f)


blob1 = _jsondb.jsonblob()
assert blob1.filename == None, "filename: '%s'" % blob1.filename
blob2 = _jsondb.jsonblob("Cpp/fost-jsondb-py/testfile.json")
assert blob2.filename == "Cpp/fost-jsondb-py/testfile.json", "filename: '%s'" % blob2.filename

rmfile("Cpp/fost-jsondb-py/testfile-new.json")
blob3 = _jsondb.jsonblob("Cpp/fost-jsondb-py/testfile-new.json", dict(
    hello = 'nightclub',
    goodbye = 'country',
))

blob4 = blob2
assert blob4.filename == "Cpp/fost-jsondb-py/testfile.json", "filename: '%s'" % blob4.filename

local3 = blob3.local
assert local3 == dict(hello = 'nightclub', goodbye = 'country'), local3.json


rmfile("Cpp/fost-jsondb-py/testfile-new.json")
