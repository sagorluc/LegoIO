# MIDDLEWARE
############

MIDDLEWARE_PRE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    # 'admin_reorder.middleware.ModelAdminReorder',
    #"corsheaders.middleware.CorsMiddleware",
    #"corsheaders.middleware.CorsMiddleware",
    #"django.middleware.common.CommonMiddleware"
]


""" CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "https://sandbox.sslcommerz.com",
]  """

MIDDLEWARE_CUSTOM = [
    "viewtracker.middleware.mw_viewTracker",
    "inventory.middleware.mw_mmhUserUniqueid",
]
CORS_ORIGIN_ALLOW_ALL=True

MIDDLEWARE = MIDDLEWARE_PRE + MIDDLEWARE_CUSTOM
