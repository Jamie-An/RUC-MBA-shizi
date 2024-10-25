# 获取 RUC-MBA-师资列表信息

# 1、添加使用到的库
import urllib3
http = urllib3.PoolManager()

# 2、请求数据
url = 'https://www.rmbs.ruc.edu.cn/common/shizi.json'
headers = {
    'content-type': 'application/json',
    'Accept': '*/*'
}
rep = http.request('GET', url, headers)
print(rep.status)

# 3、输出结果保存到文件中备用
dataFile = open('./output/shizi.txt', 'a')
dataFile.write(rep.data.decode('utf-8'))
dataFile.close()






# 一个使用正则的案例
# import re;
# source 
# key = r'<html><body><h1>hello world</h1></body></html>'
# 正则
# p = r'(?<=h1>).+?(?=</h1>)'
# 编译正则
# pattern = re.compile(p)
# 匹配查找
# matcher = re.search(pattern, key)
# 输出
# print(matcher.group(0))

# 输出文件
# file = open('./1.txt', 'a')
# file.write(matcher.group(0))
# file.close()



