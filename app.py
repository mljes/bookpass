from flask import Flask
from book_grabber import main
app = Flask(__name__)

@app.route("/")
def get_password():
    return "Here is a password! " + main()