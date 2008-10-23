/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/pybind.hpp>
#include "settings.hpp"


BOOST_PYTHON_MODULE( _settings ) {
    using namespace boost::python;

    class_<settings>("settings", init<>() )
        .def( "get", &settings::get )
        .def( "set", &settings::set )
    ;

    implicitly_convertible< fostlib::native_string, fostlib::string >();
    to_python_converter< fostlib::string, fostlib::to_pystr, false >();
}
