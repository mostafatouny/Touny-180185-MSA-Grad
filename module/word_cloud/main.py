import matplotlib.pyplot as pPlot
from wordcloud import WordCloud
import numpy as npy
from PIL import Image

import base64
from io import BytesIO
import matplotlib.pyplot as plt

def createWordCloudImgEnc(termsWeights_in):
    termsWeights = termsWeights_in

    cloud = WordCloud(background_color = "white", max_words = 200) #width, height

    cloud.fit_words(termsWeights)

    plt.imshow(cloud)
    plt.axis("off")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    imgEnc = f'data:image/png;base64,{data}'

    return imgEnc
