everything.py
=============

[![Build Status](https://travis-ci.org/eddieantonio/everything.py.svg)](https://travis-ci.org/eddieantonio/everything.py) [![Coverage Status](https://img.shields.io/coveralls/eddieantonio/everything.py.svg)](https://coveralls.io/r/eddieantonio/everything.py) 

When you just want to import *everything*.

Usage
-----

As a standard import:

```python
>>> import everything
>>> len(everything.sys.argv) > 0 and 'this works'
'this works'

```

Installed any other modules? Not to worry! Import those too:

```python
app = everything.flask.Flask(__name__)
app.run()
```

Have an irrational fear of `import <module>`. Soothe it with `everything`:

```python
>>> from everything import json
>>> json.dumps({'this_works': True})
'{"this_works": true}'

```

Use every pre-loaded module willy-nilly:

```python
>>> from everything import *
>>> isinstance(sys.argv, list) and 'this works too'
'this works too'

```

But it only works for *pre-loaded* modules!

```python
>>> from everything import *
>>> decimal.Decimal('0.01')
Traceback (most recent call last):
  ...
NameError: name 'decimal' is not defined

```

License
-------

                  DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                            Version 2, December 2004
    
      Copyright (C) 2014 Eddie Antonio Santos <easantos@ualberta.ca>
    
      Everyone is permitted to copy and distribute verbatim or modified
      copies of this license document, and changing it is allowed as long
      as the name is changed.
    
                  DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
        TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
    
      0. You just DO WHAT THE FUCK YOU WANT TO.

