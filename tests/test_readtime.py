# -*- coding: utf-8 -*-


import readtime

from .utils import unittest, u, unicode


class BaseTestCase(unittest.TestCase):

    def test_plain_text_simple(self):
        result = readtime.of_text('Some simple text')
        self.assertEquals(result.seconds, 1)
        self.assertEquals(result.text, u('1 min'))
        self.assertEquals(u(result), u('1 min read'))

    def test_plain_text(self):
        inp = open('tests/samples/plain_text.txt').read()
        result = readtime.of_text(inp)
        self.assertEquals(result.seconds, 127)
        self.assertEquals(result.text, u('3 min'))
        self.assertEquals(u(result), u('3 min read'))

    def test_markdown(self):
        inp = open('tests/samples/markdown.md').read()
        result = readtime.of_markdown(inp)
        self.assertEquals(result.seconds, 210)
        self.assertEquals(result.text, u('4 min'))
        self.assertEquals(u(result), u('4 min read'))

    def test_html(self):
        inp = open('tests/samples/html.html').read()
        result = readtime.of_html(inp)
        self.assertEquals(result.seconds, 210)
        self.assertEquals(result.text, u('4 min'))
        self.assertEquals(u(result), u('4 min read'))

    def test_plain_text_unicode(self):
        result = readtime.of_text('Some simple text')
        self.assertEquals(unicode(result), u('1 min read'))

    def test_unsupported_format(self):
        with self.assertRaises(Exception) as e:
            readtime.utils.read_time('Some simple text', format='foo')
        self.assertEquals(str(e.exception), 'Unsupported format: foo')

    def test_invalid_format(self):
        with self.assertRaises(Exception) as e:
            readtime.utils.read_time('Some simple text', format=123)
        self.assertEquals(str(e.exception), 'Unsupported format: 123')
