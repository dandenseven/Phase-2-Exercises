import sqlite3


class StudentRecords:

    tablename = "studentrecords"
    dbpath = "..model/models/studentrecords.db"

    def __init__(self, name, age, homeroom, grade, add_info, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.homeroom = homeroom
        self.grade = grade
        self.add_info = add_info


def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename} (
                        name, age, homeroom, grade, add_info
                        ) VALUES (?,?,?,?,?); """
            values = (self.name, self.age, self.homeroom,
                        self.grade, self.add_info)
            cursor.execute(sql, values)


@classmethod
def select_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename}"""
            values = (cls.name, cls.age, cls.homeroom,
                        cls.grade, cls.add_info)
            cursor.execute(sql, values)
            return cursor.fetchall()


def delete(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f""" DELETE FROM {self.tablename} WHERE id = self.id (?);"""
            values = (self.name, self.age, self.homeroom, self.grade, self.add_info)
            cursor.execute(sql, values)


if __name__ == "__main__":
    studentrecords = StudentRecords.select_all()
    print(studentrecords)
    new_student = StudentRecords("name", 15, 109, "tenth grade", "STEM")
    new_student.insert()