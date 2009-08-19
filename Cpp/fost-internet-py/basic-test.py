# -*- coding: utf-8 -*-
# Copyright 2009, Felspar Co Ltd. http://fost.3.felspar.com/
# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE_1_0.txt or copy at
#     http://www.boost.org/LICENSE_1_0.txt

import _internet

def check_throw(f, *args, **kwargs):
    threw = False
    try:
        f(*args, **kwargs)
    except:
        threw = True
    assert threw

assert _internet.url_filespec_encode("abc") == "abc"
assert _internet.url_filespec_encode("abc ") == "abc%20"
assert _internet.url_filespec_encode(u"abc ") == u"abc%20"

_internet.url_filespec_assert_valid("abc")
_internet.url_filespec_assert_valid("abc/def")
check_throw(_internet.url_filespec_assert_valid, "abc def")
_internet.url_filespec_assert_valid(u"abc/def")

assert _internet.x_www_form_urlencoded({}) == "", _internet.x_www_form_urlencoded({})
assert _internet.x_www_form_urlencoded({'a':12}) == "a=12", _internet.x_www_form_urlencoded({})
assert _internet.x_www_form_urlencoded({'a':'b'}) == "a=b", _internet.x_www_form_urlencoded({})

assert unicode(_internet.url()) == "http://localhost/", unicode(_internet.url())

request = _internet.ua_request("PUT", _internet.url())
assert request.method == "PUT", request.method
assert unicode(request.url) == "http://localhost/", unicode(request.url)

ua = _internet.user_agent()
response = ua(_internet.ua_request("HEAD", _internet.url("http://www.google.com/")))
assert unicode(response.url) == "http://www.google.com/", unicode(response.url)
assert response.method == "HEAD", response.method
assert response.protocol == "HTTP/1.0", response.protocol
assert response.status == 302, response.status
assert response.message == "Found", response.message

ua = _internet.user_agent(_internet.url())
