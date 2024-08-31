import os
from pytube import YouTube
from youtube_search import YoutubeSearch

# Function to download a song from YouTube
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

# Get the song names from the Spotify playlist
song_names = get_playlist_tracks(playlist_id)

# Download each song
for song_name in song_names:
    download_song(song_name)