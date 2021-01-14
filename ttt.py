import requests
requests.packages.urllib3.disable_warnings()
content = requests.get("https://himo-miniapp-test.local.hzmantu.com/himo_product/admin/gift_card/create", verify=False)