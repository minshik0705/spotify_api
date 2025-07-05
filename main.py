import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
authorization_code = "AQDj82I8Xi7WnEMtPbokrACXV2n0b6L5WNlGFnx-Nt_e55O1nwVw36l1JSgrrQ4Sk1NuU-szcA9kdgo-3L8MnmE5o8244imzmpSkHmHk06y6dzdhnKjmQxPAzs-R75MYLxkuXBbofQO4xA-wPhxhWXE49HfAYdvynPYlOTL_82q2Oo6BCSlt6UIb-pnfg2oS5duUTRIHYpLhf35hL-AdXNIoHR42njuHV4TrELTnanfj3FBZrS82n3ky"

print(client_id, client_secret, redirect_uri)

# Encode client_id and client_secret
auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

# Make POST request to exchange code for tokens
response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri
    },
    headers={
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
)

# Print results
data = response.json()
print("Access Token: ", data.get("access_token"))
print("Refresh Token: ", data.get("refresh_token"))
print("Expires In: ", data.get("expires_in"))
print("Scope: ", data.get("scope"))
