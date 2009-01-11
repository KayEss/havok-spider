import sys, getopt, unittest, urllib, urllib2, cookielib
from Fost.json import root as jroot, jsonblob
from Fost.Test import spider

import Fost.settings
fostsettings = Fost.settings.database()

# Base settings
fostsettings[("Spider", "host")] = "http://localhost/"
fostsettings[("Spider", "Count")] = 25

# Install a cookie jar so we can have cookies
cj = cookielib.LWPCookieJar()
urllib2.install_opener(urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)))

def main(configuration, options):
    suite = unittest.TestSuite()
    for url in configuration.local[ jroot / "urls" ]:
        tofetch = "%s%s" % (
            fostsettings[("Spider", "host")],
            url['url']
        )
        if url.has_key('data'):
            class FormTest(unittest.TestCase):
                def runTest(self):
                    from BeautifulSoup import BeautifulSoup
                    soup = BeautifulSoup(urllib2.urlopen(tofetch).read())
                    submit, query = spider.build_form_query(self, soup.find('form'), tofetch)
                    for k, v in url['data'].items():
                        query[k] = v
                    if url.has_key('location'):
                        self.assertEqual(
                            urllib2.urlopen(tofetch, urllib.urlencode(query)).url,
                            "%s%s" % (
                                fostsettings[("Spider", "host")],
                                url['location']
                            )
                        )
            suite.addTest(FormTest())
        else:
            spider.spider_test(suite, tofetch)
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    print "havok-spider\nCopyright (C) 2008-2009 Felspar Co. Ltd."
    opts, args = getopt.getopt(sys.argv[1:], '', [])
    if len(args) > 1:
        fostsettings[("Spider", "host")] = args[1]
    main(jsonblob(args[0]), **dict(options=opts))
