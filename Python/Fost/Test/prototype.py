# Copyright (C) 2008 Felspar
#
# Prototypal inheritance for setting test data


class Prototype:
    def __init__(self, parent, prototype):
        self.__parent = parent
        self.__prototype = prototype

    def fetch(self, key, default=None):
        if self.__prototype.has_key(key):
            if self.__prototype[key] == None:
                return default
            else:
                return self.__prototype[key]
        elif self.__parent != None:
            return self.__parent.fetch(key, default)
        else:
            return default

Prototype.root = Prototype(None, {})
