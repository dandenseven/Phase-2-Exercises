from flask import Flask, request, jsonify
from models.studentrecord import StudentRecords

# Server side codento receive requests

app = Flask(__name__)


@app.route("/list/insert/<name>/<age>/<homeroom>/<grade>/<add_info>", methods=["GET"])
def insert_item(name, age, homeroom, grade, add_info):
    try:
        new_insert = StudentRecords.insert(name, age, homeroom, grade, add_info)
        new_insert.insert()
    except:
        return jsonify({"success": False})
    return jsonify({"success": True})


@app.route("/list/select_all/<name>/<age>/<homeroom>/<grade>/<add_info>", methods=["GET"])
def select_all(name, age, homeroom, grade, add_info):
    item_all = StudentRecords(name, age, homeroom, grade, add_info)
    item_all.select_all()
    return jsonify({"selected": item_all})


@app.route("/list/delete/<name>/<age>/<homeroom>/<grade>/<add_info>", methods=["GET"])
def delete_item(name, age, homeroom, grade, add_info):
    delete_1 = StudentRecords(name, None, None, None,None)
    delete_1.delete()
    return jsonify({"deleted": delete_1})
