 # Copyright (C) 2008 Felspar
#
# Tests for Fost.Test.prototype.py

from Fost.Test.prototype import *
import unittest


class TestPrototype(unittest.TestCase):
    def setUp(self):
        pass


    def testroot(self):
        self.assertEquals(Prototype.root.fetch('hello'), None)
        self.assertEquals(Prototype.root.fetch('world'), None)

    def testfirst(self):
        first = Prototype(Prototype.root,{'hello':'world'})
        self.assertEquals(first.fetch('hello'), 'world')
        self.assertEquals(first.fetch('world'), None)
        self.assertEquals(first.fetch('world', 'goodbye'), 'goodbye')

    def testsecond(self):
        first = Prototype(Prototype.root,{'hello':'world'})
        second = Prototype(first, {'world':'goodbye'})
        self.assertEquals(second.fetch('hello'), 'world')
        self.assertEquals(second.fetch('world'), 'goodbye')

    def testthird(self):
        first = Prototype(Prototype.root,{'hello':'world'})
        second = Prototype(first, {'world':'goodbye'})
        third = Prototype(second, {'world': None})
        self.assertEquals(third.fetch('hello'), 'world')
        self.assertEquals(third.fetch('world'), None)
        self.assertEquals(third.fetch('world', 'goodbye'), 'goodbye')


    def tearDown(self):
            pass


if __name__ == "__main__":
    unittest.main()

