# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013, John Dewey
# All Rights Reserved.

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import subprocess

import unittest2 as unittest

from saltmeter import package


class TestPackage(unittest.TestCase):
    def test_get_package(self):
        with self.assertRaises(NotImplementedError):
            p = package.Package()
            p.get_package()

    def test_get_platform(self):
        p = package.Package()
        result = p._get_platform()
        self.assertEquals('ubuntu', result)


class TestUbuntuPackage(unittest.TestCase):
    def test_get_package_has_package(self):
        p = package.UbuntuPackage()
        result = p.get_package('curl')
        self.assertEquals(True, result)

    def test_get_package_doesnt_have_package(self):
        p = package.UbuntuPackage()
        result = p.get_package('invalid-package-name')
        self.assertEquals(False, result)
