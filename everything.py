#!/usr/bin/env python
# coding: utf-8

"""
When you want to just import *everything*.
"""

import types
import sys

class EverythingModule(types.ModuleType):

    def __getattr__(self, name):
        if name == '__all__':
            return [key for key in sys.modules
                    if len(key.split('.')) == 1]

        # Gotta put these imports in locals so that we don't recurse
        # infinitely in getattr.
        import __builtin__
        Missing = object()
        builtin = getattr(__builtin__, name, Missing)
        if builtin is not Missing:
            return builtin

        # Okay. Let's get down to business!
        import sys
        from importlib import import_module

        try:
            return import_module(name)
        except ImportError:
            raise NameError(name)

sys.modules['everything'] = EverythingModule('everything', __doc__)
