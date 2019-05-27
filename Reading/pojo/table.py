import time

# 刻度实体类
class Calibration:

    def __init__(self, calibration_id=0, identify_time=time.time(), place_id=0, image_id=0, number=0, is_die=0):
        self.calibration_id = calibration_id
        self.identify_time = identify_time
        self.place_id = place_id
        self.image_id = image_id
        self.number = number
        self.is_die = is_die

    def toString(self):
        toStr = "calibration_id = "+str(self.calibration_id)+" identify_time = "+str(self.identify_time)+\
              " place_id = "+str(self.place_id)+" image_id = "+str(self.image_id)+" number = "+str(self.number)+\
              " is_die = "+str(self.is_die)
        return toStr

# 水系实体类
class Drainage:

    def __init__(self, drainage_id=0, name='name', type=0, address='address'):
        self.drainage_id = drainage_id
        self.name = name
        self.type = type
        self.address = address

    def toString(self):
        toStr = " drainage_id="+str(self.drainage_id)+" name="+self.name+\
              " type="+str(self.type)+" address="+self.address
        return toStr

# 水尺图像实体类
class Image:

    def __init__(self, image_id=0, shoot_time=time.time(), place_id=0, path='path' ):
        self.image_id = image_id
        self.shoot_time = shoot_time
        self.place_id = place_id
        self.path = path

    def toString(self):
        toStr = " image_id="+str(self.image_id)+" shoot_time="+str(self.shoot_time)+\
              " place_id="+str(self.place_id)+" path="+self.path
        return toStr

# 地点实体类
class Place:

    def __init__(self, place_id=0, serial_number=0, address='address', monitor_time=time.time(), drainage_id=0, max_num=0, die_line=0):
        self.place_id = place_id
        self.serial_number = serial_number
        self.address = address
        self.monitor_time = monitor_time
        self.drainage_id = drainage_id
        self.max_num = max_num
        self.die_line = die_line

    def toString(self):
        toStr = " place_id="+str(self.place_id)+" serial_number="+str(self.serial_number)+\
              " address="+self.address+" monitor_time="+str(self.monitor_time)+\
              " drainage_id="+str(self.drainage_id)+" max_num="+str(self.max_num)+\
              " die_line="+str(self.die_line)
        return toStr

# 将时间戳转为时间元组
def timeStamp_to_time(t):
    return time.localtime(t)