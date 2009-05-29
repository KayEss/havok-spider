# -*- coding: utf-8 -*-
import unittest, urllib, urllib2, urlparse, random, cookielib
from BeautifulSoup import BeautifulSoup
from Fost.internet.useragent import agent

import Fost.settings
fostsettings = Fost.settings.database()

class Spider(object):
    def __init__(self, urls, visited):
        self.agent = agent()
        self.suite = unittest.TestSuite()
        self.pages = dict([(urlparse.urljoin(fostsettings["Spider", "host"], url), v) for url, v in visited.items()])
        [self.spider_test(urlparse.urljoin(fostsettings["Spider", "host"], url)) for url in urls]

    def url_data(self, url):
        if url.find('?') > 0:
            url = url[:url.find('?')]
        if not self.pages.has_key(url):
            self.pages[url] = dict()
        if not self.pages[url].has_key('remaining'):
            self.pages[url]['remaining'] = 1
        return self.pages[url]

    def run_suite(self):
        unittest.TextTestRunner().run(self.suite)

    def spider_test(spider, url, data=None):
        if spider.suite.countTestCases() < fostsettings["Spider", "Count"] and spider.url_data(url)['remaining']:
            if spider.url_data(url)['remaining']: spider.url_data(url)['remaining'] -= 1
            class Test(unittest.TestCase):
                def fetch(self, fetch, data = None):
                    try:
                        response = spider.agent.fetch(fetch, data)
                        if response.url != url and spider.url_data(url)['remaining']:
                            self.url_data(url)['remaining'] -= 1
                        if response.headers['Content-Type'].split(';')[0] == 'text/html':
                            response.soup = BeautifulSoup(response.read())
                        else:
                            response.soup = BeautifulSoup('')
                        return response
                    except urllib2.HTTPError, e:
                        if int(str(e).split()[2][0:3]) == spider.pages[fetch].get('status', 200):
                            # This is OK -- the status matches what we're expecting
                            class response(object):
                                soup = BeautifulSoup('')
                                url = fetch
                            return response()
                        elif data:
                            self.assert_(False, u"HTTP error with POST against %s with data\n%s\nBase URL %s\n%s" % (fetch, e, url, data))
                        elif data == "":
                            self.assert_(False, u"HTTP error with POST against %s with empty data\n%s\nBase URL %s" % (fetch, e, url))
                        else:
                            self.assert_(False, u"HTTP error with GET against %s\n%s\nBase URL %s" % (fetch, e, url))
                def queue_links(self, response):
                    soup = response.soup
                    # Check links in a random order
                    links = soup.findAll('a')
                    random.shuffle(links)
                    for link in links:
                        if link.has_key('href') and not link['href'].startswith('http') and not link['href'].startswith('/__'):
                            spider.spider_test(urlparse.urljoin(response.url, link['href']))
                    return soup
                def process(self, response):
                    soup = self.queue_links(response)
                    # Look for forms to submit
                    if spider.url_data(response.url).get('use_forms', True):
                        for form in soup.findAll('form'):
                            submit, query = build_form_query(self, form, response.url)
                            if spider.url_data(response.url).has_key('data'):
                                for k, v in spider.url_data(response.url)['data'].items():
                                    query[k] = v
                            if submit:
                                if form.get('method', 'get').lower() == 'get':
                                    spider.spider_test(urlparse.urljoin(response.url, u'%s?%s' % (form['action'], urllib.urlencode(query))))
                                else:
                                    self.queue_links(self.fetch(urlparse.urljoin(response.url, form['action']), urllib.urlencode(query)))
                def runTest(self):
                    self.process(self.fetch(url, data))
            spider.suite.addTest(Test())


def test_response(test, response):
    if response.status_code in [301, 302, 303]:
        response_location = response['Location']
        if 'https' in response_location:
            raise Exception("Need to turn off the HTTPS middleware")
        response_location = response_location[response_location.find('/office'):]
        if '?' in response_location:
            location, qstring = response_location.split('?')
            qstring = qstring.split('&')
            query = {}
            for qpart in qstring:
                if qpart:
                    key, value = qpart.split('=')
                    query[key] = value
            print '->', location, query
            test_response(test, test.client.get(location, query))
        else:
            print '->', response_location
            test_response(test, test.client.get(response_location))
            print '-> POST', response_location
            test_response(test, test.client.post(response_location))
    else:
        test.assert_(response.status_code in [200], "Incorrect response status of %s" % response.status_code)
    return response


def build_form_query(test, form, base_url):
    query, submits, radios = {}, [], {}
    test.assert_(form.has_key('action') and form['action'], u'Empty action in %s' % form)
    for ta in form.findAll('textarea'):
        test.assert_(ta.has_key('name'), u'%s in %s' % (ta, base_url))
        test.assert_(len(ta.contents) <= 1, u"Content of a textarea should just be some text\n" % ta.contents)
        if len(ta.contents) == 1:
            [query[ta['name']]] = ta.contents
    for inp in form.findAll('input'):
        if inp['type'] == "submit":
            submits.append(inp)
        elif inp['type'] == "checkbox":
            if inp.has_key('checked') and not inp.get('disabled', 'false').lower() == 'true':
                query[inp['name']] = inp.get('value', "")
        elif not inp['type'] == "reset":
            test.assert_(inp.has_key('name'), u'%s in %s' % (inp, base_url))
            query[inp['name']] = inp.get('value', "")
    for select in form.findAll('select'):
        test.assert_(select.has_key('name'), u'Select in form at %s has no name\n%s' % (base_url, select))
        options = select.findAll('option')
        test.assert_(len(options), u"No options found in select at %s" % base_url)
        for option in options:
            test.assert_(option.has_key('value'), u'No value found for option %s in select at %s' % (option, base_url))
            query[select['name']] = option['value']
    if len(submits):
        button = submits[random.randint(0, len(submits) - 1)]
        if button.has_key('name'):
            query[button['name']] = button['value']
        return True, query
    return False, query


def main(config_file=None, host=None, **kwargs):
    """
        This spider will start off running queries that it finds in a JSON configuration file.
    """
    print "Havok spider - Copyright (C) 2008-2009 Felspar Co Ltd."
    # Load configuration
    from Fost.json import root as jroot, jsonblob
    if config_file:
        configuration = jsonblob(config_file)
    else:
        configuration = jsonblob()
    local = configuration.local
    # Base URL configuration
    if local.has_key(jroot/"url"):
        fostsettings["Spider", "host"] = local[jroot/"url"]
    if host:
        fostsettings["Spider", "host"] = host
    # Number of tests configuration
    if local.has_key(jroot/"count"):
        fostsettings["Spider", "Count"] = local[jroot/"count"]
    if kwargs.has_key('t'):
        fostsettings["Spider", "Count"] = int(kwargs['t'])
    # Make spider and run
    spider = Spider(
        local[ jroot / "urls" ] if local.has_key(jroot/"urls") else ['/'],
        local[ jroot / "pages" ] if local.has_key(jroot/"pages") else {}
    )
    if local.has_key(jroot/'fost_authentication'):
        spider.agent.fost_authenticate(
            local[jroot/'fost_authentication'/'key'], local[jroot/'fost_authentication'/'secret'],
            local[jroot/'fost_authentication'/'headers']
        )
    spider.run_suite()
