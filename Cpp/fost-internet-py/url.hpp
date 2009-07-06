/*
    Copyright 2009, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/inet>


std::string url_filespec_encode( const fostlib::string &s );
void url_filespec_assert_valid( const std::string &s );

std::string x_www_form_urlencoded( const fostlib::json &j );
