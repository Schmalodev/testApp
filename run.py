from flask import Flask, render_template
import pyautogui
import time

app = Flask(__name__)

@app.route("/sort", methods=["POST", "GET"])
def func():
    return render_template("sort_item.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)