# -*- coding: utf-8 -*-
# Copyright 2008-2009, Felspar Co Ltd. http://fost.3.felspar.com/
# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE_1_0.txt or copy at
#     http://www.boost.org/LICENSE_1_0.txt

import cookielib, datetime, urllib2, urlparse
from Fost.crypto import sha1_hmac
from Fost.settings import database
from _internet import url_filespec_encode


def fetch(*args, **kwargs):
    return agent().fetch(*args, **kwargs)


class agent(object):
    def __init__(self):
        # Fost settings for authentication
        self.fost = {}
        # Enable cookie jar
        self.cj = cookielib.LWPCookieJar()
        class RedirectStop(urllib2.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, hdrs, newurl):
                return None
        self.opener = urllib2.build_opener(RedirectStop(), urllib2.HTTPCookieProcessor(self.cj))

    def fost_authenticate(self, key, secret, headers = {}):
        self.fost['key'] = key
        self.fost['secret'] = secret
        self.fost['headers'] = headers

    def fetch(self, url, data = None, headers = {}):
        if len(self.fost):
            signed, signed_headers = 'X-FOST-Headers', []
            for header, value in self.fost['headers'].items():
                signed += ' ' + header
                signed_headers.append(value)
                headers[ header ] = value
            utcnow = unicode(datetime.datetime.utcnow())
            document = '%s %s\n%s\n%s\n%s' % (
                "POST" if data else "GET", url_filespec_encode(urlparse.urlsplit(url).path),
                utcnow,
                '\n'.join([signed] + signed_headers),
                data or urlparse.urlsplit(url).query
            )
            headers['X-FOST-Timestamp'] = utcnow
            headers['X-FOST-Headers'] = signed
            headers['Authorization'] = "FOST %s:%s" % (self.fost['key'], sha1_hmac(self.fost['secret'], document))
            #print document
        return self.opener.open(urllib2.Request(url, data, headers))
