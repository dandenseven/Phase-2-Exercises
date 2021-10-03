import os
from flask_app_records import app
from models import StudentRecords

PATH = os.path.dirname(__file__)
StudentRecords.dbpath = os.path.join(PATH, "data", "studentrecords.db")

# print(StudentRecords.select_all())

if __name__ == "__main__":
    app.run()