#!/usr/bin/python3
""" Gathers data from an API
"""
import json
import os
import requests

BASE = 'https://jsonplaceholder.typicode.com'


def getEmployeeData():
    """Saves an employees detail to json file

    Args:
        id (integer): Id of the employee
    """
    filename = 'todo_all_employees.json'
    if os.path.exists(filename):
        os.remove(filename)

    emps = requests.get(f'{BASE}/users').json()
    data = {}

    for emp in emps:
        formatted_todos = []
        todos = requests.get(f'{BASE}/todos?userId={emp.get("id")}').json()
        for todo in todos:
            formatted_todos.append(
                {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": emp.get('username')
                }
            )
        data[f'{emp.get("id")}'] = formatted_todos

    print(json.dumps(data), file=open(filename, 'a'), end='')


if __name__ == '__main__':
    getEmployeeData()
