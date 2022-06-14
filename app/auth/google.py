import os
import flask
from flask import redirect
import requests_oauthlib
from flask import Blueprint
from flask import redirect, url_for
from flask import current_app as app


google_auth = Blueprint("google", __name__, url_prefix="" )

URL = app.config["URL"]

GOOGLE_CLIENT_ID = app.config["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = app.config["GOOGLE_CLIENT_SECRET"]

GOOGLE_AUTHORIZATION_BASE_URL = app.config["GOOGLE_AUTHORIZATION_BASE_URL"]
GOOGLE_TOKEN_URL = app.config["GOOGLE_TOKEN_URL"]

GOOGLE_SCOPE = app.config["GOOGLE_SCOPE"]

# This allows us to use a plain HTTP callback
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"




@google_auth.route("/google-login")
def login():
    print(url_for('google.callback'))
    google = requests_oauthlib.OAuth2Session(
        GOOGLE_CLIENT_ID, redirect_uri  = URL + url_for('google.callback'), scope=GOOGLE_SCOPE
    )
    authorization_url, _ = google.authorization_url(GOOGLE_AUTHORIZATION_BASE_URL, access_type="offline", prompt="select_account")
    print(authorization_url)

    return redirect(authorization_url)


@google_auth.route("/google-callback")
def callback():
    google = requests_oauthlib.OAuth2Session(
        GOOGLE_CLIENT_ID, scope=GOOGLE_SCOPE, redirect_uri= URL + url_for('google.callback')
    )

    google.fetch_token(
        GOOGLE_TOKEN_URL,
        client_secret=GOOGLE_CLIENT_SECRET,
        authorization_response=flask.request.url,
    )

    # Fetch a protected resource, i.e. user profile, via Graph API

    google_user_data = google.get(
        "https://www.googleapis.com/oauth2/v1/userinfo"
    ).json()

    email = google_user_data["email"]
    name = google_user_data["name"]
    picture_url = google_user_data.get("picture", {}).get("data", {}).get("url")

    return f"""
    User information: <br>
    Name: {name} <br>
    Email: {email} <br>
    Avatar <img src="{picture_url}"> <br>
    <a href="/">Home</a>
    """
