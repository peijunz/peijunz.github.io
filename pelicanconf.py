#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.rst import PyEmbedRst
PyEmbedRst().register()

AUTHOR = 'Peijun Zhu'
SITETITLE = 'Peijun Zhu'
#ABOUT_ME = "无可奉告"
SITENAME = "Peijun's Journal"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

LOCALE = 'zh_CN.utf8'

DATE_FORMATS = {
    'en': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
    'zh': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
}

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
FAVICON = '/static/binary.png'
#SITELOGO = '/peijunz.jpg'
#AVATAR = '/static/site.png'
#SITELOGO = '/static/site.png'
# Blogroll
LINKS = (('<img alt="Build Status" src="https://travis-ci.org/peijunz/peijunz.github.io.svg?branch=src" style="max-width:100%;">', 'https://travis-ci.org/peijunz/peijunz.github.io'),
        ('<i class="fa fa-code fa-lg"></i> Source of Contents', 'https://github.com/peijunz/peijunz.github.io/tree/src/content'))

# Social widget
SOCIAL = (
#    ('Google', 'https://plus.google.com/109997738689761453578'),
    ('Email', 'mailto:pez33@pitt.edu', 'envelope-o'),
    ('Facebook', 'https://www.facebook.com/people/Peijun-Zhu/100011384055583'),
    ('Github', 'http://github.com/peijunz'),
    )
DISPLAY_TAGS_INLINE = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU=False
DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
'tags'))
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
)
DEFAULT_DATE = 'fs'
PYGMENTS_STYLE = 'default'
DEFAULT_PAGINATION = 10
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = "flatly"
THEME_COLOR = True
DISPLAY_BREADCRUMBS=True
DISPLAY_CATEGORY_IN_BREADCRUMBS=True
BOOTSTRAP_NAVBAR_INVERSE=False
TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"

STATIC_PATHS = ['static', 'code']

#OUTPUT_SOURCES = True
#OUTPUT_SOURCES_EXTENSION = '.txt'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'authors', 'archives', 'search')
MARKUP = ('md', 'ipynb', 'rst')
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'ipynb2pelican', 'liquid_tags.include_code',
           'pelican-toc', 'i18n_subsites', 'tag_cloud', 'tipue_search', 'neighbors', 'pelican_alias']
IGNORE_FILES = ['.ipynb_checkpoints']
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
MATHJAX_CDN="/mathjax/latest.js"
TOC = {
    'TOC_HEADERS' : '^h[2-4]',
    'TOC_RUN'     : 'true',
    'TOC_INCLUDE_TITLE': 'false',
}


CUSTOM_CSS="static/css/custom.css"
SUMMARY_MAX_LENGTH = 30
