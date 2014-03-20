# coding: utf-8
import unittest

from flask import Flask, Markup, render_template_string
from flask.ext.mistune import Mistune, markdown

app = Flask(__name__)
app.debug = True
Mistune(app)


@app.route('/test')
def mardown_template_filter():
    text = u'~~testing markdown filter~~ *test*'
    return render_template_string('{{ text|markdown }}', text=text)


@app.route('/test2')
def mardown_template_block():
    test = u'*test*'
    text = u'{% filter markdown %}{{ test }}{% endfilter %}'
    return render_template_string(text, test=test)


class MistuneTest(unittest.TestCase):
    def test_render_template_filter(self):
        client = app.test_client()
        resp = client.open('/test')
        self.assertEqual(resp.data, u'<p><del>testing markdown filter</del> '
                         u'<em>test</em></p>\n')

    def test_render_template_block(self):
        client = app.test_client()
        resp = client.open('/test2')
        self.assertEqual(resp.data, u'<p><em>test</em></p>\n')

    def test_markdown_function(self):
        string = u'this is a *markdown* string'
        self.assertEqual(markdown(string), Markup(u'<p>this is a '
                                                  u'<em>markdown</em> '
                                                  u'string</p>\n'))

if __name__ == '__main__':
    unittest.main()
