import os
import flask
from flask import redirect
import requests_oauthlib
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
from flask import Blueprint
from flask import redirect, url_for
from flask import current_app as app


fb_auth = Blueprint("fb", __name__, url_prefix="" )

URL = app.config["URL"]

FB_CLIENT_ID = app.config["FB_CLIENT_ID"]
FB_CLIENT_SECRET = app.config["FB_CLIENT_SECRET"]

FB_AUTHORIZATION_BASE_URL = app.config["FB_AUTHORIZATION_BASE_URL"]
FB_TOKEN_URL = app.config["FB_TOKEN_URL"]

FB_SCOPE = app.config["FB_SCOPE"]

# This allows us to use a plain HTTP callback
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


@fb_auth.route("/fb-login")
def login():
    print(url_for('fb.callback'))
    facebook = requests_oauthlib.OAuth2Session(
        FB_CLIENT_ID, redirect_uri  = URL + url_for('fb.callback'), scope=FB_SCOPE
    )
    authorization_url, _ = facebook.authorization_url(FB_AUTHORIZATION_BASE_URL)
    print(authorization_url)

    return redirect(authorization_url)


@fb_auth.route("/fb-callback")
def callback():
    facebook = requests_oauthlib.OAuth2Session(
        FB_CLIENT_ID, scope=FB_SCOPE, redirect_uri= URL + url_for('fb.callback')
    )

    # we need to apply a fix for Facebook here
    facebook = facebook_compliance_fix(facebook)

    facebook.fetch_token(
        FB_TOKEN_URL,
        client_secret=FB_CLIENT_SECRET,
        authorization_response=flask.request.url,
    )

    # Fetch a protected resource, i.e. user profile, via Graph API

    facebook_user_data = facebook.get(
        "https://graph.facebook.com/me?fields=id,name,email,picture{url}"
    ).json()

    email = facebook_user_data["email"]
    name = facebook_user_data["name"]
    picture_url = facebook_user_data.get("picture", {}).get("data", {}).get("url")

    return f"""
    User information: <br>
    Name: {name} <br>
    Email: {email} <br>
    Avatar <img src="{picture_url}"> <br>
    <a href="/">Home</a>
    """

'''

@app.route('/facebook/')
def facebook():
   
    # Facebook Oauth Config
    FACEBOOK_CLIENT_ID = os.environ.get('FACEBOOK_CLIENT_ID')
    FACEBOOK_CLIENT_SECRET = os.environ.get('FACEBOOK_CLIENT_SECRET')
    oauth.register(
        name='facebook',
        client_id=FACEBOOK_CLIENT_ID,
        client_secret=FACEBOOK_CLIENT_SECRET,
        access_token_url='https://graph.facebook.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://www.facebook.com/dialog/oauth',
        authorize_params=None,
        api_base_url='https://graph.facebook.com/',
        client_kwargs={'scope': 'email'},
    )
    redirect_uri = url_for('facebook_auth', _external=True)
    return oauth.facebook.authorize_redirect(redirect_uri)
 
@app.route('/facebook/auth/')
def facebook_auth():
    token = oauth.facebook.authorize_access_token()
    resp = oauth.facebook.get(
        'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
    profile = resp.json()
    print("Facebook User ", profile)
    return redirect('/')

'''