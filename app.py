from flask import Flask, render_template
import requests

from youtube_downloader import YouTubeDownloader as ytd
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert')
def convert():
    playlist_url = requests.form.get("playlist")
    playlist_id = playlist_url.split('/')[-1].split('?')[0]
    ytd.iterate_downloader(playlist_id)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
