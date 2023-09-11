import pandas as pd

file_path = r'C:\Users\KDP-50\Documents\MY_PANDAS\Project\4주차\0801_김찬수\hollys_branches.csv'
df = pd.read_csv(file_path, encoding='utf-8')

local_ = input('원하는 위치(시,군)를 입력하세요: ')

find_df = df[df['위치(시,구)'] == local_]
print(find_df)