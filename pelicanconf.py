#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.rst import PyEmbedRst
PyEmbedRst().register()

AUTHOR = 'Peijun Zhu'
AUTHOR_URL = 'aboutme.html'
SITETITLE = 'Peijun Zhu'
SITENAME = "Peijun's Thoughts"

SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
FAVICON = 'res/favicon.ico'
#SITELOGO = '/peijunz.jpg'
SITELOGO = '/res/site.png'
SITESUBTITLE = 'PhD Student@Physics'
DISQUS_SITENAME = "peijunz"
GOOGLE_ANALYTICS='UA-96594625-1'
# Blogroll
LINKS = (('About', '/aboutme.html'),
         ('Contact', 'mailto:pez33@pitt.edu'),
    ('ipynb2pelican', 'https://github.com/peijunz/ipynb2pelican'),)

# Social widget
SOCIAL = (('github', 'http://github.com/peijunz'),
          ('facebook', 'https://www.facebook.com/people/Peijun-Zhu/100011384055583'),
	          ('rss', '//peijun.me/feeds/all.atom.xml'))
MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'))
COPYRIGHT_YEAR = 2017
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
#GITHUB_CORNER_URL = "https://github.com/peijunz"
USE_LESS = False
PYGMENTS_STYLE = 'default'
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = False
THEME = './pelican-themes/Flex'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb', 'rst')
PLUGIN_PATH = ['./pelican-plugins']
PLUGINS = ['render_math', 'ipynb2pelican', 'liquid_tags.include_code',
           'sitemap', 'modified_from_mtime']
ALWAYS_MODIFIED=True
IGNORE_FILES = ['.ipynb_checkpoints']
STATIC_PATHS = ['res', 'code', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
