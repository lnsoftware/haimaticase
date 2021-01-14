import requests
import jsonpath
from creatgiftcard import login_id
from config import LoginConfig as l


def batch_creat():
    url = l.bms_host + '/himo_product/admin/preferential_card/batch_create'
    # 折扣券参数
    data1 = {
	"title": "1",
	"count": 1,
	"tempType": "discount_coupon",
	"template_id": 5049,
	"discount": "6",
	"time": ["2020-12-24 00:00:00", "2021-01-31 23:59:59"],
	"buy_channel": "personal",
	"start_usage": "2020-12-24 00:00:00",
	"stop_usage": "2021-01-31 23:59:59"
}
    # 立减券参数  id 3123 每天可用的立减券  id 1221 周末不可用的立减券  pre通用立减id5037  折扣5038
    data = {
	"title": "111",
	"count": 1,
	"tempType": "decrease_coupon",
	"template_id": 5037,
	"discount": "300",
	"time": ["2020-09-25 00:00:00", "2021-01-27 23:59:59"],
	"buy_channel": "personal",
	"start_usage": "2020-09-27 00:00:00",
	"stop_usage": "2021-01-27 23:59:59"
}

    # 加修券3264
    # data = {
    #         "title": "1",
    #         "count": 1,
    #         "tempType": "ds_repair",
    #         "template_id": 3269,
    #         "time": ["2020-10-16 00:00:00", "2021-11-30 23:59:59"],
    #         "buy_channel": "personal",
    #         "start_usage": "2020-10-16 00:00:00",
    #         "stop_usage": "2021-11-30 23:59:59",
    #         "discount": 20
    # }
    # kids加修券  3268 ds_repair 加印卷3269 ds_print
#     data = {
# 	"title": "1",
# 	"count": 1,
# 	"tempType": "ds_print",
# 	"template_id": 3269,
# 	"time": ["2020-10-16 00:00:00", "2021-11-25 23:59:59"],
# 	"buy_channel": "personal",
# 	"start_usage": "2020-10-16 00:00:00",
# 	"stop_usage": "2021-11-25 23:59:59",
# 	"discount": 20,
# 	"apply_in": "kids"
# }
#     data = {
#         "count": 1,
#         "title": "1111",
#         "buy_channel": "personal",
#         "tempType": "decrease_coupon",
#         "template_id": 3395,
#         "discount": "1000",
#         "start_usage": "2020-10-26 10:30:07",
#         "stop_usage": "2021-10-31 23:59:59"
#     }
    res = requests.post(url=url,headers=l.bms_headers,json=data)
    res = res.json()
    msg = res['msg']
    return msg

def get_card():
    url = l.bms_host + '/himo_product/admin/preferential_card/all'
    params = {
        "create_log_id": batch_creat(),
        "created_at_start": "2020-09-09 11:38:26",
        "created_at_end": "2021-09-30 11:38:26",
        # "apply_in": "kids"
    }

    res = requests.get(url=url,headers=l.bms_headers,params=params)
    msg =res.json()['msg']
    # code = jsonpath.jsonpath(res, '$..code')[0]
    for i in msg:
        discode = i['code']
    return discode


def bind_coupons():
    url = l.bms_host + '/appointment_platform/user/preferential/bind_preferential_code'
    data = {
    "preferentialCode":get_card()
}
    headers = {
        'x-stream-id': login_id()

    }
    res = requests.post(url=url,headers=headers,json=data)
    if res.status_code == 200:
        print("优惠券绑定成功")
    else:
        print("绑定失败")
    print(res.json())

if __name__ == '__main__':
    bind_coupons()
