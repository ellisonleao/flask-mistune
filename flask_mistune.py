# coding: utf-8
from __future__ import absolute_import

from flask import Markup

from mistune import markdown as mistune_markdown


def markdown(text, **options):
    """
    options:
        escape - default: False
        use_xhtml - default: False
    """
    return Markup(mistune_markdown(text, **options))


class Mistune:
    def __init__(self, app=None, **params):
        self.params = params
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.jinja_env.filters.setdefault('markdown', self.render)

    def render(self, text):
        return markdown(text, **self.params)
