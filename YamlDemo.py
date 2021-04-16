import yaml
import os


# 获取当前脚本所在文件夹路径
curlPath =os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
print(curlPath)
yamlPath = os.path.join(curlPath,"test.yaml")
print(yamlPath)
# 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
f = open(yamlPath,'r',encoding='utf-8')
cont = f.read()
x = yaml.load(cont)
print(x)
print(x['rightLogin']['phone'])