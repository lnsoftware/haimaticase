from config import LoginConfig as l
from db_utils import query_xps_is_in_green, get_steram_num, update_stream
from get_x_stream_id import *
import requests, jsonpath

cloud_id = cloud_x_stream_id  # 云端sso登录x-stream-id
query_xps_is_in_green(l.xps_staff_id)  # 查询修片师id是否在绿色通道，若不存在则添加
p_id = photographer_token  # 获取摄影师token
headers = {'x-stream-id': cloud_id}  # 请求头
_stream_num = "C2020112600449194"  # 流水号${$stream_num}
result = get_steram_num(_stream_num)  # 根据流水号查询的订单状态和id，返回的是一个字典{'id':..,'state':''}
_retouch_id = l.xps_staff_id  # 测试修片师员工号,必须为登录cookies的用户id
_lock_reviewer_id = ""  # 锁定审核人,空时则不锁定
_receipt_at = ""  # 设置照片接单时间,未填写时不变动,8:00~10:00的1.5倍经验是根据修片师接单时间验证
_is_success = True  # 是否正常测试,true,false
_assert_text = True  # 包含断言

if result['state'] != 'wait_retouch':  # 如果订单状态不是等待修片
    update_stream(_retouch_id, _stream_num)  # 强制修改流水接单修片师为测试修片师
else:
    url = l.dev_host + '/project_cloud/common/tR'
    params = {'staffId': _retouch_id, "streamId": result['id']}
    res = requests.get(url=url, params=params, headers=headers)  # 获取流水队列内的流水(接单)

url = l.dev_host + f'/project_cloud/retoucher/getStreamInfo?streamId={result["id"]}'
res = requests.get(url=url, headers=headers)  # 获取流水信息
res = res.json()
photo_id = jsonpath.jsonpath(res, '$..msg.photos.*.id')  # 获取返回数据中的所有photo_id
is_true_show = jsonpath.jsonpath(res, '$.msg.photos.*.photo_version[-1:].version')  # 获取返回数据中的version 判断是否需要重修
photoData = []
photoPath = l.xps_photo_3   # 控制最后返回的图片
url = l.dev_host + '/project_cloud/common/tRv'
res = requests.get(url=url, params={'streamId': result['id'], 'staffId': 613646}, headers=headers, verify=False)
print(res.json())
url = l.dev_host + '/project_cloud/reviewer/passStream'
res = requests.put(url=url, json={'streamId': result['id']}, headers=headers, verify=False)
print(res.json())

if "return_show" in is_true_show:
    for i in photo_id:
        photoData.append({"id": i, "path": photoPath})
else:
    for i in photo_id:
        photoData.append({"id": i, "path": photoPath})
if __name__ == '__main__':
    data = {'streamId': result['id'], 'photoData': photoData}
    url = l.dev_host + '/project_cloud/retoucher/submitStream'
    res = requests.put(url=url, json=data, headers=headers)
    print(res.json())
