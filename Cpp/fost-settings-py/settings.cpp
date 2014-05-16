/*
    Copyright 2008-2014, Felspar Co Ltd. http://support.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include "settings.hpp"


namespace {


#ifdef WIN32
    const fostlib::setting< fostlib::string > s_machine_config( L"fost-settings-py", L"settings-py", L"Machine configuration", L"%WINDIR%\\fost.ini", true );
#else
    const fostlib::setting< fostlib::string > s_machine_config( L"fost-settings-py", L"settings-py", L"Machine configuration", L"/etc/fost.conf", true );
#endif
    const fostlib::setting< bool > s_reload( L"fost-settings-py", L"settings-py", L"Reload machine configuration", true, true );


}


settings::settings() {
    if ( s_reload.value() ) {
        database.push_back( store_t( new setting_t( s_reload.domain(), s_reload.section(), s_reload.name(), true, false ) ) );
        ini_database.push_back( ini_store_t( new ini_settings_t( s_machine_config.value() ) ) );
    }
}


void settings::file( const fostlib::string &location ) {
    ini_database.push_back( ini_store_t( new ini_settings_t( location ) ) );
}


fostlib::json settings::get( const fostlib::string &d, const fostlib::string &n ) const {
    return fostlib::setting< fostlib::json >::value( d, n );
}


void settings::set( const fostlib::string &d, const fostlib::string &n, const fostlib::json &v ) {
    database.push_back( store_t( new setting_t( L"fost.pybind.settings", d, n, v, false ) ) );
}


bool settings::has_key( const fostlib::string &d, const fostlib::string &n ) const {
    return fostlib::setting< fostlib::json >::exists( d, n );
}

