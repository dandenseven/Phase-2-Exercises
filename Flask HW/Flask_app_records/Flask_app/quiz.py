from flask import Flask, request, jsonify
from models.studentrecord import StudentRecords

# Server side codento receive requests

app = Flask(__name__)


@app.route("/list/insert/<name>/<age>/<homeroom>/<grade>/<add_info>", methods=["GET"])
def insert_item(name, age, homeroom, grade, add_info):
    new_insert = StudentRecords(name)
    new_insert2 = StudentRecords(name)
    set1 = set(list(new_insert))
    set2 = set(list(new_insert2))
    new_inserts = set1 & set2
    all_inserts = "".join(new_inserts)
    return jsonify({"common letters": all_inserts})


@app.route("/list/select_all", methods=["POST"])
def select_all():
    select_new_one = request.get_json()
    select_new_one = StudentRecords("select_new"["name"], "select_new"["age"],
                                    "select_new"["homeroom"], "select_new"["grade"], "select_new"["add_info"],)
    for key, value in select_new_one.items():
        return jsonify({"key": value})


@app.route("/list/select_all", methods=["POST"])
def select_all():
    select_new = request.get_json()
    select_new_one = StudentRecords(select_new["name"])
    select_new_one.select_all()
    return jsonify({"success": True})


@ app.route("/list/insert/<name>/<age>/<homeroom>/<grade>/<add_info>", methods=["GET"])
def insert_item(name, age, homeroom, grade, add_info):
    try:
        new_insert = StudentRecords.insert(
            name, age, homeroom, grade, add_info)
        if name in new_insert == name.isnumeric:
        return jsonify({"success": False})
    return jsonify({"success": True})
