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
    homepage += "<br><a href=/read>讀取Firestore資料</a><br>"
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

@app.route("/read")
def read():
   Result = ""     
cond = input("請輸入您要查詢的課程關鍵字:")

collection_ref = db.collection("111")
docs = collection_ref.get()
for doc in docs:
    dict = doc.to_dict()                
    if cond in dict["Course"]:
        print((dict["Leacture"]+"老師開的"+dict["Course"]+"課程,"+"每周"+dict["Time"]+"於"+dict["Room"]+"上課").format(doc.to_dict()))  


#if __name__ == "__main__":
 #   app.run()

