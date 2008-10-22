/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#ifndef FOST_PYBIND_HPP
#define FOST_PYBIND_HPP


#include <boost/python.hpp>
#include <fost/core>


namespace fostlib {


    struct to_pystr {
        static PyObject *convert( const string &s ) {
            std::wstring u( coerce< std::wstring >( s ) );
            return PyUnicode_FromWideChar( u.c_str(), u.length() );
        }
        static PyTypeObject const* get_pytype() {
            return &PyUnicode_Type;
        }
    };


}


#endif // FOST_PYBIND_HPP
