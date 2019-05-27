import pymysql

# 数据库连接工具类

# 连接数据库
def connect_wxremit_db():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='123456',
                           database='draft',
                           use_unicode=True,
                           charset='utf8')


