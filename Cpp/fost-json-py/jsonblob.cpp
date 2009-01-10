/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include "jsonblob.hpp"


using namespace fostlib;


nullable< string > filename( const jsondb &db ) {
    return db.filename();
}
std::auto_ptr< jsondb::local > get_local( jsondb &db ) {
    return std::auto_ptr< jsondb::local >( new jsondb::local( db, jcursor() ) );
}

json get_json( const jsondb::local &db ) {
    return db[ jcursor() ];
}
bool fostlib::operator ==( const jsondb::local &db, const json &j ) {
    return get_json( db ) == j;
}
