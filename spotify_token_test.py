import os
import base64
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
refresh_token = os.getenv("SPOTIFY_REFRESH_TOKEN")

def refresh_access_token():
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        },
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )

    if response.status_code != 200:
        print("❌ Failed to refresh token:", response.status_code, response.json())
        return None

    access_token = response.json().get("access_token")
    print("✅ Access token refreshed successfully!")
    return access_token

def test_token(token):
    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("✅ Token works! User info:", response.json()["display_name"])
    else:
        print("❌ Token failed:", response.status_code, response.json())

if __name__ == "__main__":
    token = refresh_access_token()
    if token:
        test_token(token)
