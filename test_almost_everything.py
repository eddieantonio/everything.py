#!/usr/bin/env python
# coding: utf-8

"""
Tests almost everything about `everything`.

...but you probably already figured that out.

The only thing missing here are tests for `from everything import *`
which MUST be in their own module, due to it being a module-level
syntactic thing and messing with the globals in general. 
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
    import everything

    assert pytest is everything.pytest


@pytest.mark.xfail(run=False, reason="Not Implemented")
def test_import_recursive():
    import everything

    assert everything.xml.etree.ElementTree


def test_can_still_import():
    import everything

    # This is literally the test:
    import pickle
    assert pickle.loads


def test_from_import():
    # Again, this is literally the test.
    from everything import dis, inspect

    # Just make sure some things exist...
    assert hasattr(dis, 'disassemble')
    assert hasattr(inspect, 'getmodule')


@pytest.mark.xfail(reason="Not implemented")
def test_context_manager():
    import everything
    with everything:
        # Just do something random with a module.
        # I know for a fact that token.tok_name[1] is 'NAME' so...
        NAME_TOKEN = token.tok_name[1]

    # Gotta make sure that the local was assigned properly in the
    # with-statement.
    assert NAME_TOKEN == 'NAME'


def test_documentation():
    import everything
    assert '\n' in everything.__doc__
