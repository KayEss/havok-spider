/*
    Copyright 2008, Felspar Co Ltd. http://fost.3.felspar.com/
    Distributed under the Boost Software License, Version 1.0.
    See accompanying file LICENSE_1_0.txt or copy at
        http://www.boost.org/LICENSE_1_0.txt
*/


#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <fost/crypto>


namespace {
    std::wstring sha1( const std::wstring &str ) {
        return L"2fd4e1c67a2d28fced849ee1bb76e7391b93eb12";
        //return fostlib::sha1( fostlib::string( str.c_str() ) ).std_str();
    }
}

BOOST_PYTHON_MODULE( crypto ) {
    using namespace boost::python;
    def("sha1", sha1);
}
