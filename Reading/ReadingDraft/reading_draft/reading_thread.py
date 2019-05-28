from Reading.dao import Place_Dao
import time
from Reading.dao import Place_Dao
from Reading.service import Calibration_Service
import threading
# reading_start创建一个线程每隔一分钟识别所有地点的水尺图像

# 获取每个地点的水尺刻度
def reading_every_place():
    print("识别刻度")
    # 获取所有的地点
    places = Place_Dao.get_all_place()
    # 获取该地点最近一次的水尺刻度
    for place in places:
        Calibration_Service.get_calibration_last(place)

def reading_start():
    timer = threading.Timer(60, reading_every_place)
    timer.start()
reading_start()