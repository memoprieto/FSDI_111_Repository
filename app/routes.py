from flask import Flask


app = Flask(__name__)


@app.get("/")
def index():
    me = {
        "First_name":"Guillermo",
        "Last_name":"Prieto",
        "Email":"memoprieto79@hotmail.comm",
        "active": True
    }
    return me

    