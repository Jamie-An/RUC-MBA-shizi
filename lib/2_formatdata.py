# 将获取的json数据转为表格
import json

# 整理 JSON 数据
def read_file(file_path):   # 读取文件
    with open(file_path, 'r') as f:
        config_data = json.load(f) # 反序列化为python对象
        return config_data
cur_data = read_file('./output/shizi.json')

# 整理数据
new_data = {'data':[]}
for index, val in enumerate(cur_data['data']):
    new_data['data'].append({
        '序号': index+1,
        '姓名': val['title'],
        '照片': val['picUrl'],
        '个人详情': val['url'],
        '职称': val['properties']['职称'],
        '系别': val['properties']['系别'],
        '研究方向': val['properties']['研究方向'],
        '讲授课程': val['properties']['讲授课程']
    })
# print(new_data['data'][0])

# 输出新的结构文件
with open("./output/newshizi.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
