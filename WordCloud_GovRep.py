#WordCloud_GovRep.py

import jieba
import wordcloud
import imageio

mask = imageio.imread("chinamap.jpg")
excludes = {}
fo = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = fo.read()
fo.close()
Is = jieba.lcut(t)
txt = " ".join(Is)
w = wordcloud.WordCloud(\
    width = 1000 , height = 800,\
    background_color = "white",\
    font_path = "msyh.ttc",\
    mask = mask
    )
w.generate(txt)
w.to_file("GovRep_WordCloud.jpg")