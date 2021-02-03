import requests
from db_utils import get_order_id
from config import LoginConfig as l
import jsonpath
import time

stream_num = "C2021013156911312"
# order_id = get_order_id(stream_num)
order_id = 13350311
def shenhe_order():

    data = {
        "orderId": order_id
    }
    checker_url = l.store_host + '/project_paperless/manage/second_retoucher/bind_checker'
    res = requests.post(url=checker_url,headers=l.store_headers, json=data,verify=False)
    # print(res.json)

    data1 = {
        "photo": {
            "cover_photo": {}
        },
        "streamNum": stream_num
    }
    review_url = l.store_host + '/project_paperless/manage/second_retoucher/review'
    review = requests.post(url=review_url,headers=l.store_headers,json=data1,verify=False)

    # print(review.json())

    # 看片签到
    data2 = {
        "orderId":order_id
    }
    retouch_url = l.store_host + '/project_paperless/manage/process/retouch_sign_in'
    retouch = requests.post(url=retouch_url,headers=l.store_headers,json=data2,verify=False)
    print(retouch.json())

    # 获取照片id
    photo_url = l.store_host + '/project_paperless/manage/second_retoucher/order_detail'
    photo = requests.get(url=photo_url,headers=l.store_headers,params=data2,verify=False)
    photo_json = photo.json()
    photo_idf = jsonpath.jsonpath(photo_json,"$..photo_id")[0]
    photo_ids = jsonpath.jsonpath(photo_json,"$..photo_id")[5]

    # 开启门店接单
    data3 = {
        "staffId": 613646,
        "staffType": "kps"
    }
    begin_url = l.store_host + '/project_paperless/manage/staff/begin_work'
    begin_work = requests.post(url=begin_url,headers=l.store_headers,json=data3,verify=False)
    print(begin_work.json())
    time.sleep(2)

    # 获取伙伴状态
    staff_url = l.store_host + '/project_paperless/manage/staff/get_staff_status'
    get_staff_status = requests.get(url=staff_url,headers=l.store_headers,verify=False)

    # 门店提交看片
    data4 = {
        "streamNum": stream_num,
        "photoData": [{
            "path": "2020/08/31/li3nH1V3HtAQS65rKhoTpkmLy69d.jpg",
            "id": photo_idf,
            "sizeData": "原始尺寸"
        }, {
            "path": "2020/08/31/lmVnQPLYXop5F1vChS7ZakHbU036.jpg",
            "id": photo_ids,
            "sizeData": "原始尺寸"
        }]
    }
    submit_url = l.store_host + '/project_paperless/manage/second_retoucher/submit_final_photo'
    submit_res = requests.post(url=submit_url,headers=l.store_headers,json=data4,verify=False)
    print(submit_res.json())

    # 关闭门店看片接单
    end_url = l.store_host + '/project_paperless/manage/staff/end_work'
    end_work = requests.post(url=end_url,headers=l.store_headers,json=data3,verify=False)
    print(end_work.json())

    # 门店完成订单
    data5 = {
	    "id": order_id
    }
    finish_url = l.store_host + '/himo_product_store/admin/order/finish'
    order_finish = requests.post(url=finish_url,headers=l.store_headers,json=data5,verify=False)
    print(order_finish.json())

    # 录入工作量
    data6 = {
	"orderId": order_id,
	"workloads": [{
		"staff_id": 608205,
		"staff_type": "qt",
		"work_per": "100.00"
	}, {
		"staff_id": 604064,
		"staff_type": "hzs",
		"work_per": "100.00"
	}, {
		"staff_id": 605727,
		"staff_type": "sys",
		"work_per": "100.00"
	}]
}
    workloads_url = l.store_host + '/himo_product_store/admin/order/set_order_workloads'
    workloads = requests.post(url=workloads_url,headers=l.store_headers,json=data6,verify=False)
    print(workloads.json())
if __name__ == '__main__':
    shenhe_order()
