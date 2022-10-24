from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>張佳慧的網頁</h1>"
    homepage += "<a href=/all>請點此進入</a><br>"
    return homepage


@app.route("/all")
def all():
    return render_template("all.html")

@app.route("/me")
def me():
    return render_template("me.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/future")
def future():
    return render_template("future.html")

#if __name__ == "__main__":
 #   app.run()

