from flask import Flask, render_template, request
import json

app = Flask(__name__)
todos = []

@app.route("/sort", methods=["POST", "GET"])
def func():
    todos.clear()
    bestell_numer = request.form.get("bestellungs_numer")
    with open(f"bestellung.json", "r") as file:
        json_file = json.load(file)
        todos.append(json_file)
        
    return render_template("sort_item.html", todos=todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)