import os

config_path =  os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'twittor.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # ?????
    SECRET_KEY = 'abc123'
    # WTF_CSRF_SECRET_KEY = 'a random string'
    TWEET_PER_PAGE = 20

    MAIL_DEFAULT_SENDER = 'noreply@twittor.com'
    MAIL_SERVER = 'smtp.sendgrid.net'#'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = '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'
    MAIL_SUBJECT_RESET_PASSWORD = '[Twittor] Please Reset Your Password.'
    MAIN_SUBJECT_USER_ACTIVATE = '[Twittor] Please active your account.'