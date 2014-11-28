everything.py
=============

[![Build Status](https://travis-ci.org/eddieantonio/everything.py.svg)](https://travis-ci.org/eddieantonio/everything.py) [![Coverage Status](https://img.shields.io/coveralls/eddieantonio/everything.py.svg)](https://coveralls.io/r/eddieantonio/everything.py) 

For when you want to import _everything_.

Usage
-----

```python
import everything
```

Then use... everything.

```python
>>> import everything
>>> everything.os.path.splitext('everything.py')
('everything', '.py')
>>> everything.token.tok_name[1]
'NAME'

```

Installed any other modules? Not to worry! Import those too:

```python
app = everything.flask.Flask(__name__)
app.run()
```

Have a inexpiable hatred of `import <module>` syntax? `everything` to
the rescue!

```python
from everything import this, dis # for rastafarian compatibility
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

