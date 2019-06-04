import datetime

from Reading.ReadingDraft.reading_draft import identify
from Reading.Utils import utils
from Reading.dao import Calibration_Dao
from Reading.dao import Image_Dao
from Reading.pojo import table


# 根据image,place来读取刻度
def get_calibration( image, place):
    cal = identify.get_calibration(image, place.max_num)
    return cal

# 获取place地点最近一次水尺图像,如果图像还没被识别则识别
def get_calibration_last(place):
    # 获取该地点最近一次图像
    image = Image_Dao.find_Image_By_Place_last(place)
    # 判断该图像是否已经被识别过
    calibration = Calibration_Dao.get_By_Image(image)
    # 还没被识别了
    if(type(calibration) == int):
        # 读取刻度
        cal = get_calibration(image, place)
        # 保存到数据库中
        # 判断刻度是否超过警戒线
        is_die = 0
        if cal > place.die_line:
            is_die = 1
        now = datetime.datetime.now()
        now = utils.mysql_date(now)
        calibration = table.Calibration(0, now, place.place_id, image.image_id,
                                        cal, is_die)
        Calibration_Dao.save(calibration)
        # 获取刚save的calibration
        calibration = Calibration_Dao.get_by_place_last(place)
    return calibration



