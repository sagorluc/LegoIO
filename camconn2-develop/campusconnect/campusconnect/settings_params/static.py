import os 
from django.conf import settings


if os.environ.get('SERVER_TYPE') == 'local':
	STATIC_URL = os.environ.get("STATIC_URL")
	STATIC_ROOT = os.environ.get("STATIC_ROOT") or os.path.join(settings.BASE_DIR, "static")
else:
	STATIC_URL = os.environ.get("STATIC_URL")
	STATIC_ROOT = os.environ.get("STATIC_ROOT") or os.path.join(settings.BASE_DIR, "static")



	# STATICFILES_DIRS =  os.environ.get("STATICFILES_DIRS") ##(str(settings.BASE_DIR.joinpath('static')),)
	# print("STATICFILES_DIRS ->>{}".format(STATICFILES_DIRS))	
	
	# STATIC_ROOT = os.environ.get("STATIC_ROOT") or os.path.join(settings.BASE_DIR, "static")
	# STATIC_ROOT = settings.BASE_DIR + '/' + os.environ.get("STATIC_ROOT")
	# print("STATIC_ROOT ->>{}".format(STATIC_ROOT))

	# # STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")
	# STATIC_ROOT = os.environ.get("STATIC_ROOT") or os.path.join(settings.BASE_DIR, "static")


# else:
#     # aws settings
#     AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
#     AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
#     AWS_DEFAULT_ACL = 'public-read'
#     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#     AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
#     # s3 static settings
#     AWS_LOCATION = 'static'
#     STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
#     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# 	## additional
# 	# AWS_QUERYSTRING_AUTH = os.environ.get("AWS_QUERYSTRING_AUTH")
# 	# AWS_S3_FILE_OVERWRITE = os.environ.get('AWS_S3_FILE_OVERWRITE')
