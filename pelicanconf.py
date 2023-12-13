AUTHOR = 'shukri azmi'
SITENAME = 'Buku Catatan'
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Asia/Kuala_Lumpur'
DEFAULT_LANG = 'en'

THEME = "themes/bootstrap5.3"
STYLESHEET_URL = f"{SITEURL}/theme/css/style.css"
MENUITEMS = (('Archives', '/archives.html'), ('About', '/about.html'), )
DISPLAY_CATEGORIES_ON_MENU = False
LOAD_CONTENT_CACHE = False
DEFAULT_PAGINATION = 2

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {"about.html": "about.html"}
JINJA_ENVIRONMENT = {'extensions': ["jinja2.ext.do", ]}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Python", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("Bootstrap", "https://getbootstrap.com/")
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/shukriazmi"),
    ("linkedin", "https://www.linkedin.com/in/shukri-azmi/"),
    ("envelope", "mailto:shukriazmi7@gmail.com"),

)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True