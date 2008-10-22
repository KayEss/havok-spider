/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include "settings.hpp"


settings::settings() {
}


fostlib::string settings::get( const fostlib::string &d, const fostlib::string &n ) {
    return setting_t::value( d, n );
}


void settings::set( const fostlib::string &d, const fostlib::string &n, const fostlib::string &v ) {
    database.push_back( store_t( new setting_t( L"fost.pybind.settings", d, n, v, false ) ) );
}
