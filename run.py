from flask import Flask, render_template
import pyautogui
import time

app = Flask(__name__)

@app.route("/")
def func():
    return "is Building"

@app.route("/deploy", methods=["POST", "GET"])
def deploy():
    time.sleep(5)
    pyautogui.keyDown('win')
    pyautogui.keyDown('r')
    time.sleep(5)
    pyautogui.keyUp("win")
    pyautogui.keyUp("r")
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write("cd Desktop")
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write("python donwload.py")
    time.sleep(5)
    pyautogui.press("enter")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)