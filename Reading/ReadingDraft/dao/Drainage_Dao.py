from Reading.ReadingDraft.Utils import mysql
from Reading.ReadingDraft.pojo import table

# 将查询结果转化为Drainage对象
def sql_To_Drainage( rows ):
    list = []
    for row in rows:
        p = table.Drainage(row[0], row[1], row[2], row[3])
        list.append(p)
    return list

def find_By_DrainageId( id ):
    con = mysql.connect_wxremit_db()
    cur = con.cursor()
    sql = ("select id,name,type,address " +
           " from drainage " +
           " where id = " + str(id)
           )
    cur.execute(sql)
    rows = cur.fetchall()
    p = sql_To_Drainage(rows)[0]
    cur.close()
    con.close()
    return p

p = find_By_DrainageId(1)
print(p.toString())


