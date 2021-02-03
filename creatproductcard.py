import requests
from config import LoginConfig as l
from creatgiftcard import login_id
def getproduct_gift():
    url = l.bms_host + '/himo_product/admin/product_card_order/input'
    # 通用产品券模版id873，可用于最大人数
    # 证件照-正面-白色产品券参数870
    data = {
        "buy_channel": "personal",
        "type": "virtual",
        "user_name": "1",
        "phone": "19999999991",
        "pay_type": "cash",
        "sex": "male",
        "ori_money": 918,
        "pay_money": "918",
        "extend": {
            "count": 1,
            "stop_usage": "2021-12-31 23:59:59",
            "start_usage": "2020-11-30 00:00:00",
            "template_id": 1078,
            "title": "1"
        }
    }
    res =requests.post(url=url,headers=l.bms_headers,json=data,verify=False)
    msg = res.json()['msg']
    for i in msg:
        code = i['code']
    return code

def use_productcard():
    url = l.h5_host + '/appointment_platform/user/preferential/bind_preferential_code'
    headers = {
        'x-stream-id': login_id(phone=18157566499,password=123456)
    }
    data = {
        "preferentialCode": getproduct_gift()
    }
    res = requests.post(url=url,headers=headers,json=data,verify=False)
    if res.status_code == 200:
        print("产品卡绑定成功")
    else:
        print("绑定失败")
    # res = res.json()
    # print(res)

if __name__ == '__main__':
    use_productcard()
