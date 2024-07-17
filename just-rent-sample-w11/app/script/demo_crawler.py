import requests
from bs4 import BeautifulSoup

# 發送 GET 請求
r = requests.get('https://reurl.cc/NRkm2Q')

# 解析網頁
soup = BeautifulSoup(r.text, 'html.parser')

# 輸出網頁 HTML 程式碼
print(soup.prettify())
