from Reading.dao import Place_Dao
import time
from Reading.dao import Place_Dao


# 调用reading_start即可每隔一分钟识别所有地点的水尺图像

# 获取每个地点的水尺刻度
def reading_every_place():
    print("识别刻度")
    # 获取所有的地点
    places = Place_Dao.get_all_place()
    # 获取该地点最近一次的水尺刻度
    for place in places:
        Calibration_Service.get_calibration_last(place)

def reading_start():
    while True:
        reading_every_place()
        time.sleep(60)
reading_start()