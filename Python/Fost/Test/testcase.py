# Copyright (C) 2008 Felspar
#
# Test case helpers

import unittest
import time
import Settings.Selenium
from Fost.Test.selenium import selenium
from Fost.Test.prototype import Prototype


class SeleniumTest(unittest.TestCase):
    def __init__(self, arg1):
        unittest.TestCase.__init__(self, arg1)
        self.site_url = Settings.Selenium.site_url
        self.context = Prototype(Prototype.root, {})

    def disambiguator(self):
        return time.strftime("%y%j%H%M%S", time.gmtime())

    def get_user(self, disambig):
        return Prototype(FSLib.RegisteredUser.prototype, { \
                'email': FSLib.RegisteredUser.prototype.fetch('email').replace('@', '+' + disambig + '@'), \
            })


    def setUp(self):
        Settings.Selenium.start()
        self.selenium = Settings.Selenium.selenium

    def tearDown(self):
        Settings.Selenium.stop()

