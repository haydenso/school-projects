import flask
from flask_session import Session
from datetime import datetime
import os

app = flask.Flask(__name__, template_folder=".")
app.config['SESSION_TYPE'] = 'filesystem'
# Store session data in a /cache folder
app.config['SESSION_FILE_DIR'] = os.path.join(app.root_path, "cache")
# Allow up to 1000 sessions
app.config['SESSION_FILE_THRESHOLD'] = 1000
Session(app)

@app.route("/")
def homepage():
    cookies = flask.request.cookies
    user_agent = flask.request.headers['User-Agent']
    origin = flask.request.origin
    remote = flask.request.remote_addr
    print(f"Cookies received: {cookies}")
    print(f"User agent: {user_agent}")
    print(f"Point of origin: {origin}")
    print(f"Remote address: {remote}")

    if "remember" in flask.session:
        dont_forget = flask.session['remember']
    else:
        dont_forget = ""
    return flask.render_template('index.html', data=dont_forget)

@app.route("/remember")
def remember():
    print(flask.request.values)
    if "remember" in flask.request.values:
        dont_forget = flask.request.values['remember']
        flask.session['remember'] = dont_forget
        print(f"I have been asked to remember: {dont_forget}")
    return flask.redirect("/")

if __name__ == "__main__":
    if not os.path.exists(os.path.join(app.root_path, "cache")):
        os.mkdir(os.path.join(app.root_path, "cache"))
    app.run(host="0.0.0.0", port=5000, debug=True)
