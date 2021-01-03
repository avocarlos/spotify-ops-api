import requests
import os

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT')

AUTH_URI = "https://accounts.spotify.com/api"
API_URI = "https://api.spotify.com/v1"

def getToken(code):
    response = requests.post(AUTH_URI + "/token", data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    })
    breakpoint()
    return response.text