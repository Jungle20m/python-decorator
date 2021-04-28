import os
import json
import pickle

from starlette.config import Config


SERVICE_NAME = "capnhat_tamtinh_v3"


config = Config(".env")


# **DATABASE SETTINGS
DATABASE: str = config("DATABASE", default="")
HOST: str = config("HOST", default="")
PORT: int = config("PORT", cast=int, default=3306)
USER: str = config("USER", default="")
PASSWORD: str = config("PASSWORD", default="")
POOL_SIZE: int = config("POOL_SIZE", cast=int, default=5)
 
 
# **API
API_TAM_TINH: str = config("API_TAM_TINH")


# **KAFKA SETTINGS
KAFKA_BROKERS = config("KAFKA_BROKERS").split(",")
UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_TOPIC_NAME = config("UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_TOPIC_NAME")
UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_GROUP_ID = config("UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_GROUP_ID")
UPDATE_DOXA_BY_RANGE_DAY_TOPIC_NAME = config("UPDATE_DOXA_BY_RANGE_DAY_TOPIC_NAME")

JSON_DESERIALIZER = lambda m: json.loads(m.decode('utf-8'))
JSON_SERIALIZER = lambda m: json.dumps(m).encode('utf-8')
PICKLE_DESERIALIZER = lambda m:pickle.loads(m) 
PICKLE_SERIALIZER = lambda m:pickle.dumps(m)
UTF8_DESERIALIZER = lambda m:m.decode("utf-8") 


# **LOG SETTINGS
LOG_LOCATION: str = config("LOG_LOCATION", default=os.path.join(os.getcwd(), "src/log"))  
LOG_FILE: str = config("LOG_FILE", default="capnhat_tamtinh_log")