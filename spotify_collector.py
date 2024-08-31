import spotify_collector
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyPlaylist:
    def __init__(self):
        # Set up your Spotify credentials
        self.client_id = 'da6b139e19754cbcb15f6ce202f54746'
        self.client_secret = '3d00001e4ba14ba68c9a0c7c9af332e3'

        # Authenticate
        self.auth_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.sp = spotify_collector.Spotify(auth_manager=self.auth_manager)

    # Function to get all song names from a playlist
    def get_playlist_tracks(self, playlist_id):
        results = self.sp.playlist_tracks(playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        track_names = [track['track']['name'] for track in tracks]
        return tuple(track_names)

# Spotify playlist URL
playlist_url = 'https://open.spotify.com/playlist/3DuzHWBRJN4VMir60nB9vn'
playlist_id = playlist_url.split('/')[-1].split('?')[0]

spotify_playlist_obj = SpotifyPlaylist()
# Get all song names
song_names = spotify_playlist_obj.get_playlist_tracks(playlist_id)
print(song_names)