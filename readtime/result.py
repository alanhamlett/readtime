# -*- coding: utf-8 -*-
"""
    readtime.result
    ~~~~~~~~~~~~~~~

    For returning read time results.

    :copyright: (c) 2016 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


from __future__ import division

import math
import operator
from datetime import timedelta

from ._compat import u


class Result(object):
    delta = None

    def __init__(self, seconds):
        self.delta = timedelta(seconds=seconds)
        self.add_operator_methods()

    def __repr__(self):
        return self.text + ' read'

    def __unicode__(self):
        return self.__repr__()  # pragma: nocover

    def __str__(self):
        return u(self).encode('utf-8')

    @property
    def seconds(self):
        return int(self.delta.total_seconds())

    @property
    def minutes(self):
        minutes = int(math.ceil(self.seconds / 60))
        if minutes < 1:  # Medium's formula has a minimum of 1 min read time
            minutes = 1
        return minutes

    @property
    def text(self):
        return u('{minutes} min').format(minutes=self.minutes)

    def add_operator_methods(self):
        for op in dir(operator):
            if (getattr(self.__class__, op, None) is None
                and getattr(self.delta, op, None) is not None
                and op.startswith('__')
                and op.endswith('__')):
                try:
                    setattr(self.__class__, op, self.create_method(op))
                except (AttributeError, TypeError):
                    pass

    def create_method(self, op):
        fn = getattr(self.delta, op)
        def method(cls, other, *args, **kwargs):
            delta = fn(other.delta)
            return Result(delta.total_seconds())
        return method
