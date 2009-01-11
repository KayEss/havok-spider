import sys, getopt
from Fost.json import jsonblob
from Fost.Test import spider

import Fost.settings
fostsettings = Fost.settings.database()

# Base settings
fostsettings[("Spider", "host")] = "http://localhost/"
fostsettings[("Spider", "Count")] = 25

def main(configuration, options):
    pass

if __name__ == "__main__":
    print "havok-spider\nCopyright (C) 2008-2009 Felspar Co. Ltd."
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    configuration = jsonblob(args[0])
    main(configuration.local, **dict(options=opts))
