from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from db import DB
from model.employee import Employee, RawEmployee
# import requests


app = FastAPI()


@app.get("/employees/list")
async def get_all_employee_by_filtering(name: str | None = None, position: str | None = None, remote: bool | None = None):
    em = DB.get_all_employees(name, position, remote)
    employees = []
    for emp in em:
        employees.append({"name": emp[0], "age": emp[1], "position": emp[2], "remote": emp[3], id: emp[4]})
    return {"message":employees}

@app.get("/employees/{id}")
async def get_employee_by_id(id: str):
    return DB.get_employee(id)

@app.post("/employees/new")
async def add_new_employee(employee: RawEmployee):
    # response = requests.post('http://127.0.0.1:9000/image', files=)
    emp: Employee = Employee(first_last_name=employee.first_last_Name, age=employee.age, position=employee.position, remote=employee.remote)
    return DB.add_employee(emp)



