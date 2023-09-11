from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html=requests.get("https://search.naver.com/search.naver?query=대구+날씨")
soup=BeautifulSoup(html.text, "html.parser")
select1=soup.select_one("h2.title")
select2= soup.select_one("div.temperature_text")
select3= soup.select_one("span.weather")
select4= soup.select("div.weather_info>div>div.report_card_wrap>ul>li")
select5 = soup.select("div.graph_inner._hourly_weather>ul>li>dl")

print(f"현재 위치 : {select1.get_text()}")
print(f'현재 온도 : {select2.get_text()}')
print(f'날씨 상태 : {select3.get_text()}')
for _ in select4:
    print(_.get_text())
print(f'-----------------------\n시간대별 날씨 및 온도\n-----------------------')
for _ in select5:
    print(_.get_text())