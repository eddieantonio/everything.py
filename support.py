#!/usr/bin/env python

import ast
import sys

from collections import Mapping

class StopTracing(BaseException):

    """
    Raised by `everything` in the "real" context manager so that
    __exit__ can catch it and disregard it.

    This hack is based on:
    https://code.google.com/p/ouspg/wiki/AnonymousBlocksInPython
    """

    def __init__(self, frame):
        self.lineno = frame.f_lineno
        self.filename = frame.f_code.co_filename
        self.globals = frame.f_globals
        self.locals = frame.f_locals


class WithBlockFinder(ast.NodeVisitor):

    def __init__(self, lineno):
        self.first_stmt_lineno = lineno
        self.result = None

    def is_with_everything_node(self, node):
        first_stmt = node.body[0]
        return first_stmt.lineno != self.first_stmt_lineno

    def visit_With(self, node):
        assert len(node.body) >= 1

        # Is this the with statement?
        if self.is_with_everything_node(node):
            # Give up and resort to a generic visit; the wanted
            # with-stamement might be nested within.
            return self.generic_visit(node)

        # This is the desired with-statement!
        self.result = node.body


class EverythingDict(Mapping):
    """
    A dictionary of every importable top-level module.
    """

    def __getitem__(self, name):
        # Try to import the named module.
        try:
            __import__(name)
        except ImportError:
            raise KeyError(name)
        else:
            return sys.modules[name]

    def __iter__(self, name):
        return iter(())

    def __len__(self, name):
        raise NotImplemented

everything_dict = EverythingDict()

class EverythingNamespace(dict):
    """
    Wrap a namespace. If we get a KeyError in the given namespace, delegate to
    everything.
    """

    def __init__(self, namespace):
        self.namespace = namespace

    def __getitem__(self, name):
        # Try to return the item in the namespace first.
        try:
            return self.namespace[name]
        except KeyError:
            pass
        # Delegate to everything.
        return everything_dict[name]

    # Delegate the rest of these to the namespace.
    def __setitem__(self, name, value):
        self.namespace[name] = value
    def __delitem__(self, name):
        del self.namespace[name]
    def __len__(self):
        return len(self.namespace)
    def __iter__(self):
        return iter(self.namespace)

