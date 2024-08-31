import os
from pytube import YouTube
from youtube_search import YoutubeSearch

from spotify_collector import SpotifyPlaylist

# Function to download a song from YouTube
class YouTubeDownloader:
    def __init__(self):
        self.spotify_playlist_obj = SpotifyPlaylist()

    def download_song(song_name):
        try:
            # Search for the song on YouTube
            yt_search = YoutubeSearch(song_name, max_results=1)
            video_url = yt_search.results[0]['link']
            yt = YouTube(video_url)
            yt.streams.filter(only_audio=True).first().download()
            print(f"Downloaded {song_name}")
        except Exception as e:
            print(f"Error downloading {song_name}: {e}")

    def iterate_downloader(self, playlist_id):
        # Get all song names
        songnames = self.spotify_playlist_obj.get_playlist_tracks(playlist_id)
        for songname in songnames:
            self.download_song(songname)


