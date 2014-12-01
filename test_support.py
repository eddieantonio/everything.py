"""
Test some things in the support library.
"""

from support import EverythingNamespace


def test_everything_namespace_as_globals():

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

def test_everything_namespace_as_locals():
    beth_gibbons = 'dummy'
    adrian_utley = 'portishead'

    namespace = EverythingNamespace(locals())

    # Sanity tests first....
    locals()['adrian_utley'] = 'guitar'
    assert adrian_utley == 'guitar'

    assert namespace['beth_gibbons'] is beth_gibbons
    namespace['beth_gibbons'] = 'vox'

    # Check that the assignment worked.
    assert beth_gibbons == 'vox'

    # Make sure it magically injects things into locals.
    namespace['geoff_barrow'] = 'devices'
    assert geoff_barrow

