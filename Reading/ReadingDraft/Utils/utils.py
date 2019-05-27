import time,datetime

# 系统的工具类

# 将datetime类型插入到数据库前需要先转换
def mysql_date(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

# 获取当前时间
def get_now_time():
    t = datetime.datetime.now()
    return t
