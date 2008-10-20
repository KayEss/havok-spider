/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <boost/python.hpp>
#include <fost/crypto>


namespace {
    struct to_pystr {
        static PyObject *convert( const fostlib::string &s ) {
            std::wstring u( fostlib::coerce< std::wstring >( s ) );
            return PyUnicode_FromWideChar( u.c_str(), u.length() );
        }
        static PyTypeObject const* get_pytype() {
            return &PyUnicode_Type;
        }
    };
}


BOOST_PYTHON_MODULE( crypto ) {
    using namespace boost::python;

    def( "sha1", fostlib::sha1 );

    implicitly_convertible< fostlib::native_string, fostlib::string >();
    to_python_converter< fostlib::string, to_pystr, false >();
}
