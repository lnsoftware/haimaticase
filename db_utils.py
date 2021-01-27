from config import LoginConfig as l
import pymysql
from typing import Dict
from singleton import singleton

# data_base_config = {
#     'host': '192.168.188.12',
#     'user': 'root',
#     'password': 'u4bVDgdvELq6Nmhb',
#     'port': 33061
# }
data_base_config = {
    'host': 'mainto-rw-pre-outer.mysql.rds.aliyuncs.com',
    'user': 'pre',
    'password': 'Al7ug0EvXxTG6hFK',
    'port': 3306
}


class DB:
    def __init__(self, db_name):
        self.db = pymysql.connect(db=db_name, cursorclass=pymysql.cursors.DictCursor, **data_base_config)
        self.cur = self.db.cursor()

    def query_one(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res


    def query_all(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def execute_one(self, sql):
        self.cur.execute(sql)
        res = self.db.commit()
        return res

    def __del__(self):
        self.cur.close()
        self.db.close()
        del self.db


@singleton.Singleton
class DbManager:
    def __init__(self):
        self.dbs: Dict[str, DB] = {}

    def add_db(self, db_name):
        assert db_name not in self.dbs
        self.dbs[db_name] = DB(db_name)


    def remove_db(self, db_name):
        del self.dbs[db_name]

    def query_one(self, db_name, sql):
        return self.dbs[db_name].query_one(sql)

    def query_all(self, db_name, sql):
        return self.dbs[db_name].query_all(sql)

    def execute_one(self, db_name, sql):
        return self.dbs[db_name].execute_one(sql)

    def __del__(self):
        for db in self.dbs:
            del db


def check_db_connect(db_name):
    if db_name not in DBM.dbs:
        DBM.add_db(db_name)


DBM = DbManager.instance()  # type: DbManager


def query_xps_is_in_green(xps_id):
    check_db_connect(l.cloud_database_schemas)
    a = DBM.query_one(l.cloud_database_schemas, f'select id from green_channel_staffs where staff_id = {xps_id}')
    if not a:
        DBM.execute_one(l.cloud_database_schemas, f'INSERT INTO green_channel_staffs '
                                                  f'(staff_id, created_at, updated_at) VALUES ({xps_id}, '
                                                  f'"2019-11-25 16:45:13", "2019-11-25 16:45:13")')
        return 1
    return 1


def get_steram_num(stream_num):
    check_db_connect(l.cloud_database_schemas)
    result = DBM.query_one(l.cloud_database_schemas,
                           f'select id, state from streams where stream_num = '
                           f'"{stream_num}" and deleted_at is null')
    return result


def update_stream(retouch_id, stream_num):
    check_db_connect(l.cloud_database_schemas)
    DBM.execute_one(l.cloud_database_schemas,
                    f'update streams set retoucher_id={retouch_id} '
                    f'where stream_num = "{stream_num}"')
    return


def query_ding_u_id(phone):
    check_db_connect("himo-micro-staff")
    id = DBM.query_one("himo-micro-staff", f"select dingding_uid from "
                                           f"staff where phone={phone}")['dingding_uid']
    return id

def update_order_staues(order_no):
    check_db_connect("new-himo-micro-order")
    DBM.execute_one("new-himo-micro-order",f'UPDATE orders SET pending_status="select_photos" WHERE order_no="{order_no}"')
    return 1

def get_order_id(_stream_num):
    check_db_connect("himo-middle-photo")
    order_id = DBM.query_one("himo-middle-photo",f'select order_id from cloud_streams where stream_num="{_stream_num}"')
    return order_id
def get_user_id(phone):
    check_db_connect("himo-micro-user")
    user_id = DBM.query_one("himo-micro-user",F'select id from users where phone = "{phone}"')
    return user_id
# def get_sale_sku_id():

# print(query_ding_u_id(13676561839))
