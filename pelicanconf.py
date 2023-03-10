AUTHOR = 'Kevin Cash'
SITENAME = 'nomde'
SITESUBTITLE = ''
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

PLUGIN_PATHS = ['pelican-plugins']
THEME = 'pelican-themes/simple-bootstrap'
BOOTSTRAP_THEME = 'flatly'

PLUGIN_PATHS = ['pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites']

I18N_TEMPLATES_LANG = 'en'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Pelican-Bootstrap3 Theme alterations

# HIDE_SIDEBAR = True
DISABLE_SIDEBAR_TITLE_ICONS = True
PADDED_SINGLE_COLUMN_STYLE = True
