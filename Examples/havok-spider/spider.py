import sys, getopt, unittest, urllib, urllib2
from Fost.json import root as jroot, jsonblob
from Fost.Test.spider import Spider

import Fost.settings
fostsettings = Fost.settings.database()

def main(configuration, options):
    local = configuration.local
    spider = Spider(local[ jroot / "urls" ], local[ jroot / "visited" ])
    spider.run_suite()

if __name__ == "__main__":
    print "havok-spider\nCopyright (C) 2008-2009 Felspar Co. Ltd."
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    if len(args) > 1:
        fostsettings[("Spider", "host")] = args[1]
    main(jsonblob(args[0]), **dict(options=opts))
