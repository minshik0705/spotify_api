import requests
from refresh_token import refresh_access_token

# Step 1: Get a fresh access token
access_token = refresh_access_token()
print(access_token)


def get_global_top_50():
    playlist_id = "3cEYpjA9oz9GiPac4AsH4n"

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch playlist:", response.json())
        return None
    data = response.json()
    tracks = []
    for item in data['items']:
        track = item['track']
        tracks.append({
            'name': track['name'],
            'artist': ', '.join([artist['name'] for artist in track['artists']]),
            'album': track['album']['name'],
            'url': track['external_urls']['spotify']
        })
    return tracks

# Example usage
if __name__ == "__main__":
    top_50 = get_global_top_50()
    for i, track in enumerate(top_50, 1):
        print(f"{i}. {track['name']} - {track['artist']} ({track['album']})")
        print(f"   {track['url']}")
