/*
    Copyright 2008-2017, Felspar Co Ltd. http://support.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/python>
#include <fost/crypto>


namespace {
    /// Now that these functions take a `u8view` and that isn't a type
    /// known to Python we're just going to wrap this stuff for now and
    /// deal with it properly for Python 3.
    fostlib::string md5(const fostlib::string &s) {
        return fostlib::md5(s);
    }
    fostlib::string sha1(const fostlib::string &s) {
        return fostlib::sha1(s);
    }
    fostlib::string sha1_hmac(const fostlib::string &s, const fostlib::string &k) {
        return fostlib::sha1_hmac(s, k);
    }
}


BOOST_PYTHON_MODULE(_crypto) {
    using namespace boost::python;
    fostlib::python_string_registration();

    def("md5", ::md5);
    def("sha1", ::sha1);
    def("sha1_hmac", ::sha1_hmac);
}

