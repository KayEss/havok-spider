#!/usr/bin/env python
import base64
import http.cookiejar
import datetime
import hashlib
import hmac
import urllib.request, urllib.error, urllib.parse
import urllib.parse


def sha1_hmac(secret, document):
    k = bytes(secret, "utf-8")
    m = bytes(secret, "utf-8")
    d = hmac.new(k, m, hashlib.sha1)
    s = d.digest()
    b64 = base64.b64encode(s)
    return str(b64, "utf-8")


def fetch(*args, **kwargs):
    return agent().fetch(*args, **kwargs)


class agent(object):
    def __init__(self, base="http://localhost/", stop_redirects=True):
        self.url = base
        # Fost settings for authentication
        self.fost = {}
        # Enable cookie jar
        self.cj = http.cookiejar.LWPCookieJar()

        chain_of_responsibility = []
        if stop_redirects:
            class RedirectStop(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, req, fp, code, msg, hdrs, newurl):
                    return None
            chain_of_responsibility.append(RedirectStop())
        chain_of_responsibility.append(
            urllib.request.HTTPCookieProcessor(self.cj)
        )

        self.opener = urllib.request.build_opener(
            *chain_of_responsibility
        )

    def fost_authenticate(self, key, secret, headers = None):
        self.fost.update(
            key = key,
            secret = secret,
            headers = headers or {}
        )

    def fetch(self, url, data = None, headers = None):
        """
            Fetches a single URL using either GET or POST depending on whether
            a body (data) is present
        """
        if not headers:
            headers = {}
        self.url = urllib.parse.urljoin(self.url, url)
        if len(self.fost):
            signed, signed_headers = 'X-FOST-Headers', []
            for header, value in list(self.fost['headers'].items()):
                signed += ' ' + header
                signed_headers.append(value)
                headers[ header ] = value
            utcnow = str(datetime.datetime.utcnow())
            path = urllib.parse.urlsplit(self.url).path
            document = '%s %s\n%s\n%s\n%s' % (
                "POST" if data else "GET", path,
                utcnow,
                '\n'.join([signed] + signed_headers),
                data or urllib.parse.urlsplit(self.url).query
            )
            headers['X-FOST-Timestamp'] = utcnow
            headers['X-FOST-Headers'] = signed
            headers['Authorization'] = "FOST %s:%s" % (
                self.fost['key'],
                sha1_hmac(self.fost['secret'], document)
            )
            #print document
        return self.opener.open(urllib.request.Request(self.url, data, headers))

    def process(self, url, configuration = {}, data = None):
        """
            Processes a JSON request configuration starting at the specified
            URL with the specified body
        """
        try:
            #print "Configuration", configuration
            #print "Data", data
            from BeautifulSoup import BeautifulSoup
            response = self.fetch(url, data, configuration.get("headers", {}))
            response.mime_type = response.headers.get('Content-Type', ';').split(';')[0]
            response.body = response.read()
            if configuration.get("parse_result", True) and response.mime_type.startswith('text'):
                if response.body.startswith("<!DOC"):
                    response.soup = BeautifulSoup(
                        response.body[response.body.find(">")+1:])
                else:
                    response.soup = BeautifulSoup(response.body)
            else:
                response.soup = BeautifulSoup('')
            return response
        except urllib.error.HTTPError as e:
            status = int(str(e).split()[2][0:3])
            if status in configuration.get('status', [200, 301, 302, 303]):
                # This is OK -- the status matches what we're expecting
                class response(object):
                    status_code = status
                    soup = BeautifulSoup('')
                    body = ''
                    def __init__(self, u):
                        self.url = u
                return response(url)
            raise
