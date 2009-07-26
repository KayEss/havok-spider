/*
    Copyright 2009, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/python>
#include "url.hpp"


using namespace fostlib;


BOOST_PYTHON_MODULE( _internet ) {
    using namespace boost::python;
    python_string_registration();
    python_json_registration();

    def( "url_filespec_encode", url_filespec_encode );
    def( "url_filespec_assert_valid", url_filespec_assert_valid );

    def( "x_www_form_urlencoded", x_www_form_urlencoded );
}
