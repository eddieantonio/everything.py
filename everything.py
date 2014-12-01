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

Have an irrational fear of `import <module>`. Soothe it with
`everything`::

    >>> from everything import json
    >>> json.dumps({'this_works': True})
    '{"this_works": true}'

Use every pre-loaded module willy-nilly::

    >>> from everything import *
    >>> isinstance(sys.argv, list) and 'this works too'
    'this works too'

But it only works for *pre-loaded* modules::

    >>> from everything import *
    >>> decimal.Decimal('0.01')
    Traceback (most recent call last):
        ...
    NameError: name 'decimal' is not defined

"""

import sys
import types


class EverythingModule(types.ModuleType):
    # Once I'm in this module, I can't trust the global namespace, so
    # ALL imports are done as globals in every single method.  :/

    def __getattr__(self, name):
        import sys
        # Hack! Return all base module names that are currently loaded.
        if name == '__all__':
            return [key for key in sys.modules if len(key.split('.')) == 1]

        from support import everything_dict
        # Try to get it from the EVERYTHING dict.
        try:
            return everything_dict[name]
        except KeyError:
            raise AttributeError(name)

sys.modules[__name__] = EverythingModule('everything', __doc__)
