# -*- coding: utf-8 -*-


def u(text):
    if isinstance(text, bytes):
        return text.decode('utf-8')
    return str(text)
