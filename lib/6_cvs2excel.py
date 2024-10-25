# cvs 转为 excel
import pandas as pd

# 读取 CSV 文件
csv_file = './output/endshizi.csv'  
data = pd.read_csv(csv_file)
# 将数据写入 Excel 文件
excel_file = './output/shizi.xlsx'  # 输出的 Excel 文件名
data.to_excel(excel_file, index=False, engine='openpyxl')
print("CSV 文件已成功转换为 Excel 文件！")