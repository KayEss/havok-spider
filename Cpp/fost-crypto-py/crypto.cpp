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
    std::string sha1( const std::string &str ) {
        return fostlib::sha1( fostlib::string( str ) ).std_str();
    }
}

BOOST_PYTHON_MODULE( crypto ) {
    using namespace boost::python;
    def("sha1", sha1);
}
