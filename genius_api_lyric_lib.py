import os
from dotenv import load_dotenv
import lyricsgenius

# Load API token from .env
load_dotenv()
GENIUS_API_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

# Initialize Genius client
genius = lyricsgenius.Genius(GENIUS_API_TOKEN, timeout=15, retries=3)

def get_lyrics(artist, title):
    print(f"🔍 Searching Genius for: {artist} – {title}")
    song = genius.search_song(title, artist)
    if song:
        print(f"🎤 Lyrics:\n\n{song.lyrics}")
        return song.lyrics
    else:
        print("❌ No results found on Genius.")
        return None

# Example usage
if __name__ == "__main__":
    artist = "Beatles"
    title = "Hey Jude"
    get_lyrics(artist, title)
