from flask import Flask, render_template, request
import spotify_collector as spot
import youtube_downloader as yout

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    playlist = request.form.get("playlist")
    
    if playlist:
        spotify_playlist = spot.SpotifyPlaylist()
        song_names = spotify_playlist.get_playlist_tracks(playlist)
        # You can now use the song names to download from YouTube or perform any other operation
        # For example: yout.download_songs(song_names)
    
    return render_template('index.html', songs=song_names)

if __name__ == '__main__':
    app.run(debug=True)
