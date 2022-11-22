import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>張佳慧的網頁</h1>"
    homepage += "<a href=/all>請點此進入</a><br>"
    homepage += "<br><a href=/course>選修課程內容</a><br>"
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

@app.route("/course", methods=["GET", "POST"])
def course():
    if request.method == "POST":
        cond = request.form["leac"]
        cond1 = request.form["teac"]
        result = "您的關鍵字的課程為：" + cond
        result = "您的關鍵字的課程為：" + cond1

        db = firestore.client()
        collection_ref = db.collection("111")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if cond in dict["Course"] and cond1 in dict["Leacture"]:
                #print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
                result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
                result += dict["Time"] + "於" + dict["Room"] + "上課<br>"

        if result == "":
            result = "抱歉，查無相關條件的選修課程"
        return result
    else:
        return render_template("course.html")


@app.route("/movie", methods=["GET", "POST"])
def movie():
    if request.method == "POST":
        cond3 = request.form["keyword"]
        result = "片名：" + cond3

        db = firestore.client()
        collection_ref = db.collection("佳慧電影")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if cond3 in dict["rate"]:
                result += "片名:" + dict["title"] +dict["hyperlink"] "<br>"
                result += "電影分級:" + dict["rate"] + "<br>"

        if result == "":
            result = "抱歉，查無相關條件"
        return result
    else:
        return render_template("movie.html")


#if __name__ == "__main__":
 #   app.run()

