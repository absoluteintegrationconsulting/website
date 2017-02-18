#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alex Hutton'
AUTHORS = ['AAA', 'BBB']
SITENAME = u'Absolute Integration Consulting'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'BT3-Flat'

# BT3-Flat

ARCHIVE_LIST = True

DEFAULT_DATA_FORMAT = ('%Y/%m/%d %a')

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

PLUGINS = ['sitemap', 'neighbors', 'related_posts']

PERSONAL_INFO = """Hello, this is my personal info"""

HEADER_IMAGE = 'https://dl.dropboxusercontent.com/u/299446/logo-invert.png'
BACKGROUND_IMAGE = 'http://images.nationalgeographic.com/wpf/media-live/photos/000/763/cache/egret-fog-reflection_76312_990x742.jpg'
