from urllib.request import urlopen
from bs4 import BeautifulSoup

html='''
<ul id="seven-day-forecast-list" class="list-unstyled"><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Tonight<br><br></p>
<p><img src="newimages/medium/nbkn.png" alt="Tonight: Mostly cloudy, with a low around 54. West southwest wind around 10 mph. " title="Tonight: Mostly cloudy, with a low around 54. West southwest wind around 10 mph. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Mostly Cloudy</p><p class="temp temp-low">Low: 54 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Monday<br><br></p>
<p><img src="newimages/medium/sct.png" alt="Monday: Mostly sunny, with a high near 67. West wind 7 to 16 mph, with gusts as high as 24 mph. " title="Monday: Mostly sunny, with a high near 67. West wind 7 to 16 mph, with gusts as high as 24 mph. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Mostly Sunny</p><p class="temp temp-high">High: 67 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Monday<br>Night</p>
<p><img src="newimages/medium/nbkn.png" alt="Monday Night: Increasing clouds, with a low around 54. West southwest wind 10 to 14 mph, with gusts as high as 21 mph. " title="Monday Night: Increasing clouds, with a low around 54. West southwest wind 10 to 14 mph, with gusts as high as 21 mph. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Increasing<br>Clouds</p><p class="temp temp-low">Low: 54 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Tuesday<br><br></p>
<p><img src="newimages/medium/bkn.png" alt="Tuesday: Mostly cloudy, with a high near 64. West southwest wind 8 to 13 mph, with gusts as high as 18 mph. " title="Tuesday: Mostly cloudy, with a high near 64. West southwest wind 8 to 13 mph, with gusts as high as 18 mph. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Mostly Cloudy</p><p class="temp temp-high">High: 64 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Tuesday<br>Night</p>
<p><img src="newimages/medium/nbkn.png" alt="Tuesday Night: Mostly cloudy, with a low around 55. West southwest wind 8 to 14 mph, with gusts as high as 21 mph. " title="Tuesday Night: Mostly cloudy, with a low around 55. West southwest wind 8 to 14 mph, with gusts as high as 21 mph. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Mostly Cloudy</p><p class="temp temp-low">Low: 55 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Wednesday<br><br></p>
<p><img src="newimages/medium/bkn.png" alt="Wednesday: Partly sunny, with a high near 66." title="Wednesday: Partly sunny, with a high near 66." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Partly Sunny</p><p class="temp temp-high">High: 66 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Wednesday<br>Night</p>
<p><img src="newimages/medium/nbkn.png" alt="Wednesday Night: Mostly cloudy, with a low around 55." title="Wednesday Night: Mostly cloudy, with a low around 55." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Mostly Cloudy</p><p class="temp temp-low">Low: 55 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Thursday<br><br></p>
<p><img src="newimages/medium/sct.png" alt="Thursday: Mostly sunny, with a high near 65." title="Thursday: Mostly sunny, with a high near 65." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Mostly Sunny</p><p class="temp temp-high">High: 65 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Thursday<br>Night</p>
<p><img src="newimages/medium/nsct.png" alt="Thursday Night: Partly cloudy, with a low around 55." title="Thursday Night: Partly cloudy, with a low around 55." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Partly Cloudy</p><p class="temp temp-low">Low: 55 °F</p></div></li></ul>
'''
soup = BeautifulSoup(html, 'html.parser')

find_1=soup.find_all('p', {'class':'period-name'})
find_2=soup.find_all('img', {'class':'forecast-icon'})
find_3=soup.find_all('p', {'class':'short-desc'})
find_4=soup.find_all('p',{'class':'temp'})
print(f'[find 함수 사용]')
print(f'총 tomestone-container 검색 개수: {len(find_1)}')
for i in range (len(find_1)):
    print(f'--------------------------------------------------------------------------------')
    print(f'[Period]: {find_1[i].get_text()}')
    print(f'[Short desc]: {find_3[i].get_text()}')
    print(f'[Temperature]: {find_4[i].get_text()}')
    print(f'[Image desc]: {find_2[i]["title"]}')

select_1=soup.select('p.period-name')
select_2=soup.select('img.forecast-icon')
select_3=soup.select('p.short-desc')
select_4=soup.select('p.temp')
for i in range (len(select_1)):
    print(f'--------------------------------------------------------------------------------')
    print(f'[Period]: {select_1[i].get_text()}')
    print(f'[Short desc]: {select_3[i].get_text()}')
    print(f'[Temperature]: {select_4[i].get_text()}')
    print(f'[Image desc]: {select_2[i]["title"]}')