from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
#================================================================================================
# Scraping10 매출 변화
driver_10 = selenium.webdriver.Chrome(r"C:\Users\KDP-50\Desktop\C.D\chromedriver")
driver_10.get(f'https://www.google.com/search?q=%EC%BF%A0%ED%8C%A1+%EB%A7%A4%EC%B6%9C&sxsrf=AB5stBjgl8KIyEli74V1oJWpen69SzT2oQ%3A1691063691001&ei=ipXLZNLHPLvt2roP0qyJgAw&ved=0ahUKEwjStOCUt8CAAxW7tlYBHVJWAsAQ4dUDCBA&uact=5&oq=%EC%BF%A0%ED%8C%A1+%EB%A7%A4%EC%B6%9C&gs_lp=Egxnd3Mtd2l6LXNlcnAiDey_oO2MoSDrp6TstpwyBBAjGCcyBxAjGIoFGCcyBxAjGIoFGCcyBxAAGIoFGEMyBRAAGIAEMgUQABiABDIHEAAYigUYQzIFEAAYgAQyBRAAGIAEMgUQABiABEjJEVDQCFjcEHADeACQAQGYAdcBoAG_CqoBBTAuNS4yuAEDyAEA-AEBwgIHECMYsAMYJ8ICChAAGEcY1gQYsAPCAgsQABiABBixAxiDAeIDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp')
soup_10 = BeautifulSoup(driver_10.page_source, 'html.parser')
# 분기
profit_date_3_2022_2 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(1) > g-tabs > div > div > a:nth-child(5) > div.SVWlSe.t35a5d > div > div').text[:-1]
profit_date_3_2022_3 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(1) > g-tabs > div > div > a:nth-child(4) > div.SVWlSe.t35a5d > div > div').text[:-1]
profit_date_3_2022_4 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(1) > g-tabs > div > div > a:nth-child(3) > div.SVWlSe.t35a5d > div > div').text[:-1]
profit_date_3_2023_1 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(1) > g-tabs > div > div > a:nth-child(2) > div.SVWlSe.t35a5d > div > div').text[:-1]
profit_date_list = [profit_date_3_2022_2, profit_date_3_2022_3, profit_date_3_2022_4, profit_date_3_2023_1]
# 순 이익 (단위 : 억)
profit_3_2022_2 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(4) > g-card-section > table > tbody > tr:nth-child(1) > td:nth-child(2)').text[:-1]
profit_3_2022_3 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(3) > g-card-section > table > tbody > tr:nth-child(1) > td:nth-child(2)').text[:-1]
profit_3_2022_4 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(2) > g-card-section > table > tbody > tr:nth-child(1) > td:nth-child(2)').text[:-1]
profit_3_2023_1 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(1) > g-card-section > table > tbody > tr:nth-child(1) > td:nth-child(2)').text[:-1]
profit_list = [profit_3_2022_2, profit_3_2022_3, profit_3_2022_4, profit_3_2023_1]
# 전년대비 수익 증가율 (단위 : %)
profit_per_3_2022_2 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(4) > g-card-section > table > tbody > tr:nth-child(1) > td.WlRRw.Mk9Auc.ckQqBf > span > span > span:nth-child(1)').text[:-1]
profit_per_3_2022_3 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(3) > g-card-section > table > tbody > tr:nth-child(1) > td.WlRRw.Mk9Auc.ckQqBf > span > span > span:nth-child(1)').text[:-1]
profit_per_3_2022_4 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(2) > g-card-section > table > tbody > tr:nth-child(1) > td.WlRRw.Mk9Auc.ckQqBf > span > span > span:nth-child(1)').text[:-1]
profit_per_3_2023_1 = soup_10.select_one('#kp-wp-tab-FinanceFinancials > div.TzHB6b.cLjAic.LMRCfc > div > div > div:nth-child(2) > div.B03h3d.V14nKc.OYXDld.EN1f2d.ptcLIOszQJu__wholepage-card.wp-ms > div.UDZeY > div.wDYxhc > div > div:nth-child(2) > div:nth-child(1) > g-card-section > table > tbody > tr:nth-child(1) > td.WlRRw.Mk9Auc.ckQqBf > span > span > span:nth-child(1)').text[:-1]
profit_per_list = [profit_per_3_2022_2, profit_per_3_2022_3, profit_per_3_2022_4, profit_per_3_2023_1]
# 총 수익 DataFrame
profit_change = [profit_list, profit_per_list]
df = pd.DataFrame(profit_change, columns=profit_date_list, index = ['분기별 매출(단위 : 억)','분기별 성장률(단위 : %)']).T
df["분기별 매출(단위 : 억)"] = df["분기별 매출(단위 : 억)"].astype("float")
df["분기별 성장률(단위 : %)"] = df['분기별 성장률(단위 : %)'].astype("float")

print(df)


font_path = r'c:\Windows\Fonts\malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
# plt.style.use('ggplot')

fig, ax1 = plt.subplots(figsize=(20, 10))

ax1.bar([x for x in range(len(df.index.to_list()))], df['분기별 매출(단위 : 억)'].to_list(), width=0.7, label='매출(단위: 억)')
ax1.set_ylim(40, 60)
ax1.set_xticks([x for x in range(len(df.index.to_list()))])
ax1.set_xticklabels(df.index.to_list())
ax1.set_xlabel('분기', size=20)
ax1.set_ylabel('매출(단위: 억)')

ax2 = ax1.twinx()
ax2.plot([x for x in range(len(df.index.to_list()))], df['분기별 성장률(단위 : %)'].to_list(), color='red',  ls='-', marker='o', markersize=20,label='성장률(단위 : %)')
ax2.set_ylim(0, 20)
ax2.set_xticks([x for x in range(len(df.index.to_list()))])
ax2.set_xticklabels(df.index.to_list())

ax2.set_ylabel('성장률(단위 : %)')
plt.title('쿠팡 분기별 매출 및 성장률', size=30)
plt.show()
#=================================================================================================