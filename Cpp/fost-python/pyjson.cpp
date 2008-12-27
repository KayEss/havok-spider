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
namespace bp = boost::python;


namespace {
    struct from_python {
        static void *convertible( PyObject *object );
        static void construct( PyObject *object, bp::converter::rvalue_from_python_stage1_data *data );
    private:
        static json to_json( bp::object o );
    };
}


void fostlib::python_json_registration() {
    bp::converter::registry::push_back(
        from_python::convertible, from_python::construct,
        bp::type_id< json >()
    );
}


void *from_python::convertible( PyObject *object ) {
    return object;
}
void from_python::construct( PyObject *object, bp::converter::rvalue_from_python_stage1_data *data ) {
    void *storage = reinterpret_cast<
        boost::python::converter::rvalue_from_python_storage< json >*
    >( data )->storage.bytes;
    if ( object == Py_None )
        new (storage) json();
    else {
        bp::handle<> h(object);
        new (storage) json( to_json( bp::object( h ) ) );
    }
    data->convertible = storage;
}
json from_python::to_json( bp::object o ) {
    if ( bp::extract< bool >( o ).check() )
        return json( bp::extract< bool >( o )() );
    else
        throw exceptions::not_implemented( L"from_python::to_json( boost::python::object )" );
}
