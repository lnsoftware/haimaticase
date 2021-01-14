import requests
from db_utils import get_order_id
from config import LoginConfig as l


stream_num = "C2020123155670955"
# order_id = get_order_id(stream_num)
order_id = 13530237
def shenhe_order():
    #
    # data = {
    #     "order_id": order_id
    # }
    # shenhe_url = l.store_host + '/himo_product_store/photo/second_retoucher/bind_checker'
    # res = requests.post(url=shenhe_url,headers=l.store_headers, json=data)
    # print(res.json)

    data1 = {
	"photo": {
		"cover_photo": {}
	},
	"streamNum": stream_num
}
    tijiao_url = l.store_host + '/project_paperless/manage/second_retoucher/review'
    tijiao = requests.post(url=tijiao_url,headers=l.store_headers,
                           json=data1)

    print(tijiao.json())

    # 看片签到
    data2 = {
        "orderId":order_id
    }
    look_url = l.store_host + '/project_paperless/manage/process/retouch_sign_in'
    looksignin = requests.post(url=look_url,headers=l.store_headers,json=data2)
    print(looksignin.json())

    # 开启门店接单
    data3 = {
	"staffId": 613646,
	"staffType": "kps"
}
    begin_url = l.store_host + '/project_paperless/manage/staff/begin_work'
    begin_work = requests.post(url=begin_url,headers=l.store_headers,json=data3)
    print(begin_work.json())

    # 门店提交看片
    data4 = {
	"streamNum": stream_num,
	"photoData": [{
		"path": "2020/06/17/ljj3UXg3uaY_C0DJ4kBsitaVV8UJ.jpg",
		"id": 27331421,
		"sizeData": "原始尺寸"
	}]
}
    submit_url = l.store_host + '/project_paperless/manage/second_retoucher/submit_final_photo'
    submit_res = requests.post(url=submit_url,headers=l.store_headers,json=data4)
    print(submit_res.json())

    # 关闭门店看片接单
    end_url = l.store_host + '/project_paperless/manage/staff/end_work'
    end_work = requests.post(url=end_url,headers=l.store_host)
    print(end_work.json())
if __name__ == '__main__':
    shenhe_order()
