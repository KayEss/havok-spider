/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include "fost-python.hpp"
#include <fost/pybind.hpp>

#include <fost/exception/not_implemented.hpp>


using namespace fostlib;


namespace {
    struct from_python {
        static void *convertible( PyObject *object );
        static void construct( PyObject *object, boost::python::converter::rvalue_from_python_stage1_data *data );
    };
}


void fostlib::python_json_registration() {
    using namespace boost::python;

    converter::registry::push_back(
        from_python::convertible, from_python::construct,
        type_id< json >()
    );
}


void *from_python::convertible( PyObject *object ) {
    return object;
}
void from_python::construct( PyObject *object, boost::python::converter::rvalue_from_python_stage1_data *data ) {
    void *storage = reinterpret_cast<
        boost::python::converter::rvalue_from_python_storage< json >*
    >( data )->storage.bytes;
    if ( object == Py_None )
        new (storage) json();
    else {
        throw exceptions::not_implemented( L"from_python::construct( PyObject *object, boost::python::converter::rvalue_from_python_stage1_data *data )" );
    }
    data->convertible = storage;
}
