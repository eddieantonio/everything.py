"""
Test some things in the support library.
"""

from support import EverythingNamespace

def test_everything_namespace():

    namespace = EverythingNamespace(globals())
    
    # Check if some globals are in there.
    assert namespace['__file__'] == __file__
    assert namespace['__doc__'] == __doc__

    # Make sure some modules are in there.
    import os
    assert namespace['os'] is os
    assert isinstance(getattr(namespace['token'], 'tok_name'), dict)
    # Now I'm just playin' around...
    assert 0 < getattr(namespace['decimal'], 'Decimal')('0.01') < 1

