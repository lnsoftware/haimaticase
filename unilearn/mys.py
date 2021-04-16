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
    host='8.129.215.246',
    port=3306,
    user='root',
    password='123456',
    database='test',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
# 创建游标
cursor = conn.cursor()
# 需要执行的sql语句
sql = 'SELECT phone,pwd FROM person WHERE pname="lemon"'
cursor.execute(sql)
#增删改需要commit，查询不需要
# conn.commit()
results = cursor.fetchone()
print(results['phone'],results['pwd'])
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
