#! /bin/python3
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/")
def index():
    meme, subreddit = get_meme()
    return render_template("meme_index.html", meme = meme, subreddit = subreddit)


app.run(host="0.0.0.0", port=80)