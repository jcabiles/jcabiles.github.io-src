#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Cabiles'
SITENAME = 'Data Primalytics'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

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
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True



#enables plugins on Pelican
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['rmd_reader']


### the code in this block is for pelican-ipynb, which isn't working properly
### code it out right now until I figure out why Pelican isn't processing ipynb files
# PLUGINS = ['pelican-ipynb.markup']
# allows us to use ipynb and md 
# MARKUP = ('md', 'ipynb')
# prevents Pelican from trying to parse ipynb notebook checkpoint files
# I haven't run into this issue yet
# but it will be handy if I run into an error about checkpoints
#IGNORE_FILES = ['.ipynb_checkpoints']


## add this after you install rmd_reader
## allows us to write Pelican blog posts using R Markdown and Knitr




# gives knitr instructions on how to name & where to store image files
# this will reduce the likelihood of you having conflicts and overwriting files from older 
STATIC_PATHS = ['figure']
RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}
