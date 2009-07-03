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

_internet.url_filespec_asssert_valid("abc")
_internet.url_filespec_asssert_valid("abc/def")
check_throw(_internet.url_filespec_asssert_valid, "abc def")

assert _internet.x_www_form_urlencoded({}) == "", _internet.x_www_form_urlencoded({})
assert _internet.x_www_form_urlencoded({'a':12}) == "a=12", _internet.x_www_form_urlencoded({})
assert _internet.x_www_form_urlencoded({'a':'b'}) == "a=b", _internet.x_www_form_urlencoded({})
