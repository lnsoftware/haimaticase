import requests
from db_utils import update_order_staues, get_user_id
import jsonpath
import json
import datetime
from config import LoginConfig as l
import urllib3
urllib3.disable_warnings()

# requests = requests.sessions()
# requests.verify = False
# phone = "18157566498"
# re_time = "2020-10-21 21:30:00"


# 创建订单
def creatorder():
    data = {
        "type": "person_order",
        "userId": 999999003,
        "userName": "test",
        "userPhone": "18157566499",
        "userSex": "male",
        "userBirthday": "2009-02-01 00:00:00",
        "money": 159,
        "reachedPeopleNum": 1,
        "realMoney": 159,
        "reserveTime": str(datetime.date.today())+' 19:30:00',
        "productInfo": [{
            "productId": 5403,
            "isPrimary": 1,
            "parentId": 0,
            "productName": "精致签证照-精致签证照",
            "productImage": "https://fed.dev.hzmantu.com/erp2/精致签证照.jpg",
            "productPrice": "159.00",
            "productMoney": 159,
            "peopleNum": 1,
            "photosNum": 1,
            "num": 1,
            "addNumber": "39wb1mojhc80",
            # "orderSaleId": "null",
            "retakeSkuId": 0,
            "userSex": "male",
            "skuInfo": {
                "addPeoplePrice": "0.00"
            }

        }]
    }


    url = l.store_host + '/himo_product_store/admin/order/create'
    res = requests.post(url=url, headers=l.store_headers, json=data,verify=False)
    res = res.json()
    print(res)
    order_id = res['msg']['id']
    order_no = res['msg']['order_no']
    order_diffid = res['msg']['order_diff']['id']

    # 支付订单
    data1 = {
        "id": order_id,
        "payType": "cash",
        "diffType": "order",
        "orderDiffId": order_diffid
    }
    zf_url = l.store_host + '/himo_product_store/admin/order/paid'
    pay = requests.post(url=zf_url, headers=l.store_headers, json=data1,verify=False)
    a = pay.json()['msg']['order_sale_sku'][0]['id']


    # 到店签到
    data2 = {
        "orderId": order_id,
        "staffId": 608205,
        "skipMakeUp": "false",
        "saleSkuSex": [{
            "orderSaleSkuId": a,
            "sex": "male"
        }]
    }
    qd_url = l.store_host + '/project_paperless/manage/process/user_sign_in'
    qiandao = requests.post(url=qd_url, headers=l.store_headers,json=data2,verify=False)

    print(qiandao.json())

    # 获取processid
    data3 = {
		"storeId": 1080,
        "status": "working"
    }
    process_url = l.store_host + '/project_paperless/manage/order/paperless_orders'
    get_process = requests.get(url=process_url,headers=l.store_headers,params=data3,verify=False)
    process_json = get_process.json()
    print(process_json)
    process_id = jsonpath.jsonpath(process_json,"$..process_id")[0]

    # 添加订单给摄影师
    data4 = {
        "orderId": order_id
    }
    push_url = l.store_host + '/project_paperless/manage/cameraman/push_order_to_cameraman'
    push_order = requests.post(url=push_url,headers=l.store_headers,json=data4,verify=False)
    print(push_order.json())
    # 云端上传照片
    tj_url = l.store_host + '/project_paperless/manage/cameraman/complete_select_photo'
    tj_data = {
        "retouchClaim": {
            "eye": "small",
            "face": "middle",
            "pimples": "true"
        },
        "takeTime": "today",
        "retouchNote": "1",
        "photoData": [{
            "path": "2021/03/18/FhqnaLdrEN7HO_vo9Kpg9WZWOPIQ.jpg",
            "peopleNum": 1,
            "spliceMark": "",
            "splicePosition": "",
            "type": "normal",
            "file": {
                "status": "success",
                "name": "ljj3UXg3uaY_C0DJ4kBsitaVV8UJ.jpg",
                "size": 291032,
                "percentage": 100,
                "uid": 1616049373200,
                "raw": {
                    "uid": 1616049373200
                },
                "response": {
                    "url": "upload_dev/2021/03/18/FhqnaLdrEN7HO_vo9Kpg9WZWOPIQ.jpg"
                }
            },
            "isNewUpload": "false"
        }],
            "orderId": order_id,
            "productId": 5403,
            "serviceId": 0,
            "saleSkuId": a,
            "processId": process_id
    }

    select_photo = requests.post(url=tj_url, headers=l.store_headers, json=tj_data,verify=False)
    print(select_photo.json())
    msg = select_photo.json()['msg']
    stream_num = msg['stream_num']
    print(stream_num)

if __name__ == '__main__':
    creatorder()
