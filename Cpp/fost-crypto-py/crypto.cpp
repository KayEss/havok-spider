/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <fost/pybind.hpp>
#include <fost/crypto>


BOOST_PYTHON_MODULE( _crypto ) {
    using namespace boost::python;

    def( "md5", fostlib::md5 );
    def( "sha1", fostlib::sha1 );
    def( "sha1_hmac", fostlib::sha1_hmac );

    implicitly_convertible< fostlib::native_string, fostlib::string >();
    boost::python::converter::registry::push_back(
        fostlib::from_pystr::convertible, fostlib::from_pystr::construct,
        boost::python::type_id< fostlib::string >()
    );
    to_python_converter< fostlib::string, fostlib::to_pystr, false >();
}
