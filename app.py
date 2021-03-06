# ./python_code/api.py
from flask import Flask, render_template,request,redirect,url_for, send_from_directory # For flask implementation
# from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from auth import HOST_URI
import datetime
import smtplib

# app = Flask(__name__,
#             static_folder='client/pet_interface/build/static',
#             template_folder="client/pet_interface/build")
app = Flask(__name__)
CORS(app)
api = Api(app)

title = "Users and Results"
heading = "Users and Results"

#HOST_URI = os.environ["HOST_URI"]

client = MongoClient(HOST_URI) #host uri
db = client.K92019 #Select the database
users = db.User #Select the collection name

# @app.route("/js/<path:path>")
# def send_js(path):
#     return send_from_directory('js', path);

# @app.route("/")
# def hello():
#     return render_template("index.html")

@app.route("/")
def hello():
    return "ok"

@app.route("/add", methods=['POST'])
def action ():
    #Adding a User
    user=request.values.get("user")
    disease=request.values.get("disease")
    type=request.values.get("type")
    condition=request.values.get("condition")
    result=request.values.get("result")
    today = datetime.datetime.now()

    print("RESULT in api", result)

    users.insert_one({ "user":user, "disease":disease, "type":type, "condition":condition, "result":result, "date": today})
    return "ok"

@app.route("/email")
def update ():
    body = request.values.get("value")
    print("passed into email", body)

    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('mshei1824@gmail.com', 'yowh qvlj ixmf acne')
    conn.sendmail('mshei1824@gmail.com', 'welovedogs123456@gmail.com', 'Your dog has alerted that you are at risk of high blood pressure.')
    return "ok"

@app.route("/remove")
def remove ():
    #Deleting a Task with various references
    key=request.values.get("_id")
    users.remove({"_id":ObjectId(key)})
    return "ok"

# @app.route("/update")
# def update ():
#     id=request.values.get("_id")
#     user=users.find({"_id":ObjectId(id)})
#     return "ok"
#
# @app.route("/search", methods=['GET'])
# def search():
#     #Searching a Task with various references
#     key=request.values.get("key")
#     refer=request.values.get("refer")
#     if(key=="_id"):
#         users_l = users.find({refer:ObjectId(key)})
#     else:
#         users_l = users.find({refer:key})
#     return "ok"

if __name__ == "__main__":
     app.run(debug=True)
