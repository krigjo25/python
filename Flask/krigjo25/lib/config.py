class DefaulthConfig(object):
    TESTING = False
    #DATABASE_URL =
    DEBUG = False
    SESSION_TYPE = None
    SESSION_PERMANENT = False

class DevelopmentConfig(DefaulthConfig):
    TESTING = False
    #DATABASE_URL
    SESSION_TYPE ='filesystem'
    DEBUG = True