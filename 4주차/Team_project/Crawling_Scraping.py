from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import requests
import selenium
from selenium import webdriver
import pandas as pd
import matplotlib as plt
import csv

# Scraping1 쿠팡의 수익 극대화를 위한 AI 활용 방법
driver_1 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_1.get(f'https://ayuls.tistory.com/297#1_AI_%EB%B6%84%EC%84%9D%EC%9D%84_%ED%86%B5%ED%95%9C_%EC%A0%9C%ED%92%88_%EC%B6%94%EC%B2%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C')
soup_1 = BeautifulSoup(driver_1.page_source, 'html.parser')
content_1 = []
content_1.append(soup_1.select_one(r'#\31 _AI_분석을_통한_제품_추천_시스템').text)
content_1.append(soup_1.select_one('#content > div > div.entry-content > div.contents_style > p:nth-child(8)').text)
content_1.append(soup_1.select_one(r'#\32 _AI_기반_협업_필터링을_통한_개인화된_광고_서비스').text)
content_1.append(soup_1.select_one('#content > div > div.entry-content > div.contents_style > p:nth-child(11)').text)
content_1.append(soup_1.select_one(r'#\33 _AI를_활용한_효율적인_실시간_재고_관리').text)
content_1.append(soup_1.select_one('#content > div > div.entry-content > div.contents_style > p:nth-child(14)').text)
content_1.append(soup_1.select_one(r'#\34 _AI_이미지_인식_기술을_활용한_상품_이미지_검색_서비스').text)
content_1.append(soup_1.select_one('#content > div > div.entry-content > div.contents_style > p:nth-child(17)').text)
content_1.append(soup_1.select_one(r'#\35 _AI_기반_가격_예측_모델을_활용한_경쟁력_있는_상품_가격_설정').text)
content_1.append(soup_1.select_one('#content > div > div.entry-content > div.contents_style > p:nth-child(20)').text)


# Scraping2 [2020 AI대상] '추천부터 로켓배송까지' 쿠팡, 글로벌 AI기업으로 발돋움
url_2 = f'https://it.chosun.com/site/data/html_dir/2020/11/24/2020112402242.html'
html_2 = urlopen(url_2)
soup_2 = BeautifulSoup(html_2.read(), 'html.parser')
header_2 = [soup_2.select_one('#csContent > div > div.news_title > h1').text]
contents_2 = []
contents_2.append(header_2)
for i in range (1,4,2):
    contents_2.append(soup_2.select_one(f'#news_body_id > div:nth-child({i})').text)



# Scraping3 상담사 연결도 AI 활용, 쿠팡 24시간 CS 만족도 높여
driver_3 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_3.get(f'https://news.imaeil.com/page/view/2023071813214690991')
soup_3 = BeautifulSoup(driver_3.page_source, 'html.parser')
contents_3_header = soup_3.select_one(r'#container > div.inner > div.article_head > p').text
contents_3_sub_header = soup_3.select_one(r'#container > div.inner > div.section > div > div.article_view.v2 > div > p').text
contents_3 = []
contents_3.append(contents_3_header)
contents_3.append(contents_3_sub_header)
tables = soup_3.select('table.tb_store')
for i in range (4,7):
    contents_3.append(soup_3.select_one(f'#articlebody > p:nth-child({i})').text)
for i in range(8,12):
    contents_3.append(soup_3.select_one(f'#articlebody > p:nth-child({i})').text)

# Scraping4 쿠팡, 해외직구 판매자 돕는다..."상품페이지 번역 서비스 할인"
driver_4 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_4.get(f'https://newsis.com/view/?id=NISX20230725_0002389061&cID=13001&pID=13000')
soup_4 = BeautifulSoup(driver_4.page_source, 'html.parser')
contents_4 = []
contents_4_header = soup_4.select_one(f'#content > div.articleView > div.view > div.top > h1').text
contents_4.append(contents_4_header)
contents_4.append(soup_4.select_one(f'#content > div.articleView > div.view > div.viewer > article').text[99:-31])

# Scraping5 쿠팡 흑자 중심에도 AI 있었다...유통가 부는 'AI 바람'
driver_5 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_5.get(f'https://news.mt.co.kr/mtview.php?no=2023031416361832988')
soup_5 = BeautifulSoup(driver_5.page_source, 'html.parser')
contents_5_header = soup_5.select_one(r'#container > div.view_top > h1').text
contents_5 = []
contents_5.append(contents_5_header)
contents_5.append(soup_5.select_one(r'#textBody').text[11:])

