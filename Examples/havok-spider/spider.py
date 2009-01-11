import sys, getopt, unittest
from Fost.json import jsonblob
from Fost.Test import spider

import Fost.settings
fostsettings = Fost.settings.database()

# Base settings
fostsettings[("Spider", "host")] = "http://localhost/"
fostsettings[("Spider", "Count")] = 25

def main(configuration, options):
    suite = unittest.TestSuite()
    spider.spider_test(suite, "%s/" % fostsettings[("Spider", "host")])
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    print "havok-spider\nCopyright (C) 2008-2009 Felspar Co. Ltd."
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    if len(args) > 1:
        fostsettings[("Spider", "host")] = args[1]
    main(jsonblob(args[0]), **dict(options=opts))
