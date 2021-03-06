
from redis import StrictRedis

class Config(object):
    DEBUG = True
    SECRET_KEY="BlOMwXHF7b1qUG4sTMB/wzGLA0YfPRY3Q5wzFb6MDGPpj4LDxJNLpHzKIjQFVBZB"
    SQLALCHEMY_DATABASE_URI = "mysql://root:yige@127.0.0.1:3306/travelblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    REDIS_HOST="127.0.0.1"
    REDIS_PORT= 6379
    #Session
    SESSION_TYPE ="redis"
    SESSION_USE_SIGNER= True
    SESSION_REDIS= StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_PERMANET= False
    PERMANET_SESSION_LIFETIME= 86400*2
    pass