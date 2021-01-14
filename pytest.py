import requests

# a = 0
# while a < 10 :
#     a = a+1
#     if a % 2 == 0:
#         continue
#     print(a)
# a = " "
# while a != 'quit':
#     a = input()
#     print(a)

# print("请问你的年龄是多少？")
# a = int(input())
# while a > 0:
#     if  a < 3:
#         print("免费")
#         break
#     elif 3 <= a < 12:
#         print("10美元")
#         break
#     else:
#         print("15美元")
#         break

# begin_orders = ['og','ag','bg','og','og']
# print("og都卖完了")
# while 'og' in begin_orders:
#     begin_orders.remove('og')
# finish_orders = []
# while begin_orders:
#     a = begin_orders.pop()
#     print(a)
#     finish_orders.append(a)
# print(finish_orders)

# def testone(a,b):
#     print(a)
#     print(b)
# testone(1,2)

# def name(first_name,second_name,third_name=''):
#     if third_name:
#         all_name = first_name + ' ' + second_name + ' ' + third_name
#     else:
#         all_name = first_name + ' ' + second_name
#     return all_name.title()
#
# print(name('无敌','牛逼','风火轮'))
# print(name('无敌','牛逼'))

# testnames = ['abc','bcd','cde']
# def great_name(names):
#     for name in names:
#         if name != 'abc':
#             msg = "hello," + name + "!"
#             print(msg)
#
# great_name(testnames)
# var = 'abcd'
# print(var[1:3])
from appium import webdriver
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# from appium import webdriver
#
# caps = {}
# caps["platformName"] = "Android"
# caps["platformVersion"] = "10.0.0"
# caps["deviceName"] = "TAS-AL00"
# caps["appPackage"] = "cn.mainto.maintoapp"
# caps["appActivity"] = ".ui.activity.MainActivity"
# caps["ensureWebviewsHavePages"] = True
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.Button")
# el3.click()
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.Button")
# el4.click()
# el5 = driver.find_element_by_id("cn.mainto.maintoapp:id/btnSelected")
# el5.click()
# el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]")
# el6.click()
# el7 = driver.find_element_by_id("cn.mainto.maintoapp:id/ivHomeUp")
# el7.click()
# el8 = driver.find_element_by_id("cn.mainto.maintoapp:id/ibCart")
# el8.click()
# el9 = driver.find_element_by_id("cn.mainto.maintoapp:id/btnSelectDate")
# el9.click()
# el10 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]")
# el10.click()
#
# driver.quit()




















