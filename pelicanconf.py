AUTHOR = 'shukri'
SITENAME = 'Buku Catatan'
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG = 'en'

DISPLAY_CATEGORIES_ON_MENU = False

THEME = "themes/bootstrap5.3"
STYLESHEET_URL = f"{SITEURL}/theme/css/style.css"
LOAD_CONTENT_CACHE = False
JINJA_GLOBALS = {'article_url': []}
JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True, 'extensions': ["jinja2.ext.do", ]}

# this is a destructive setting and should be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True