from Reading.dao import Place_Dao
import time
from Reading.dao import Place_Dao
from Reading.service import Calibration_Service
import threading
import random
from Reading.pojo import table
from Reading.Utils import utils
from Reading.dao import Image_Dao, Place_Dao

# 一些定时任务:如每分钟插入图片,每分钟识别图片

# 创建一个线程每隔一分钟识别所有地点的水尺图像
# 私有方法:获取每个地点的水尺刻度
def __reading_every_place():
    print("识别刻度")
    # 获取所有的地点
    places = Place_Dao.get_all_place()
    # 获取该地点最近一次的水尺刻度
    for place in places:
        Calibration_Service.get_calibration_last(place)

# 调用reading_start来执行定时识别水尺任务
__reading_thread = None

def reading_start():
    global __reading_thread
    if __reading_thread == None:
        __reading_thread = threading.Timer(60, __reading_every_place)
        __reading_thread.start()

##########################################################
# 创建一个线程模拟每个地点一分钟上传一张图片
def __insert_image_all_place():
    # 获取所有的地点
    places = Place_Dao.get_all_place()
    # 图片地址
    address = 'D:/USER/Desktop/软件工程/水尺?.jpg'
    # 水尺刻度
    nums = [650, 775]
    add_num1 = [2, 5, 6, 7]
    add_num2 = [1, 3, 4]
    # 插入图片
    for place in places:
        if place.max_num == nums[0]:
            num = random.randint(0, 3)
            add = address.replace('?', str(add_num1[num]))
        elif place.max_num == nums[1]:
            num = random.randint(0, 2)
            add = address.replace('?', str(add_num2[num]))
        image = table.Image(0, utils.get_now_time(), place.place_id, add)
        Image_Dao.insert_image(image)

# 调用reading_start来执行定时上传图片任务
__uploading_thread = None

def uploading_start():
    global __uploading_thread
    if __uploading_thread == None:
        __uploading_thread = threading.Timer(60, __insert_image_all_place)
        __uploading_thread.start()
