from flask import Flask, redirect, url_for, render_template
from werkzeug.exceptions import abort

import config as config

# word cloud
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

import base64
from io import BytesIO
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config.from_object("config.Config")  # not loaded into other blueprints


# word cloud
def create_word_cloud(string):
   cloud = WordCloud(background_color = "white", max_words = 200, stopwords = set(STOPWORDS))
   cloud.generate(string)
   return cloud
   #cloud.to_file("wordCloud.png")

@app.route('/')
def home():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/rawTweets')
def rawTweets():
    columnsNames = ["col1", "col2"]
    temList = [
        ["abc", "def"],
        ["ghi", "jkl"]
    ]
    return render_template('raw_tweets.html', list_2d=temList, columnsNames=columnsNames)

@app.route('/summary')
def summary():
    dataset = open("sample_input.txt", "r").read()
    dataset = dataset.lower()
    cloud = create_word_cloud(dataset)
    plt.imshow(cloud)
    plt.axis("off")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    imgEnc = f'data:image/png;base64,{data}'

    return render_template('summary.html', summary="summary body is here", imageEncode_in=imgEnc)


if __name__ == "__main__":
    app.run()
    #app.add_url_rule('/favicon.ico',
    #             redirect_to=url_for('static', filename='favicon.ico'))

