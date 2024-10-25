import pandas as pd
import json

# 读取 JSON 文件
with open("./output/endshizi.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

# 将 JSON 数据转换为 DataFrame
df = pd.json_normalize(json_data['data'])

# 保存为 CSV 文件
df.to_csv("./output/endshizi.csv", index=False, encoding="utf-8")