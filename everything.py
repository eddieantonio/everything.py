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

import types
import sys


class EverythingModule(types.ModuleType):
    # Once I'm in this module, I can't trust the global namespace, so
    # ALL imports are done as globals in every single method.  :/

    def __getitem__(self, name):
        # Pretend we're a dictionary.
        return getattr(self, name)

    def __getattr__(self, name):
        import sys
        try:
            # The name of the Python 3 module:
            import builtins
        except ImportError:  # pragma: no cover
            import __builtin__ as builtins

        # Hack! Return all base module names that are currently loaded.
        if name == '__all__':
            return [key for key in sys.modules if len(key.split('.')) == 1]

        # Try to return a builtin.
        try:
            return getattr(builtins, name)
        except AttributeError:
            pass

        # Try to import the named module.
        try:
            builtins.__import__(name)
        except ImportError:
            raise NameError(name)
        else:
            return sys.modules[name]

    # Let's be a super sweet context managers.
    def __enter__(self):
        # This terribleness is inspired by:
        # https://code.google.com/p/ouspg/wiki/AnonymousBlocksInPython
        import sys
        import inspect

        # As __enter__ is called *before* the context manager is...
        # entered, we have to hook into the debug tracer, but only for
        # the context in which the code is running in!
        # https://docs.python.org/2/library/sys.html#sys.settrace

        # Give settrace a no-op so that we can install our own trace
        # handler.
        sys.settrace(lambda *args, **kwargs: None)

        # Get the calling stack frame and its current instruction
        # pointer. This is the scope of the with-statement.
        frame = inspect.currentframe(1)

        # Our trace handler that pops us into exit.
        def stop_tracing(frame, event, arg):
            from support import StopTracing
            # Disable ourselves...
            frame.f_trace = None

            # __exit__ will pick it up from here.
            raise StopTracing(frame)

        # Install our trace function.
        frame.f_trace = stop_tracing

    # Catches StopTracing and ONLY StopTracing!
    # Used to implemented the context manager hack.
    def __exit__(self, exc_type, exc_value, traceback):
        from support import StopTracing
        if exc_type is not StopTracing:
            # Some other exception. Have no idea how to deal with it
            # so... ¯(°_o)/¯
            return
        info = exc_value

        if not info.filename:
            raise SyntaxError('with-statement must be in a source file')

        import ast
        from support import WithBlockFinder

        # Get the tree of the source file.
        with open(info.filename) as source_file:
            tree = ast.parse(source_file.read(), mode='exec')

        # Figure out the with statement that called us.
        visitor = WithBlockFinder(info.lineno)
        visitor.visit(tree)

        # Now we should have a module!
        block_ast = ast.Module(visitor.result)
        assert block_ast is not None, 'Visitor did not find with-statement'

        block_code = compile(block_ast, info.filename, 'exec')

        # Exec it in its own locals, but inject self into globals.
        exec block_code in info.locals, self

        # Ignore the StopTracing error.
        return True

sys.modules[__name__] = EverythingModule('everything', __doc__)
