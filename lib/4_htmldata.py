# 进一步提取详情信息
import urllib3
http = urllib3.PoolManager()
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

# 读取数据
def read_file(file_path):   # 读取文件
    with open(file_path, 'r') as f:
        config_data = json.load(f) # 反序列化为python对象
        return config_data
cur_data = read_file('./output/newshizi.json')

# 封装请求函数    
def get_html_info(url):
    rep = http.request('GET', url)
    soup = BeautifulSoup(rep.data, 'html.parser')  # 预处理返回格式
    return soup

# 封装一个查找正则
def re_match(k):
    key = r'{}'.format(k)
    # print(key)
    # 正则表达式
    # <span>电话：8610-82500479 </span>
    # p = r'(?<=h1>).+?(?=</h1>)'
    p = r'(?<=title>).+?(?=</title>)'
    pattern = re.compile(p)
    # 匹配查找
    matcher = re.search(pattern, key)
    # 输出
    if matcher:
        print(matcher.group(0))  # 如果 matcher 不为 None，则输出匹配的结果
        return matcher.group(0)
    else:
        print("没有找到匹配项。")
        return ''

# 简化，只执行一遍
for index, val in enumerate(cur_data['data']):
    cur_url = cur_data['data'][index]['个人详情']
    print(cur_url)   # 检查详情页地址
    add_val = get_html_info(cur_url)  # 请求并解析新的数据
    cur_data['data'][index]['电话'] = re_match(add_val)  # 合并数据
    break


# 输出新的结构文件
with open("./output/endshizi.json", "w", encoding="utf-8") as f:
    json.dump(cur_data, f, ensure_ascii=False, indent=4)



