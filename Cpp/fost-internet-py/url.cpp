/*
    Copyright 2009, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include "url.hpp"


using namespace fostlib;


std::string url_filespec_encode( const fostlib::string &s ) {
    return coerce< url::filepath_string >( s ).underlying().underlying();
}
void url_filespec_assert_valid( const fostlib::string &s ) {
    url::filepath_string_tag::check_encoded( ascii_string( coerce< utf8string >( s ) ) );
}


std::string x_www_form_urlencoded( const json &j ) {
    url::query_string qs;
    for ( json::const_iterator i = j.begin(); i != j.end(); ++i )
        qs.append( coerce< string >( i.key() ), coerce< string >( *i ) );
    return qs.as_string().value( ascii_string() ).underlying();
}


fostlib::string url_to_fostlib_string(const url &u) {
    return coerce< string >( u );
}


string ua_response_body(const http::user_agent::response &response) {
    const mime &body = response.body();
    if ( dynamic_cast< const text_body * >( &body ) )
        return dynamic_cast< const text_body & >( body ).text();
    else
        throw exceptions::not_implemented("ua_response_body(const http::user_agent::response &response) for non text responses");
}
