from Reading.ReadingDraft.Utils import mysql
from Reading.ReadingDraft.pojo import table
from Reading.ReadingDraft.Utils import utils
# 将查询结果转化为Calibration对象
def sql_To_Calibration( rows ):
    list = []
    for row in rows:
        p = table.Calibration(row[0], row[1], row[2], row[3], row[4], row[5])
        list.append(p)
    return list

# 根据id查询Calibration对象
def find_By_CalibrationId( id ):
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,identify_time,place_id,image_id,number,is_die " +
           " from calibration " +
           " where id = " + str(id)
           )
    cur.execute(sql)
    rows = cur.fetchall()
    p = sql_To_Calibration(rows)[0]
    cur.close()
    con.close()
    return p
# 根据image获取calibration
def get_By_Image(image):
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,identify_time,place_id,image_id,number,is_die " +
           " from calibration " +
           " where image_id = " + str(image.image_id)
           )
    cur.execute(sql)
    rows = cur.fetchall()
    p = int(0)
    if rows.__len__() > 0:
        p = sql_To_Calibration(rows)[0]
    cur.close()
    con.close()
    return p

# 将刻度保存到数据库中
def save(calibration):
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("insert into calibration(identify_time,place_id,image_id,number,is_die) " +
           "values(%s,%s,%s,%s,%s)"
           )
    values = [calibration.identify_time,calibration.place_id,calibration.image_id,calibration.number,calibration.is_die]
    cur.execute(sql, values)
    con.commit()
    cur.close()
    con.close()


# 获取place最近一次的刻度
def get_by_place_last(place):
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,identify_time,place_id,image_id,number,is_die " +
           " from calibration " +
           " where place_id = " + str(place.place_id) +
           " order by identify_time desc limit 1"
           )
    cur.execute(sql)
    rows = cur.fetchall()
    p = int(0)
    if rows.__len__() > 0:
        p = sql_To_Calibration(rows)[0]
    cur.close()
    con.close()
    return p