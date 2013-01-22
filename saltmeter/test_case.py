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

import os

import unittest2 as unittest

from saltmeter import package


class TestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        self._clazz = self._get_package_class()
        super(unittest.TestCase, self).__init__(methodName)

    def _get_package_class(self):
        """
        Determine and return the package subclass to use.
        """
        class_map = {
            'ubuntu': package.UbuntuPackage()
        }
        p = package.Package()
        platform = p._get_platform()
        return class_map.get(platform)

    def assertPackageInstalled(self, expected):
        """
        Determine if the given package is installed, and return a boolean
        assertion.

        :param expected: A string containing the name of the package.
        """
        result = self._clazz.get_package(expected)
        if result is True:
            self.assertTrue(True)
        else:
            msg = 'Could not find {0}'.format(expected)
            self.assertTrue(False, msg=msg)

    def assertFileExists(self):
        pass

    def assertFileIncludes(self, file, expected):
        """
        Determine if the given file matches the expected regex, and return
        a match assertion.

        :param file: A string containing the path to a file.
        :param expected: A string containing a regex.
        """
        try:
            with open(file, 'r') as fh:
                content = fh.read()
                self.assertRegexpMatches(content, expected)
        except IOError:
            raise

    def assertFileOwner(self, file, expected):
        """
        Determine if the given file's owner matches the expected owner,
        and return an assertion.

        :param file: A string containing the path to a file.
        :param expected: An integer containing the file's UID.
        """
        st = os.stat(file).st_uid
        self.assertEquals(expected, st)

    def assertFileGroup(self, file, expected):
        """
        Determine if the given file's group matches the expected group,
        and return an assertion.

        :param file: A string containing the path to a file.
        :param expected: An integer containing the file's GID.
        """
        st = os.stat(file).st_gid
        self.assertEquals(expected, st)

    def assertFileMode(self, file, expected):
        """
        Determine if the given file's permissions match the expected
        permissions, and return an assertion.

        :param file: A string containing the path to a file.
        :param expected: A 4-digit octal number.
        """
        st = os.stat(file)
        sm = oct(st.st_mode & 07770)
        self.assertEquals(oct(expected), sm)
