from flask import Flask, request
import json
import requests
from config import LoginConfig as l
app = Flask(__name__)

@app.route("/bind/coupon", methods=["post"])
def bind_coupon():
    # 默认返回内容
    return_dict = {'return_code': '200', 'result': None}

    # 判断传入的json数据是否为空
    if len(request.get_data()) == 0:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    coupon_type = str(request.values.get('coupon_type'))
    template_id = request.values.get('template_id')
    discount = str(request.values.get('discount'))
    host = request.values.get('host')
    phone = request.values.get('phone')
    password = request.values.get('password')
    url = host + '/himo_product/admin/preferential_card/batch_create'
    data = {
        "title": "1",
        "count": 1,
        "tempType": coupon_type,
        "template_id": template_id,
        "discount": discount,
        "time": ["2020-12-24 00:00:00", "2022-01-31 23:59:59"],
        "buy_channel": "personal",
        "start_usage": "2020-12-24 00:00:00",
        "stop_usage": "2022-01-31 23:59:59"
    }

    res = requests.post(url=url, headers=l.bms_headers, json=data)
    log_id = res.json()['msg']
    url1 = host + '/himo_product/admin/preferential_card/all'
    params = {
        "create_log_id": log_id,
        "created_at_start": "2020-09-09 11:38:26",
        "created_at_end": "2021-09-30 11:38:26"
    }
    msg = requests.get(url=url1, headers=l.bms_headers, params=params).json()['msg']
    for i in msg:
        discode = i['code']

    url2 = host + '/user_auth/login/pass'
    data1 = {'phone': phone, 'pass': password, 'brand': 'mainto_app', 'temp_token': ''}
    token = requests.get(url=url2, params=data1).headers['x-stream-id']
    print(token)
    url3 = host + '/appointment_platform/user/preferential/bind_preferential_code'
    data2 = {"preferentialCode": discode}
    headers = {'x-stream-id': token}
    r = requests.post(url=url3, json=data2, headers=headers)
    print(r.json())

    # 对参数进行操作
    return_dict['result'] = "优惠券绑定成功"
    print(return_dict)
    return json.dumps(return_dict, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8889')
