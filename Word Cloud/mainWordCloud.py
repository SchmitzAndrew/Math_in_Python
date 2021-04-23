from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import pandas as pd

from generateListWordCloud import create_words

word_list = create_words()

text = " ".join([str(elem) for elem in word_list])


wordcloud = WordCloud(width = 800, height = 800, background_color ='white', min_font_size= 10, max_font_size= 200).generate(text)


plt.figure(figsize= (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
