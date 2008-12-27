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
#include <fost/exception/out_of_range.hpp>


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
    struct to_nullable_pystr {
        static PyObject *convert( const nullable< string > &s ) {
            std::wstring u( coerce< std::wstring >( s.value() ) );
            return PyUnicode_FromWideChar( u.c_str(), u.length() );
        }
        static PyTypeObject const* get_pytype() {
            return &PyUnicode_Type;
        }
    };

    struct from_pystr {
        static void *convertible( PyObject *object ) {
            boost::python::handle<> unicode( PyUnicode_FromObject( object ) );
            if ( unicode )
                return object;
            else
                return NULL;
        }

        static void construct( PyObject *object, boost::python::converter::rvalue_from_python_stage1_data *data ) {
            boost::python::handle<> unicode( PyUnicode_FromObject( object ) );
            int len( PyUnicode_GetSize( unicode.get() ) );
            if ( len < 0 )
                throw exceptions::out_of_range< int >( L"Unicode length is not valid", 0, std::numeric_limits< int >::max(), len );
            boost::scoped_array< wchar_t > ustr( new wchar_t[ len + 1 ] );
            if ( int c = PyUnicode_AsWideChar( reinterpret_cast< PyUnicodeObject* >( unicode.get() ), ustr.get(), len ) != len )
                throw exceptions::out_of_range< int >( L"Could not get all of the Python string", len, len, c );
            ustr[ len ] = 0;
            // These lines look bad, but is apparently the way to do it
            void *storage = reinterpret_cast<
                boost::python::converter::rvalue_from_python_storage< string >*
            >( data )->storage.bytes;
            new (storage) string( ustr.get() );
            data->convertible = storage;
        }
    };
    struct from_nullable_pystr {
        static void *convertible( PyObject *object ) {
            boost::python::handle<> unicode( PyUnicode_FromObject( object ) );
            if ( unicode )
                return object;
            else
                return NULL;
        }

        static void construct( PyObject *object, boost::python::converter::rvalue_from_python_stage1_data *data ) {
            boost::python::handle<> unicode( PyUnicode_FromObject( object ) );
            int len( PyUnicode_GetSize( unicode.get() ) );
            if ( len < 0 )
                throw exceptions::out_of_range< int >( L"Unicode length is not valid", 0, std::numeric_limits< int >::max(), len );
            boost::scoped_array< wchar_t > ustr( new wchar_t[ len + 1 ] );
            if ( int c = PyUnicode_AsWideChar( reinterpret_cast< PyUnicodeObject* >( unicode.get() ), ustr.get(), len ) != len )
                throw exceptions::out_of_range< int >( L"Could not get all of the Python string", len, len, c );
            ustr[ len ] = 0;
            // These lines look bad, but is apparently the way to do it
            void *storage = reinterpret_cast<
                boost::python::converter::rvalue_from_python_storage< nullable< string > >*
            >( data )->storage.bytes;
            new (storage) nullable< string >( ustr.get() );
            data->convertible = storage;
        }
    };


    /*
        Call this inside the BOOST_PYTHON_MODULE function to enable fostlib::string handling
    */
    inline void string_registration() {
        using namespace boost::python;

        converter::registry::push_back(
            from_pystr::convertible, from_pystr::construct,
            type_id< string >()
        );
        converter::registry::push_back(
            from_nullable_pystr::convertible, from_nullable_pystr::construct,
            type_id< nullable< string > >()
        );
        to_python_converter< string, to_pystr, false >();
        to_python_converter< nullable< string >, to_nullable_pystr, false >();
    }


}


#endif // FOST_PYBIND_HPP
