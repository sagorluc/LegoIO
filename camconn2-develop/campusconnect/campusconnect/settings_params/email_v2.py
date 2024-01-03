import os
from django.conf import settings
 
EMAIL_HOST    = os.environ.get("EMAIL_HOST_PROVIDER")
EMAIL_PORT    = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS") 

if os.environ.get("SERVER_TYPE") == "production":
  DEVELOPMENT_ONLY_EMAIL_RECIPIENTS = []
else:
  if os.environ.get('DEVELOPMENT_ONLY_EMAIL_RECIPIENTS') is not None:
    DEVELOPMENT_ONLY_EMAIL_RECIPIENTS = (os.environ.get('DEVELOPMENT_ONLY_EMAIL_RECIPIENTS')).split(",")
  else:
    DEVELOPMENT_ONLY_EMAIL_RECIPIENTS = [
      "def274753@gmail.com",
    ]

EMAIL_CONFIG = {
  "AUTH":{
    'EMAIL_HOST_USER':os.environ.get("EMAIL_HOST_USER_AUTH"),
    'EMAIL_HOST_PASSWORD':os.environ.get("EMAIL_HOST_PASSWORD_AUTH")
  },
  "SHOPCART":{
    'EMAIL_HOST_USER':os.environ.get("EMAIL_HOST_USER_SHOPCART"),
    'EMAIL_HOST_PASSWORD':os.environ.get("EMAIL_HOST_PASSWORD_SHOPCART")
  },
  "GENERAL":{
    'EMAIL_HOST_USER':os.environ.get("EMAIL_HOST_USER_GENERAL"),
    'EMAIL_HOST_PASSWORD':os.environ.get("EMAIL_HOST_PASSWORD_GENERAL")
  },
  "CUSTSUPP":{
    'EMAIL_HOST_USER':os.environ.get("EMAIL_HOST_USER_CUSTSUPP"),
    'EMAIL_HOST_PASSWORD':os.environ.get("EMAIL_HOST_PASSWORD_CUSTSUPP")
  },
}