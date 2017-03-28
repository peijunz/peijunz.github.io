#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.rst import PyEmbedRst
PyEmbedRst().register()

AUTHOR = 'Peijun Zhu'
SITENAME = "Peijun's Thoughts"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Contact Me', 'mailto:pez33@pitt.edu'),
         ('ipynb2pelican', 'https://github.com/peijunz/ipynb2pelican'),)

# Social widget
SOCIAL = (('github', 'http://github.com/peijunz'),
          ('facebook', 'https://www.facebook.com/people/Peijun-Zhu/100011384055583'),)

DEFAULT_PAGINATION = 6
MULTI_NEIGHBORS = 5
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKUP = ('md', 'ipynb', 'rst')
PLUGIN_PATH = ['./pelican-plugins']
PLUGINS = ['render_math', 'ipynb2pelican', 'neighbors']

IGNORE_FILES = ['.ipynb_checkpoints']
STATIC_PATHS = ['images', 'pdfs', 'Homepage/_static']
