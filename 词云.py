import jieba.analyse
import cv2
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib.font_manager import *
import jieba
import matplotlib.pyplot as plt

with open("E:\codes\python\\text1.txt", "rb") as f:
    text = f.read()
keywords = jieba.analyse.textrank(
    text, topK=200, withWeight=False)

file = ",".join(keywords)
font = r'./font/simhei.ttf'
image = cv2.imread('E:\codes\python\ima.jpg')
wc = WordCloud(
    font_path=font,
    background_color='white',
    mask=image,
    width=720,
    height=1280,
    max_words=200,
    max_font_size=200
)

image_colors = ImageColorGenerator(image)
wc.generate(file)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('return.png')