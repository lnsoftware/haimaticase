from config import LoginConfig as l
import requests, re
from db_utils import *

ding_user_id = "111927205633700075"
appId = l.cloud_login_path


def get_authCode():
    sso_path = "/login/goto/eyJ0aXRsZSI6Iue8puWbvuS6keerryIsInJlZGlyZWN0IjoiY2xvdWQ6Ly9wcm9kdWN0aW9uL2xvZ2luLmh0bWwjLz90b2tlbj0ifQ=="
    cloud_login_path = l.cloud_login_url + sso_path
    res = requests.get(url=cloud_login_path)
    authCode = re.findall(r'authCode = \'(.+)\';', res.text)[0]
    assert len(authCode) >= 15
    return authCode


def get_login_token(authCode):
    ding_url = 'https://dingtalk.mpapi.haimati.cn/qrAuthDev/api.php'
    data = {'code': authCode, 'dtid': ding_user_id, 'event': 'hma_login'}
    res = requests.post(ding_url, data=data)
    res = res.json()
    assert res['error'] == 0
    quick_login_url = l.cloud_login_url + '/staff/checkQrLogin'
    data = {'authCode': authCode, 'appId': appId}
    res = requests.post(quick_login_url, data=data)
    res = res.json()
    return res['msg']


def get_login_token_(authCode, phone):
    ding_url = 'https://dingtalk.mpapi.haimati.cn/qrAuthDev/api.php'
    data = {'code': authCode, 'dtid': query_ding_u_id(phone), 'event': 'hma_login'}
    res = requests.post(ding_url, data=data)
    res = res.json()
    assert res['error'] == 0
    quick_login_url = l.cloud_login_url + '/staff/checkQrLogin'
    data = {'authCode': authCode, 'appId': "100"}
    res = requests.post(quick_login_url, data=data)
    res = res.json()
    return res['msg']


# print(get_login_token(get_authCode()))

def get_cloud_sso_x_stream_id(login_token):
    hma_mendian = l.dev_host + '/manage_auth/login/sso'
    params = {'token': login_token}
    res = requests.get(hma_mendian, params=params)
    res = res.headers
    print(res['x-stream-id'])
    return res['x-stream-id']


cloud_x_stream_id = get_cloud_sso_x_stream_id(get_login_token(get_authCode()))


def get_photographer_token():
    url = l.dev_host + '/project_cloud/authApi/getAccessToken'
    params = {
        'account': l.sys_org_account,
        'secret': l.sys_org_secret,
        'orgType': 'photographer'
    }
    res = requests.get(url=url, params=params)
    res = res.json()
    return res['msg']


photographer_token = get_photographer_token()



# get_cloud_sso_x_stream_id(login_token)

