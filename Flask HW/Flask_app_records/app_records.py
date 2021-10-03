from flask import Flask, request, jsonify
from models import StudentRecords
# Server side codento receive requests

app = Flask(__name__)


@app.route("/list/insert", methods=["POST"])
def insert_item():
    new_insert = request.get_json()
    insert_new_item = StudentRecords(new_insert["name"], new_insert["age"], 
        new_insert["homeroom"], new_insert["grade"], new_insert["add_info"])
    insert_new_item.insert()
    return jsonify({"success": True})


@app.route("/list/select_all", methods=["POST"])
def select_all():
    select_new = request.get_json()
    select_new_one = StudentRecords(select_new["name"])
    select_new_one.select_all()
    return jsonify({"success": True})


@app.route("/list/delete", methods=["POST"])
def delete_item():
    delete_1 = request.get.json()
    delete_2 = StudentRecords(delete_1["name"], delete_1["age"], 
        delete_1["homeroom"], delete_1["grade"], delete_1["add_info"])
    delete_2.delete()
    delete_2.delete_item()
    return jsonify({"success": True})
