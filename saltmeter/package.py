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

import platform
import subprocess

from saltmeter import utils


class Package(object):
    def __init__(self):
        self._platform = self._get_platform()

    def get_package(self):
        raise NotImplementedError

    def _get_platform(self):
        """
        Determine and return the name of the Linux OS distribution name.
        """
        return platform.linux_distribution()[0].lower()


class UbuntuPackage(Package):
    def __init__(self):
        pass

    def get_package(self, package):
        """
        Determine if the given package is installed, and return a boolean.

        :param package: A string containing the name of the package.
        """
        cmd = 'dpkg -s {0}'.format(package)
        return utils.Utils().execute(cmd)

# Platform Family...
# ('Ubuntu', '12.10', 'quantal')
# Debian
# CentOS
