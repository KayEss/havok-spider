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

    try {
        // We need these two to provide context for the scripts
        boost::python::object main_module( boost::python::import( "__main__" ) );
        boost::python::object main_namespace( main_module.attr( "__dict__" ) );

        // Run the file so that we get a main to execute
        boost::python::exec_file( fostlib::coerce< std::string >( args[ 1 ].value() ).c_str(), main_namespace, main_namespace );

        // Build the argument list
        boost::python::list main_args;
        for ( std::size_t p( 2 ); p < args.size(); ++p )
            main_args.append( fostlib::coerce< boost::python::str >( args[ p ] ) );

        // Build the command line switches
        boost::python::dict switches;
        for ( std::map< fostlib::string, fostlib::string >::const_iterator p( args.switches().begin() ); p != args.switches().end(); ++p )
            switches[ fostlib::coerce< boost::python::str >( p->first ) ] = fostlib::coerce< boost::python::str >( p->second );

        // Find main and call it through a lambda to handle the arguments for us
        boost::python::object main_func = main_namespace[ "main" ];
        boost::python::eval( "lambda f, a, k: f(*a, **k)" )( main_func, main_args, switches );
    } catch ( boost::python::error_already_set const & ) {
        PyErr_Print();
    }

    return 0;
}
