import os
import dotenv

class Config(object):
    dotenv.load_dotenv(".env")
    CSRF_ENABLED = True
    TWITTER_OAUTH_CLIENT_KEY = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
    TWITTER_OAUTH_CLIENT_SECRET = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    URL = os.environ.get("URL")

    FB_CLIENT_ID = os.environ.get("FB_CLIENT_ID")
    FB_CLIENT_SECRET = os.environ.get("FB_CLIENT_SECRET")

    FB_AUTHORIZATION_BASE_URL = os.environ.get("FB_AUTHORIZATION_BASE_URL")
    FB_TOKEN_URL = os.environ.get("FB_TOKEN_URL")

    FB_SCOPE = os.environ.get("FB_SCOPE")

    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")

    GOOGLE_AUTHORIZATION_BASE_URL = os.environ.get("GOOGLE_AUTHORIZATION_BASE_URL")
    GOOGLE_SCOPE = os.environ.get("GOOGLE_SCOPE")
    GOOGLE_TOKEN_URL = os.environ.get("GOOGLE_TOKEN_URL")

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "Prod@Secret_Key"

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
    DEVELOPMENT = True
    SECRET_KEY = "Dev@Secret_Key"
    OAUTHLIB_INSECURE_TRANSPORT = True