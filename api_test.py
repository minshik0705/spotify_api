import time
from genius_api_lyric_lib import get_lyrics as get_lyrics_lib
from genius_api import get_lyrics as get_lyrics_scraper

artist = "Beatles"
title = "Hey Jude"

print("🔍 Comparing lyricsgenius vs. scraper method:\n")

# Lyricsgenius
start = time.time()
get_lyrics_lib(artist, title)
print(f"\n📊 lyricsgenius time: {time.time() - start:.2f} seconds\n")

# Scraper
start = time.time()
get_lyrics_scraper(artist, title)
print(f"\n📊 scraper time: {time.time() - start:.2f} seconds\n")
