#!/usr/bin/env python
# coding: utf-8

"""
When you just want to import *everything*.

-----
Usage
-----

As a standard import::

    >>> import everything
    >>> len(everything.sys.argv) > 0 and 'this works'
    'this works'

Have an irrationl fear of `import <module>`. Sooth it with
`everything`::

    >>> from everything import json
    >>> json.loads('{"this_works": true}')['this_works']
    True

Use every pre-loaded module willy-nilly::

    >>> from everything import *
    >>> isinstance(sys.argv, list) and 'this works too'
    'this works too'

But only for *pre-loaded* modules::

    >>> from everything import *
    >>> Tkinter.Tcl()
    Traceback (most recent call last):
        ...
    NameError: global name 'Tkinter' is not defined

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
        except ImportError:  # pragma: no cover
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
