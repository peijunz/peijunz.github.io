#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.rst import PyEmbedRst
PyEmbedRst().register()

AUTHOR = 'Peijun Zhu'
# AUTHOR_URL = 'aboutme.html'
#SITETITLE = 'Peijun Zhu'
SITENAME = "Peijun's Thoughts"
ABOUTURL="/aboutme.html"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
FAVICON = '/res/favicon.ico'
#SITELOGO = '/peijunz.jpg'
SITELOGO = '/res/site.png'
# Blogroll
#LINKS = (('ipynb2pelican', 'https://github.com/peijunz/ipynb2pelican'),)

# Social widget
SOCIAL = (('github', 'http://github.com/peijunz'),
          ('facebook', 'https://www.facebook.com/people/Peijun-Zhu/100011384055583'),
	          ('rss', 'http://www.peijun.me/feeds/all.atom.xml'))
MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Blog', '/blogging-with-jupyter-and-pelican.html'))
#GITHUB_CORNER_URL = "https://github.com/peijunz"
#USE_LESS = False
#DISABLE_URL_HASH = True
DEFAULT_DATE = 'fs'
PYGMENTS_STYLE = 'default'
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = False
THEME = './pelican-themes/Flex'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb', 'rst')
PLUGIN_PATH = ['./pelican-plugins']
PLUGINS = ['render_math', 'ipynb2pelican', 'liquid_tags.include_code']
IGNORE_FILES = ['.ipynb_checkpoints']
STATIC_PATHS = ['res', 'code']
CACHE_CONTENT = False#True
LOAD_CONTENT_CACHE = False#True
MATHJAX_CDN="/static/MathJax.js"
