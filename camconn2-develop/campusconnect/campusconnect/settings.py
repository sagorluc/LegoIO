import os

DEBUG                   = os.environ.get('DEBUG_MODE')
SERVER_TYPE 			= os.environ.get('SERVER_TYPE')

## App Version Info
VER_RESUMEWEB			= os.environ.get('VER_RESUMEWEB')
VER_PROFILER			= os.environ.get('VER_PROFILER')
VER_SHOPCART			= os.environ.get('VER_SHOPCART')
VER_AUTH				= os.environ.get('VER_AUTH')

## project level settings
BASE_DIR                = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY              = "%@161s%q0w^y!7lvvn&9ni+%svsjy&xd-dw1jrjbe@tvn9jg&s"
ROOT_URLCONF            = "campusconnect.urls"
WSGI_APPLICATION        = "campusconnect.wsgi.application"
LANGUAGE_CODE           = "en-us"

## Network settings project level
DNS_NAME                = os.environ.get('DNS_NAME')
PROTOCOL 				= os.environ.get('PROTOCOL')

## list of allowed IP address
INTERNAL_IPS 			= ['127.0.0.1',]

## Allowed hosts
if os.environ.get('DJANGO_ALLOWED_HOSTS') is not None:
	ALLOWED_HOSTS       = (os.environ.get('DJANGO_ALLOWED_HOSTS')).split(",")
else:
	ALLOWED_HOSTS       = ["0.0.0.0"]

## Login redirection
# LOGIN_URL               = "/rw/home"
# LOGIN_REDIRECT_URL      = "/rw/home"
CACHE_TTL               = 60*60

MESSAGE_STORAGE         = 'django.contrib.messages.storage.session.SessionStorage'
DEFAULT_AUTO_FIELD      = 'django.db.models.AutoField'
CRISPY_TEMPLATE_PACK    = 'bootstrap4'


from .settings_params import DATABASES
from .settings_params import ELASTICSEARCH_DSL
from .settings_params import PAYPAL_CLIENT_ENV
from .settings_params import STATIC_URL
from .settings_params import STATIC_ROOT
from .settings_params import MEDIA_ROOT
from .settings_params import MEDIA_URL
from .settings_params import DEVELOPMENT_ONLY_EMAIL_RECIPIENTS

print("***SERVER_TYPE ->>{}".format(SERVER_TYPE))
print("***VER_RESUMEWEB ->>{}".format(VER_RESUMEWEB))
print("***VER_PROFILER ->>{}".format(VER_PROFILER))
print("***VER_SHOPCART ->>{}".format(VER_SHOPCART))
print("***VER_AUTH ->>{}".format(VER_AUTH))
print("***DNS_NAME ->>{}".format(DNS_NAME))
print("***PROTOCOL ->>{}".format(PROTOCOL))
print("***ALLOWED_HOSTS ->>{}".format(ALLOWED_HOSTS))
print("***STATIC_URL ->>{}".format(STATIC_URL))
print("***STATIC_ROOT ->>{}".format(STATIC_ROOT))
print("***MEDIA_ROOT ->>{}".format(MEDIA_ROOT))
print("***MEDIA_URL ->>{}".format(MEDIA_URL))
print("***PAYPAL_CLIENT_ENV ->>>{}".format(PAYPAL_CLIENT_ENV))
print("***DATABASE ->>>{}".format(DATABASES['default']['NAME']))
print("***ELASTICSEARCH ->>>{}".format(ELASTICSEARCH_DSL['default']['hosts'][0]))
print("***DEVELOPMENT_ONLY_EMAIL_RECIPIENTS ->>{}".format(DEVELOPMENT_ONLY_EMAIL_RECIPIENTS))

# Import all settings params
from .settings_params import *