# Scraping6 쿠팡, ‘로켓배송’ 비결은 AI…관련 특허 출원도 활발
driver_6 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_6.get(f'https://www.ceoscoredaily.com/page/view/2023053113404984529')
soup_6 = BeautifulSoup(driver_6.page_source, 'html.parser')
contents_6_header = soup_6.select_one(f'#container > div.inner > div.section > div.article_view.type_04 > div.article_content > h3').text
contents_6 = []
contents_6.append(contents_6_header)
for i in range(5,12,2):
    contents_6.append(soup_6.select_one(f'#container > div.inner > div.section > div.article_view.type_04 > div.article_content > p:nth-child({i})').text)
for i in range(14,25,2):
    contents_6.append(soup_6.select_one(f'#container > div.inner > div.section > div.article_view.type_04 > div.article_content > p:nth-child({i})').text)

# Scraping7 쿠팡, AI·빅데이터 자동화 물류센터 구축
driver_7 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_7.get(f'https://www.coldchainnews.kr/mobile/article.html?no=25065')
soup_7 = BeautifulSoup(driver_7.page_source, 'html.parser')
contents_7_header = soup_7.select_one('#container > div.con_primary > div > div.m_arv_001_01 > div.news_top.mov_fix > h3').text
contents_7_subheader = soup_7.select_one('#container > div.con_primary > div > div.m_arv_001_01 > div.news_top.mov_fix > h4').text
contents_7 = []
contents_7.append(contents_7_header)
contents_7.append(contents_7_subheader)
for i in range(3,8,2):
    contents_7.append(soup_7.select_one(f'#container > div.con_primary > div > div.m_arv_001_01 > div.news_detail > div > div:nth-child(2) > div:nth-child({i})').text)
contents_7.append(soup_7.select_one('#container > div.con_primary > div > div.m_arv_001_01 > div.news_detail > div > div:nth-child(2) > div:nth-child(11)').text)
for i in range(15,20,2):
    contents_7.append(soup_7.select_one(f'#container > div.con_primary > div > div.m_arv_001_01 > div.news_detail > div > div:nth-child(2) > div:nth-child({i})').text)

# Scraping8 로봇과 인공지능: 쿠팡 물류의 최신 기술을 소개합니다 
driver_8 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_8.get(f'https://news.coupang.com/archives/19485/')
soup_8 = BeautifulSoup(driver_8.page_source, 'html.parser')
contents_8_header = soup_8.select_one('#post-19485 > header > div > h1').text
contents_8 = []
contents_8.append(contents_8_header)
contents_8.append(soup_8.select_one(f'#the_content > h3:nth-child(5)').text)
for i in range(6,8):
    contents_8.append(soup_8.select_one(f'#the_content > p:nth-child({i})').text)
contents_8.append(soup_8.select_one(f'#the_content > h3:nth-child(8)').text)
for i in range(9,13):
    contents_8.append(soup_8.select_one(f'#the_content > p:nth-child({i})').text)
contents_8.append(soup_8.select_one(f'#the_content > h3:nth-child(14)').text)
for i in range(15,18):
    contents_8.append(soup_8.select_one(f'#the_content > p:nth-child({i})').text)
contents_8.append(soup_8.select_one(f'#the_content > h3:nth-child(18)').text)
for i in range(19,23):
    contents_8.append(soup_8.select_one(f'#the_content > p:nth-child({i})').text)

# Scraping9 AI 기술을 통한 물류·배송 혁신의 실현 : 로켓배송 의 모든 과정을 총괄하는 인공지능 시스템
driver_9 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_9.get(f'http://webzine.koita.or.kr/202301-specialissue/%ED%99%95%EC%9E%A5%ED%95%98%EB%8A%94-%EB%94%94%EC%A7%80%ED%84%B8-%EA%B2%BD%EC%A0%9C-%E2%80%98%EC%82%AC%EB%9E%8C%EA%B3%BC-AI%EC%9D%98-%ED%8C%80%ED%94%8C%EB%A0%88%EC%9D%B4%E2%80%99%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%BF%A0%ED%8C%A1%EC%9D%98-%ED%98%81%EC%8B%A0')
soup_9 = BeautifulSoup(driver_9.page_source, 'html.parser')
contents_9_header = soup_9.select_one('#wrap > main > div > div > div > div.read_body > div > div > xe-content > h3:nth-child(8)').text
contents_9 = []
contents_9.append(contents_9_header)
for i in range(9,11):
    contents_9.append(soup_9.select_one(f'#wrap > main > div > div > div > div.read_body > div > div > xe-content > p:nth-child({i})').text)


contents = [content_1, contents_2, contents_3, contents_4, contents_5, contents_6, contents_7, contents_8, contents_9]


file_path = 'scraping_contents.csv'
with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(contents)