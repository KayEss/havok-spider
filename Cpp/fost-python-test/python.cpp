/*
    Copyright 2008-2016, Felspar Co Ltd. http://support.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/python>


using namespace fostlib;


string annotate( const string &s ) {
    return L"Passed in '" + s + L"'";
}
nullable< string > getnull() {
    return null;
}
bool isnone( const nullable< string > &s ) {
    return s.isnull();
}


BOOST_PYTHON_MODULE( _test ) {
    using namespace boost::python;
    python_string_registration();
    python_json_registration();

    def( "annotate", annotate );
    def( "getnull", getnull );
    def( "isnone", isnone );

    def("tojson", (string (*)(const json &, bool))json::unparse);
    def("fromjson", (json (*)(const string &))json::parse);
}
