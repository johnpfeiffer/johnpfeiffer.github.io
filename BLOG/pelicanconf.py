#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'john pfeiffer'
SITENAME = u'johnpfeiffer'
# SITEURL = 'johnpfeiffer.bitbucket.org'
TIMEZONE = 'America/Los Angeles'
DEFAULT_LANG = u'en'
OUTPUT_PATH = '../'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('CV', 'https://www.linkedin.com/in/foupfeiffer'),
          ('source code', 'https://bitbucket.org/johnpfeiffer'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'js']
# Sole author and don't use categories ... disable these features
# AUTHOR_SAVE_AS = False
# AUTHORS_SAVE_AS = False
# CATEGORY_SAVE_AS = False
# CATEGORIES_SAVE_AS = False

THEME = "/usr/local/lib/python2.7/dist-packages/pelican/themes/foundation-default-colours"
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = False
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = ''
FOUNDATION_PYGMENT_THEME = 'monokai'
