import sys, getopt, unittest, urllib, urllib2
from Fost.json import root as jroot, jsonblob
from Fost.Test.spider import Spider

import Fost.settings
fostsettings = Fost.settings.database()

def main(configuration):
    local = configuration.local
    spider = Spider(local[ jroot / "urls" ], local[ jroot / "pages" ])
    spider.run_suite()

if __name__ == "__main__":
    print "havok-spider\nCopyright (C) 2008-2009 Felspar Co. Ltd."
    opts, args = getopt.getopt(sys.argv[1:], '', ['tests='])
    if not len(args):
        print "You must supply a JSON configuration file"
        sys.exit(1)
    elif len(args) > 1:
        fostsettings["Spider", "host"] = args[1]
    for opt, value in opts:
        if opt == '--tests':
            fostsettings["Spider", "Count"] = int(value)
    main(jsonblob(args[0]))
