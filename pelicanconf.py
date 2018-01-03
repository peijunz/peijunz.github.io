#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.rst import PyEmbedRst
PyEmbedRst().register()

AUTHOR = 'Peijun Zhu'
# AUTHOR_URL = 'aboutme.html'
SITETITLE = 'Peijun Zhu'
#ABOUT_ME = "无可奉告"
SITENAME = "Peijun's Journal"
ABOUTURL="/aboutme.html"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'zhs'

LOCALE = 'zh_CN.utf8'

DATE_FORMATS = {
    'en': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
    'zh': ((u'zh_HK', 'utf8'), u'%Y年%m月%d日(週%a)',),
    'zhs': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
    'jp': ((u'ja_JP', 'utf8'), u'%Y年%m月%d日(%a曜日)',),
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
FAVICON = '/res/favicon.ico'
#SITELOGO = '/peijunz.jpg'
#AVATAR = '/res/site.png'
#SITELOGO = '/res/site.png'
# Blogroll
#LINKS = (('ipynb2pelican', 'https://github.com/peijunz/ipynb2pelican'),)

# Social widget
SOCIAL = (
#    ('google', 'https://plus.google.com/109997738689761453578'),
    ('rss', 'http://www.peijun.me/feeds/all.atom.xml'),
    #('puzzle-piece', 'https://greasyfork.org/en/users/72080-%E6%B2%9B%E4%BF%8A%E6%9C%B1'),
    #('envelope-o', 'mailto:pez33@pitt.edu'),
    ('facebook', 'https://www.facebook.com/people/Peijun-Zhu/100011384055583'),
    ('github', 'http://github.com/peijunz'),
    )
DISPLAY_TAGS_INLINE = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#             ('Tags', '/tags.html'),
#             ('Blog', '/blogging-with-jupyter-and-pelican.html')
)
#GITHUB_CORNER_URL = "https://github.com/peijunz"
#USE_LESS = False
#DISABLE_URL_HASH = True
DEFAULT_DATE = 'fs'
PYGMENTS_STYLE = 'default'
DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = False
#THEME = './pelican-themes/Flex'
THEME = './pelican-themes/pelican-bootstrap3'
OUTPUT_SOURCES = False
BOOTSTRAP_THEME = "cosmo"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
MARKUP = ('md', 'ipynb', 'rst')
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math', 'ipynb2pelican', 'liquid_tags.include_code',
           'pelican-toc', 'neighbors', 'i18n_subsites', 'tag_cloud', 'tipue_search']
IGNORE_FILES = ['.ipynb_checkpoints']
STATIC_PATHS = ['res', 'code']
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
MATHJAX_CDN="/static/MathJax.js"
#DISABLE_URL_HASH=True
TOC = {
    'TOC_HEADERS' : '^h[2-4]',
    'TOC_RUN'     : 'true',
    'TOC_INCLUDE_TITLE': 'false',
}


CUSTOM_CSS="res/css/custom.css"
#GITHUB_USER="peijunz"
#CUSTOM_JS="https://rawgit.com/peijunz/90da9dc4c7d753f9c5b128d45a23fecb/raw/add_blog_buttons.js"
