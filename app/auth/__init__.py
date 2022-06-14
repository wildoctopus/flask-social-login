from flask import Blueprint


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return """
    Test Login :
    <ul>
        <li><a href="/fb-login">Login with Facebook</a></li>
        <li><a href="/google-login">Login with Google</a></li>
    </ul>
    """