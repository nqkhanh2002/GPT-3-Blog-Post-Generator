##OPEN API STUFF
OPENAI_API_KEY = 'enter your key here'
# process.env.OPENAI_API_KEY


## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "enter your key here"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
