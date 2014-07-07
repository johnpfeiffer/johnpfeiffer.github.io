#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'john pfeiffer'
SITENAME = u'johnpfeiffer'
OUTPUT_PATH = 'output/'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

LINKS =  (('About John Pfeiffer', 'http://johnpfeiffer.bitbucket.org/pages/about-john-pfeiffer.html'),
          ('CV', 'https://www.linkedin.com/in/foupfeiffer'),
          ('source code', 'https://bitbucket.org/johnpfeiffer'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-elegant'
PLUGIN_PATHS = 'plugins'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
