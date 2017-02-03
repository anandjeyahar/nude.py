nude.py
=======

About
-----
This is a fork of _GitHub: https://github.com/hhatto/nude.py with some additions and changes.
Nudity detection with Python. Port of `nude.js`_ to Python.

.. _`nude.js`: https://github.com/pa7/nude.js


Installation
------------
from pip::

    $ pip install --upgrade nudepy

from easy_install::

    $ easy_install -ZU nudepy


Requirements
------------
* Python2.7+ and Python3.3+
* Pillow


Usage
-----
via command-line

.. code-block:: sh

    $ nudepy IMAGE_FILE

via Python Module

.. code-block:: python

    import nude
    from nude import Nude

    print(nude.is_nude('./nude.rb/spec/images/damita.jpg'))

    n = Nude('./nude.rb/spec/images/damita.jpg')
    n.parse()
    print("damita :", n.result, n.inspect())

see examples_ .

.. _examples: https://github.com/hhatto/nude.py/tree/master/examples

Links
-----
* PyPI_
* GitHub_

.. _PyPI: http://pypi.python.org/pypi/nudepy/


# My 2 paisas
* Improvements on the nude.py by hhatto/nude.py..
*  Adding a way to write custom sampling engine function to pass to the nude class to sample pixels

# ROADMAP:
* This is kinda obsolete. There is the [open_nsfw](https://github.com/yahoo/open_nsfw) which probably makes this look clownish.
* This is a very brute force approach. A more scalable approach would be either:
	a, Neural network trained approach or
	b, One approach could be extract SIFT features from a set of true and false nude images,
	and then training a neural network(which one?) and building a model.


