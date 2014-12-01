#!/usr/bin/env python

import ast

# Context manager hacks based on
# https://code.google.com/p/ouspg/wiki/AnonymousBlocksInPython


class StopTracing(BaseException):

    """
    Raised by `everything` in the "real" context manager so that
    __exit__ can catch it and disregard it.

    Called with the instruction pointer of the frame we're munging with.
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
