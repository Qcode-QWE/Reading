import time,datetime
from Reading.dao import Place_Dao
from Reading.dao import Image_Dao
import random
from Reading.pojo import table
from Reading.Utils import thread_utils

# 系统的工具类


# 获取当前时间
def get_now_time():
    t = datetime.datetime.now()
    return t
