import os
from django.conf import settings


# DATABASES
###################################
if os.environ.get('SERVER_TYPE') == 'local':
  DATA_BASE_DIR = os.environ.get("DATA_BASE_DIR", settings.BASE_DIR)
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.sqlite3",
          "NAME": os.path.join(DATA_BASE_DIR, "db.sqlite3"),
      }
  }
else:
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "HOST": os.environ.get("CAMPUSCONNECT_DBHOST"),
          "NAME": os.environ.get("CAMPUSCONNECT_DBNAME"),
          "USER": os.environ.get("CAMPUSCONNECT_DBUSERNAME"),
          "PASSWORD": os.environ.get("CAMPUSCONNECT_DBPASS"),
          "PORT": os.environ.get("CAMPUSCONNECT_DBPORT"),
          "OPTIONS": {
                    "sslmode": "require",
        }
      }
  }


## For testing purpose
## ************************************************
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "HOST": "localhost",
#         "NAME": "campusconn",
#         "USER": "postgres",
#         "PASSWORD": "102030",
#         "PORT": "5432",

#     }
# }


# os.environ.get("RESUMEWEB_DBHOST"),
# os.environ.get("RESUMEWEB_DBNAME"),
# os.environ.get("RESUMEWEB_DBUSERNAME"),
# os.environ.get("RESUMEWEB_DBPASS"),
# os.environ.get("RESUMEWEB_DBPORT"),