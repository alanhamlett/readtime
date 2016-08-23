# -*- coding: utf-8 -*-
"""
    readtime.result
    ~~~~~~~~~~~~~~~

    For returning read time results.

    :copyright: (c) 2016 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


from __future__ import division

from ._compat import u


class Result(object):
    seconds = None
    minutes = None
    text = None

    def __init__(self, seconds):
        self.seconds = seconds
        self.minutes = int(round(seconds / 60))
        if self.minutes < 1:
            self.minutes = 1
        self.text = u('{0} min').format(self.minutes)

    def __repr__(self):
        return self.text + ' read'

    def __unicode__(self):
        return self.__repr__()  # pragma: nocover
