from flask import *
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/')
def catch_all(path):
#     if path == "/venti":
#         return send_file("venti_origin.png")
    return "Hello World"

@app.route('/venti')
def test():
    return send_file("venti_origin.png")

