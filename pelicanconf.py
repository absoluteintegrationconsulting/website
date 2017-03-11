#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = u'Alex Hutton'
AUTHORS = ['AAA', 'BBB']
SITENAME = u'Absolute Integration Consulting'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['css']

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

CSS_FILE = 'styles.css'

# BT3-Flat

ARCHIVE_LIST = True

COPYRIGHT = '%s &copy; All Rights Reserved.' % datetime.datetime.now().year

DEFAULT_DATA_FORMAT = ('%Y/%m/%d %a')

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

PLUGINS = ['sitemap', 'neighbors', 'related_posts']

SERVICES_TEXT = """
<p>
We specialise in integration work. Integrate your website or application
with a third party API. Offer your own API. Meld four or five APIs together to
create your own unique service. Migrate a legacy SOAP API to REST. Facade your
legacy database with a web service to avoid direct database queries.  Create an
adapter to external services to avoid vendor lock-in.
</p>
<p>
Whatever service you need to integrate with, Open Auth, payments, SMS,
chatbots, analytics, image processing, booking, social media or any
proprietary system you can think of, our mission is to give you a tested,
documented, accurate solution that will exceed your expectations and deliver
you the greatest possible value for money.
</p>
"""

PERSONAL_INFO = """
Elite level API and Integration development, at your service."""

HEADER_IMAGE = 'https://dl.dropboxusercontent.com/u/299446/logo-invert.png'
HEADER_IMAGE = 'planes.jpg'
BACKGROUND_IMAGE = 'http://images.nationalgeographic.com/wpf/media-live/photos/000/763/cache/egret-fog-reflection_76312_990x742.jpg'
