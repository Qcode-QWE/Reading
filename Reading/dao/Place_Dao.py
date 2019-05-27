from Reading.Utils import mysql
from Reading.pojo import table


# 将查询结果转化为Place对象
def sqlToPlace( rows ):
    list = []
    for row in rows:
        p = table.Place(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        list.append(p)
    return list

# 根据id查询Place对象
def find_By_Place( id ):
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,serial_number,address,monitor_time,drainage_id,max_num,die_line" +
           " from place " +
           " where id = " + str(id)
           )
    cur.execute(sql)
    rows = cur.fetchall()
    p = sqlToPlace(rows)[0]
    cur.close()
    con.close()
    return p

# 获取所有的地点
def get_all_place():
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,serial_number,address,monitor_time,drainage_id,max_num,die_line" +
           " from place "
           )
    cur.execute(sql)
    rows = cur.fetchall()
    ps = sqlToPlace(rows)
    cur.close()
    con.close()
    return ps