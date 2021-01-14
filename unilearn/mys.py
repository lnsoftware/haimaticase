import pymysql
from unilearn.creatorders import *
# config = {
#     'host': '192.168.188.231',
#     'user': 'root',
#     'password': 'u4bVDgdvELq6Nmhb',
#     'port': 33061,
#     'datebase': 'himo-micro-user',
#     'charset': 'utf8'
# }
conn = pymysql.connect(
    host='192.168.188.12',
    port=33061,
    user='root',
    password='u4bVDgdvELq6Nmhb',
    database='new-himo-micro-order',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
# 创建游标
cursor = conn.cursor()
# 需要执行的sql语句
sql = 'UPDATE orders SET pending_status="select_photos WHERE order_no=?;'
cursor.execute(sql,[])
#增删改需要commit，查询不需要
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
