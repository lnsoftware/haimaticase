import requests
import jsonpath
from config import LoginConfig as l

# requests = requests.session()
# requests.verify = False

def get_giftcode_msg():
    url = l.bms_host + '/himo_product/admin/gift_card_order/create'
    data = {
	"type": "virtual",
	"user_name": "1",
	"phone": "18157566499",
	"pay_type": "cash",
	"sex": "male",
	"ori_money": "400.00",
	"pay_money": 10,
	"buy_channel": "personal",
	"extend": {
		"money": "100000",
		"count": 1,
		"stop_usage": "2023-12-24 14:33:27",
		"start_usage": "2020-09-24 14:33:27",
		"cover_id": 1,
		"title": "1"
	}
}

    res = requests.post(url=url,headers=l.bms_headers,json=data)
    res = res.json()
    code = jsonpath.jsonpath(res, '$..code')[0]
    print(code)
    return code

def login_id(phone=18157566499,password=123456):
    url = l.h5_host + '/user_auth/login/pass'
    data = {
        'brand': 'mainto_app',
        'phone': phone,
        'pass': password,
        'temp_token': ''
    }
    res = requests.get(url=url, params=data)
    res = res.headers
    return res['x-stream-id']

def use_giftcode():
    url = l.h5_host + '/himo_product/user/gift_card/charge'
    data = {"code":get_giftcode_msg()}
    headers = {
        'x-stream-id': login_id()
    }
    res = requests.post(url=url,headers=headers, json=data)
    if res.status_code == 200:
        print("恭喜你礼品卡绑定成功")
    else:
        print("抱歉失败了")
if __name__ == '__main__':
    use_giftcode()


