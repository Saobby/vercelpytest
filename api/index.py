from flask import *
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == "/venti":
        return send_file("venti_origin.png")
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
