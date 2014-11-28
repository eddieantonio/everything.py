#!/usr/bin/env python
# coding: utf-8

"""
When you want to just import *everything*.
"""

import types
import sys

class EverythingModule(types.ModuleType):

    def __getattr__(self, name):
        # Gotta put these imports in locals so that we don't recurse
        # infinitely in getattr.
        import sys
        try:
            import __builtin__
        except ImportError: # pragma: no cover
            # For Python 3 support...
            import builtins as __builtin__

        # Hack! Return all base module names that are currently loaded.
        if name == '__all__':
            return [key for key in sys.modules if len(key.split('.')) == 1]

        # Try to return a builtin.
        try:
            return getattr(__builtin__, name)
        except AttributeError:
            pass

        # Try to import the named module.
        try:
            __builtin__.__import__(name)
        except ImportError:
            raise NameError(name)
        else:
            return sys.modules[name]

sys.modules['everything'] = EverythingModule('everything', __doc__)
