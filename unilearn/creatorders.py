import requests
from db_utils import update_order_staues, get_user_id
from config import LoginConfig as l

# requests = requests.sessions()
# requests.verify = False
# phone = "18157566498"
# re_time = "2020-10-21 21:30:00"
# userid = get_user_id(phone)


# 创建订单
def creatorder():
    data = {
	"type": "person_order",
	"userId": 7659598,
	"userName": "lemon",
	"userPhone": "18157566499",
	"userSex": "male",
	"userBirthday": "2000-01-31 00:00:00",
	"money": 159,
	"reachedPeopleNum": 1,
	"realMoney": 159,
	"reserveTime": "2021-01-13 20:10:00",
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
		"addNumber": 1610336315099,
		"skuInfo": {
			"addPeoplePrice": "0.00"
		},
		"userSex": "male"
	}]
}



    url = l.store_host + '/himo_product_store/admin/order/create'
    res = requests.post(url=url, headers=l.store_headers, json=data)
    res = res.json()
    order_id = res['msg']['id']
    order_diffid = res['msg']['order_diff']['id']


    # 支付订单
    data1 = {
        "id": order_id,
        "payType": "cash",
        "diffType": "order",
        "orderDiffId": order_diffid
    }
    zf_url = l.store_host + '/himo_product_store/admin/order/paid'
    pay = requests.post(url=zf_url, headers=l.store_headers, json=data1)
    order_id = pay.json()['msg']['id']
    print(order_id)
    # 到店签到
    data2 = {
        "orderId": order_id,
        "staffId": 608205,
        "skipMakeUp": "false",
        "saleSkuSex": [{
            "orderSaleSkuId": 13685244,
            "sex": "male"
        }]
    }
    qd_url = l.store_host + '/project_paperless/manage/process/user_sign_in'
    qiandao = requests.post(url=qd_url, headers=l.store_headers,json=data2)

    print(qiandao.json())

    # 添加订单给摄影师
    data3 = {
	"orderId": order_id
    }
    push_url = l.store_host + '/project_paperless/manage/cameraman/push_order_to_cameraman'
    push_order = requests.post(url=push_url,headers=l.store_headers,json=data3)
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
		"path": "2021/01/13/FpVElcsxwtcZXqtrNIFbf1Uad5_W.jpg",
		"peopleNum": 1,
		"spliceMark": "",
		"splicePosition": "",
		"type": "normal",
		"file": {
			"status": "success",
			"name": "10001.jpg",
			"size": 187750,
			"percentage": 100,
			"uid": 1610528496343,
			"raw": {
				"uid": 1610528496343
			},
			"response": {
				"url": "upload_dev/2021/01/13/FpVElcsxwtcZXqtrNIFbf1Uad5_W.jpg"
			}
		},
		"isNewUpload": "false"
	}],
	"orderId": order_id,
	"productId": 5403,
	"serviceId": 0,
	"saleSkuId": 13685295,
	"processId": 4223536
}

    select_photo = requests.post(url=tj_url, headers=l.store_headers, json=tj_data)
    msg = select_photo.json()['msg']
    stream_num = msg['stream_num']
    print(stream_num)
creatorder()
