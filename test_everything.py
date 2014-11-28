#!/usr/bin/env python
"""
Tests everything about `everything`.

...but you probably already figured that out.

"""

import pytest

from types import ModuleType


def test_import():
    import everything

    assert isinstance(everything, ModuleType)


def test_builtins():
    import everything

    assert everything.enumerate


def test_imports_stdlib():
    import pickle
    import everything

    assert pickle is everything.pickle


def test_not_a_module_or_buitlin():
    import everything

    # Did you seriously install a module called fhqwhgads?
    with pytest.raises(ImportError):
        import fhqwhgads

    with pytest.raises(NameError):
        everything.fhqwhgads


def test_imports_other():
    import pip
    import everything

    assert pip is everything.pip
    assert pytest is everything.pytest


def test_import_recursive():
    import everything

    assert everything.xml.etree.ElementTree


def test_can_still_import():
    import everything

    # This is literally the test:
    import pickle
    assert pickle


def test_from_import():
    # Again, this is literally the test.
    from everything import dis, inspect

    # Just make sure some things exist...
    assert hasattr(dis, 'disassemble')
    assert hasattr(inspect, 'getmodule')


def test_documentation():
    import everything
    assert '\n' in everything.__doc__

# Since `from <mod> import *` are not allowed in functions in Python 3, so...
# secretely, this line is a test:
from everything import *
