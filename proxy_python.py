from bs4 import BeautifulSoup
import requests
import pandas as pd


headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"}

r = requests.get('https://free-proxy-list.net/', headers=headers)

soup = BeautifulSoup(r.content,'html.parser')
proxiesRaw = soup.find_all('textarea', class_="form-control")[0].text
proxiesList = proxiesRaw[73:].strip()

with open("proxies.txt","w") as f:
 for p in proxiesList:
  f.writelines(p)