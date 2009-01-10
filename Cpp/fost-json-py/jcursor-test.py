# Copyright 2009, Felspar Co Ltd. http://fost.3.felspar.com/
# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE_1_0.txt or copy at
#     http://www.boost.org/LICENSE_1_0.txt

import _json

# Basic constructor
j1 = _json.jcursor()

# Add to the path of the jcursor
j1 /= "path"
