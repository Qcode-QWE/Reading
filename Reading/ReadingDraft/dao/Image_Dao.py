from Reading.ReadingDraft.Utils import mysql
from Reading.ReadingDraft.pojo import table

# 将查询结果转化为Image对象
def sqlToImage( rows ):
    list = []
    for row in rows:
        p = table.Image(row[0], row[1], row[2], row[3])
        list.append(p)
    return list

# 根据id查询Image对象
def find_By_Image( id ):
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,shoot_time,place_id,path" +
           " from image " +
           " where id = " + str(id)
           )
    cur.execute(sql)
    rows = cur.fetchall()
    p = sqlToImage(rows)[0]
    cur.close()
    con.close()
    return p

# 根据地点来获取数据库中最近一张水尺图片
def get_Image_By_Place_last( place ):
    place_id = place.place_id
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,shoot_time,place_id,path" +
           " from image " +
           " where place_id = " + str(place_id) +
           " and shoot_time = (select max(shoot_time) from image)"
           )
    cur.execute(sql)
    rows = cur.fetchall()
    p = sqlToImage(rows)[0]
    return p


