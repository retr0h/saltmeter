# saltmeter

Integration testing of a [salt](https://github.com/saltstack/salt) enduced
highstate.

## Usage

Toying around with ways to test the outcome of a salt highstate run.
Will likely add assertions as needed.

Import the library, and write unit tests by subclassing `saltmeter.TestCase`.

```python
from saltmeter import test_case as saltmeter

class TestCase(saltmeter.TestCase):
    ...
```

Assert a package installed (currently only supports Ubuntu):

```python
def test_assert_package_installed(self):
    self.assertPackageInstalled('curl')
```

Assert a file contains content:

```python
def test_assert_file_includes(self):
    self.assertFileIncludes(file, '^foo bar')
```

Assert a file's owner:

```python
def test_assert_file_owner(self):
    self.assertFileOwner(file, 1000)
```

Assert a file's group ownership:

```python
def test_assert_file_group(self):
    self.assertFileGroup(file, 1000)
```

Assert a file's permissions:

```python
def test_assert_file_mode(self):
    self.assertFileMode(file, 0640)
```

## License and Author

Author:: John Dewey (<john@dewey.ws>)

Copyright 2013, John Dewey

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
