/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/pybind.hpp>
#include "connection.hpp"
#include "jsonblob.hpp"


using namespace fostlib;


BOOST_PYTHON_MODULE( _jsondb ) {
    using namespace boost::python;
    fostlib::string_registration();

    class_< jsonblob >( "jsonblob", init<>() )
        .def( init< nullable< string > >() )
        .def( init< nullable< string >, nullable< string > >() )

        .add_property("filename", &jsonblob::filename_)
    ;
}
