import os

if os.environ.get("SERVER_TYPE") == "production":
    PAYPAL_CLIENT_ENV = "LiveEnvironment"
else:
    PAYPAL_CLIENT_ENV = "SandboxEnvironment"

