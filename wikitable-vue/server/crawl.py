import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/France"

response = requests.get(url)

# 检查请求是否成功
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'lxml')
    
    # 查找所有 class 为 'infobox' 的表格
    infobox_tables = soup.find_all('table', class_='infobox')
    
    # 遍历并打印每个 infobox 表格
    for i, table in enumerate(infobox_tables):
        print(f"Infobox Table {i + 1}:")
        
        # 将表格解析为 DataFrame
        df = pd.read_html(str(table))[0]
        print(df)
        
        print("\n" + "=" * 50 + "\n")  # 分隔符
else:
    print(f"请求失败，状态码: {response.status_code}")