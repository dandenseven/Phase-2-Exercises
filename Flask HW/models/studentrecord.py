import sqlite3


class StudentRecords:

    tablename = "studentrecords"
    dbpath = "../studentrecords.db"

    def __init__(self, name, age, homeroom, grade, add_info):
        self.name = name
        self.age = age
        self.homeroom = homeroom
        self.grade = grade
        self.add_info = add_info


def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            student_insert = """INSERT {self.tablename} SET name = ?, age = ?, homeroom = ?,
                grade = ?, add_info = ?; """
            values = (self.name, self.age, self.homeroom, self.grade, self.add_info)
            cursor.execute(student_insert, values)


@classmethod
def select_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            student_select_all = """SELECT * FROM {cls.tablename} WHERE name = ?, age = ?, homeroom = ?,
                grade = ?, add_info = ?; """
            values = (cls.name, cls.age, cls.homeroom, cls.grade, cls.add_info)
            cursor.execute(student_select_all, values)
            


def delete(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            delete_student = """ DELETE {self.tablename} SET name = ?, age = ?, homeroom = ?,
                grade = ?, add_info = ?; """
            values = (self.name, self.age, self.homeroom, self.grade, self.add_info)
            cursor.execute(delete_student, values)


if __name__ == "__main__":
    studentrecords = StudentRecords.select_all()
    print(studentrecords)
    new_name = StudentRecords("name", 15, 109, "tenth grade", "STEM")
    new_name.insert()