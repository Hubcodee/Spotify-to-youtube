import spotify_collector
from spotipy.oauth2 import SpotifyClientCredentials

# Set up your Spotify credentials
client_id = 'da6b139e19754cbcb15f6ce202f54746'
client_secret = '3d00001e4ba14ba68c9a0c7c9af332e3'

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotify_collector.Spotify(auth_manager=auth_manager)

# Function to get all song names from a playlist
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    track_names = [track['track']['name'] for track in tracks]
    return tuple(track_names)

# Spotify playlist URL
playlist_url = 'https://open.spotify.com/playlist/3DuzHWBRJN4VMir60nB9vn'
playlist_id = playlist_url.split('/')[-1].split('?')[0]

# Get all song names
song_names = get_playlist_tracks(playlist_id)
print(song_names)