#!/usr/bin/env python
# coding: utf-8

"""
Since `from <mod> import *` are not allowed in functions in Python 3
this file deals with tests that use `from everything import *` exclusivly.
"""

import pytest

from everything import *


def test_loaded_module():
    # That all of this works is a test in itself.
    assert isinstance(sys.argv, list)


@pytest.mark.xfail(reason="Not implemented")
def test_use_obscure_module():
    import sys
    assert 'Tkinter' not in sys.modules

    # It will be magically loaded on this line:
    assert Tkinter.Tcl()
