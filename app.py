from flask import Flask, render_template, make_response
from sys import argv, stderr

app = Flask(__name__, template_folder="templates", static_folder="static")

# -----------------------------------------------------------------------


@app.route('/')
@app.route('/login')
def login():
    html = render_template("login.html")
    return make_response(html)

# -----------------------------------------------------------------------


@app.route('/index')
def index():
    html = render_template("index.html")
    return make_response(html)

# -----------------------------------------------------------------------


if __name__ == '__main__':

    if len(argv) != 2:
        print("Usage: " + argv[0] + " [port]", file=stderr)
        exit(1)

    try:
        ret = int(argv[1])
    except:
        print("Port must be an integer", file=stderr)
        exit(1)

    app.run(host="0.0.0.0", port=int(argv[1]))

# -----------------------------------------------------------------------
