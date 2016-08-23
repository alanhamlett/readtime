readtime
========

.. image:: https://travis-ci.org/alanhamlett/readtime.svg?branch=master
    :target: https://travis-ci.org/alanhamlett/readtime
    :alt: Tests

.. image:: https://coveralls.io/repos/github/alanhamlett/readtime/badge.svg?branch=master
    :target: https://coveralls.io/github/alanhamlett/readtime?branch=master
    :alt: Coverage

Calculates the time some text takes the average human to read, based on
Medium's `read time forumula <https://help.medium.com/hc/en-us/articles/214991667-Read-time>`_.


Installation
------------

::

    virtualenv venv
    . venv/bin/activate
    pip install readtime

Or if you like to live dangerously::

    sudo pip install readtime


Usage
-----

Import ``readtime`` and pass it some text, HTML, or Markdown to get back the
time it takes to read::

    >>> import readtime
    >>> result = readtime.of_text('The shortest blog post in the world!')
    >>> result.seconds
    2
    >>> result.text
    u'1 min'

The result can also be used as a string::

    >>> str(readtime.of_text('The shortest blog post in the world!'))
    u'1 min read'

To calculate read time of Markdown::

    readtime.of_markdown('This is **Markdown**')

To calculate read time of HTML::

    readtime.of_html('This is <strong>HTML</strong>')


Contributing
------------

Before contributing a pull request, make sure tests pass::

    virtualenv venv
    . venv/bin/activate
    pip install tox
    tox

Many thanks to all `contributors <https://github.com/alanhamlett/readtime/blob/master/AUTHORS>`_!
