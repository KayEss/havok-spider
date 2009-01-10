import _json, os

def rmfile(f):
    if os.path.isfile(f):
        os.remove(f)

# Perform some basic tests to show we can create the objects
blob1 = _json.jsonblob()
assert blob1.filename == None, "filename: '%s'" % blob1.filename
blob2 = _json.jsonblob("Cpp/fost-json-py/testfile.json")
assert blob2.filename == "Cpp/fost-json-py/testfile.json", "filename: '%s'" % blob2.filename

# Make sure we can make a file on disk
rmfile("Cpp/fost-json-py/testfile-new.json")
blob3 = _json.jsonblob("Cpp/fost-json-py/testfile-new.json", dict(
    hello = 'nightclub',
    goodbye = 'country',
))

# Aliasing the same database
blob4 = blob2
assert blob4.filename == "Cpp/fost-json-py/testfile.json", "filename: '%s'" % blob4.filename

# Grab a local transaction from the BLOB
local3 = blob3.local
assert local3 == dict(hello = 'nightclub', goodbye = 'country'), local3.json


# Tidy up files
rmfile("Cpp/fost-json-py/testfile-new.json")
