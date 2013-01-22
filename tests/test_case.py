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

from saltmeter import test_case as saltmeter


class TestCase(saltmeter.TestCase):
    def setUp(self):
        self._file = os.path.join(os.path.dirname(__file__), 'file.txt')

    def test_assert_package_installed(self):
        self.assertPackageInstalled('curl')

    def test_assert_package_not_installed(self):
        with self.assertRaises(AssertionError):
            self.assertPackageInstalled('invalid-package-name')

    def test_assert_file_includes(self):
        self.assertFileIncludes(self._file, '^foo bar')

    def test_assert_invalid_file_includes(self):
        with self.assertRaises(AssertionError):
            self.assertFileIncludes(self._file, 'not found') 

    def test_assert_file_includes_raises_on_non_existent_file(self):
        with self.assertRaises(IOError):
            self.assertFileIncludes('non-existent', '^foo bar')

    def test_assert_file_owner(self):
        self.assertFileOwner(self._file, 1000)

    def test_assert_invalid_file_owner(self):
        with self.assertRaises(AssertionError):
            self.assertFileMode(self._file, 666)

    def test_assert_file_group(self):
        self.assertFileGroup(self._file, 1000)

    def test_assert_invalid_file_mode(self):
        with self.assertRaises(AssertionError):
            self.assertFileGroup(self._file, 666)

    def test_assert_file_mode(self):
        self.assertFileMode(self._file, 0640)

    def test_assert_invalid_file_mode(self):
        with self.assertRaises(AssertionError):
            self.assertFileMode(self._file, 0700)
