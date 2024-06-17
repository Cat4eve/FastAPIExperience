import sqlite3
from model.employee import Employee

class DB:

    connection = None
    cursor = None

    @staticmethod
    def initialize(name: str) -> None:
        DB.connection = sqlite3.connect(name)
        DB.cursor = DB.connection.cursor()

        # SQlite 3 does not have boolean type - replace with integer with 0/1 values.
        DB.cursor.execute("""CREATE TABLE IF NOT EXISTS employees (name TEXT, age INTEGER, pos TEXT, remote INTEGER, id VARCHAR(20))""")

    @staticmethod
    def add_employee(employee: Employee):
        print(employee.id)
        DB.cursor.execute(f"""INSERT INTO employees VALUES ('{employee.first_last_name}', {employee.age}, '{employee.position}', {employee.remote}, {employee.id})""")
        DB.connection.commit()

    # here I suppose that filtering needs to be done with AND notation
    @staticmethod
    def get_all_employees(name: str | None, position: str | None, remote: bool | None):
        filtering_string: list[str] = []
        if (name is not None):
            filtering_string.append(f"name = '{name}'")
        if (position is not None):
            filtering_string.append(f"pos = '{position}'")
        if (remote is not None):
            filtering_string.append(f"remote = {1 if remote else 0}")


        DB.cursor.execute(f"""SELECT * FROM employees{' WHERE ' if len(filtering_string) > 0 else ''}{' AND '.join(filtering_string)}""")
        return DB.cursor.fetchall()
    
    @staticmethod
    def get_employee(emloyee_id: int):
        DB.cursor.execute("""SELECT * FROM employees WHERE id=?""", (emloyee_id,))
        return DB.cursor.fetchone()
    
