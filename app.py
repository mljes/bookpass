from flask import Flask
from book_grabber import main
app = Flask(__name__)

@app.route("/passwordplease")
def get_password():
    return "Here is a password! " + main() + "\n"