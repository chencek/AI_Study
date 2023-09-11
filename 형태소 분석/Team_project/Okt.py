from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
text = open(r'C:\Users\KDP-50\Documents\MY_PANDAS\Project\4주차\Team_project\scraping_contents.csv', encoding='utf-8').read()
okt = Okt() 
sentences_tag = []
sentences_tag = okt.pos(text)
noun_adj_list = []
for word, tag in sentences_tag:
    if tag in ['Noun']:
        noun_adj_list.append(word)
print(noun_adj_list)
counts = Counter(noun_adj_list)
tags = counts.most_common(100)
print(tags)
path = r'c:\Windows\Fonts\malgun.ttf'

wc = WordCloud(font_path=path, background_color="white", max_font_size=60)

cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(15, 9))
plt.axis('off')
plt.imshow(cloud)
plt.show()

