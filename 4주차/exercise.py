import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

data_list = []

for i in range(1, 53):
    Url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    html = urlopen(Url)
    soup = BeautifulSoup(html.read(), 'html.parser')

    tables = soup.select('table.tb_store')
    for table in tables:
        rows = table.select('tr')
        for row in rows:
            cells = row.select('td')
            if len(cells) >= 4:  # Check if there are enough cells to extract data
                store_name = cells[1].get_text().strip()
                area = cells[0].get_text().strip()
                address = cells[3].get_text().strip()
                phone_number = cells[5].get_text().strip()
                data_list.append([store_name, area, address, phone_number])

# CSV 파일에 헤더를 먼저 추가
header = ['매장이름', '위치(시,구)', '주소', '전화번호']

file_path = 'hollys_branches.csv'
with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    # 데이터를 CSV 파일에 저장
    writer.writerows(data_list)