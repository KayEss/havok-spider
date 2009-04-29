/*
    Copyright 2009, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/cli>
#include <fost/main.hpp>
#include <fost/python>


FSL_MAIN(
    L"fpython",
    L"fpython\nCopyright (c) 2009 Felspar Co. Ltd."
)( fostlib::ostream &out, fostlib::arguments &args ) {
    Py_Initialize();
    fostlib::python_string_registration();
    fostlib::python_json_registration();

    boost::python::object main_module( boost::python::import( "__main__" ) );
    boost::python::object main_namespace( main_module.attr( "__dict__" ) );

    boost::python::exec_file( fostlib::coerce< std::string >( args[ 1 ].value() ).c_str(), main_namespace, boost::python::dict() );

    return 0;
}
