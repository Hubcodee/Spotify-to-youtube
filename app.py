from flask import Flask, render_template
import requests

from youtube_downloader import YouTubeDownloader
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert')
def convert():
    playlist = requests.form.get("playlist")
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
