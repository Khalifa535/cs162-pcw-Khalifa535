from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", task=None)


@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.form["task"]
    return render_template("home.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
