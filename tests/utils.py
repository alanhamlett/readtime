# -*- coding: utf-8 -*-

import sys


is_py2 = (sys.version_info[0] == 2)
is_py3 = (sys.version_info[0] == 3)


if is_py2:
    def u(text):
        try:
            return text.decode('utf-8')
        except:
            try:
                return unicode(text)
            except:
                return text

    unicode = unicode


elif is_py3:
    def u(text):
        if isinstance(text, bytes):
            return text.decode('utf-8')
        return str(text)

    unicode = str
