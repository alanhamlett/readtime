# -*- coding: utf-8 -*-


import readtime

import unittest

from .utils import u
from readtime.utils import DEFAULT_WPM


class BaseTestCase(unittest.TestCase):

    def test_transitions(self):
        word = 'word '
        for x in range(10):

            # test the maximum num words for x read time
            text = word * 265 * x
            result = readtime.of_text(text)
            self.assertEqual(result.seconds, x * 60 if x > 0 else 1)
            self.assertEqual(result.text, u('{0} min'.format(x if x > 0 else 1)))
            self.assertEqual(u(result), u('{0} min read'.format(x if x > 0 else 1)))

            # test the maximum + 1 num words, and make sure read time is x + 1
            text += 'word'
            result = readtime.of_text(text)
            self.assertEqual(result.seconds, x * 60 + 1)
            self.assertEqual(result.text, u('{0} min'.format(x + 1)))
            self.assertEqual(u(result), u('{0} min read'.format(x + 1)))

    def test_plain_text(self):
        inp = open('tests/samples/plain_text.txt').read()
        result = readtime.of_text(inp)
        self.assertEqual(result.seconds, 154)
        self.assertEqual(type(result.seconds), int)
        self.assertEqual(result.text, u('3 min'))
        self.assertEqual(u(result), u('3 min read'))

    def test_plain_text_empty(self):
        result = readtime.of_text('')
        self.assertEqual(result.seconds, 1)
        self.assertEqual(result.text, u('1 min'))
        self.assertEqual(u(result), u('1 min read'))

    def test_plain_text_null(self):
        result = readtime.of_text(None)
        self.assertEqual(result.seconds, 0)
        self.assertEqual(result.text, u('1 min'))
        self.assertEqual(u(result), u('1 min read'))

    def test_markdown(self):
        inp = open('tests/samples/markdown.md').read()
        result = readtime.of_markdown(inp)
        self.assertEqual(result.seconds, 236)
        self.assertEqual(result.text, u('4 min'))
        self.assertEqual(u(result), u('4 min read'))

    def test_html(self):
        inp = open('tests/samples/html.html').read()
        result = readtime.of_html(inp)
        self.assertEqual(result.seconds, 236)
        self.assertEqual(result.text, u('4 min'))
        self.assertEqual(u(result), u('4 min read'))

    def test_plain_text_unicode(self):
        result = readtime.of_text('Some simple text')
        self.assertEqual(str(result), u('1 min read'))

    def test_unsupported_format(self):
        with self.assertRaises(Exception) as e:
            readtime.utils.read_time('Some simple text', format='foo')
        self.assertEqual(str(e.exception), 'Unsupported format: foo')

    def test_invalid_format(self):
        with self.assertRaises(Exception) as e:
            readtime.utils.read_time('Some simple text', format=123)
        self.assertEqual(str(e.exception), 'Unsupported format: 123')

    def test_can_add(self):
        inp = open('tests/samples/plain_text.txt').read()
        result1 = readtime.of_text(inp)
        self.assertEqual(result1.seconds, 154)

        inp = open('tests/samples/markdown.md').read()
        result2 = readtime.of_markdown(inp)
        self.assertEqual(result2.seconds, 236)

        result = (result1 + result2)
        self.assertEqual(result.seconds, 154 + 236)
        self.assertEqual(type(result.seconds), int)
        self.assertEqual(result.text, u('7 min'))
        self.assertEqual(u(result), u('7 min read'))

    def test_custom_wpm(self):
        text = 'some test content ' * 100
        result = readtime.of_text(text)
        self.assertEqual(result.wpm, DEFAULT_WPM)
        self.assertEqual(result.seconds, 68)
        self.assertEqual(result.text, u('2 min'))
        wpm = 50
        result = readtime.of_text(text, wpm=wpm)
        self.assertEqual(result.wpm, wpm)
        self.assertEqual(result.seconds, 360)
        self.assertEqual(type(result.seconds), int)
        self.assertEqual(result.text, u('6 min'))
        self.assertEqual(u(result), u('6 min read'))
