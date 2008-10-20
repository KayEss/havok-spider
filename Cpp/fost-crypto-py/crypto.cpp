/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <boost/python.hpp>
#include <fost/crypto>


namespace fostlib {

    bool operator ==( const fostlib::string &l, const boost::python::str &r ) {
        return r == l.c_str();
    }

}


BOOST_PYTHON_MODULE( crypto ) {
    using namespace boost::python;

    class_< fostlib::string >( "foststring", init< fostlib::native_string >() )
            .def( "length", &fostlib::string::length )
            .def( "__unicode__", &fostlib::string::std_str )
            .def( self == other< str >() )
        ;

    def( "sha1", fostlib::sha1 );

    implicitly_convertible< fostlib::native_string, fostlib::string >();
}
