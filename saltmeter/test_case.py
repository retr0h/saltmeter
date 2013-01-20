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

import unittest2 as unittest

from saltmeter import package


class TestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        self._clazz = self._get_package_class()
        super(unittest.TestCase, self).__init__(methodName)

    def _get_package_class(self):
        class_map = {
          'ubuntu': package.UbuntuPackage()
        }
        p = package.Package()
        platform = p._get_platform()
        return class_map.get(platform)

    def assertPackageInstalled(self, expected):
        result = self._clazz.get_package(expected)
        if result is True:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
