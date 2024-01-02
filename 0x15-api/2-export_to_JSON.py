#!/usr/bin/python3
""" Gathers data from an API
"""
import requests
import sys
import os
import json

BASE = 'https://jsonplaceholder.typicode.com'


def getEmployeeData(id):
    """Saves an employee's detail to json file

    Args:
        id (integer): Id of the employee
    """
    filename = f'{id}.json'
    if os.path.exists(filename):
        os.remove(filename)

    emp = requests.get(f'{BASE}/users/{id}').json()
    todos = requests.get(f'{BASE}/todos?userId={id}').json()
    formatted_todos = []
    for todo in todos:
        formatted_todos.append(
            {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": emp.get('username')
            }
        )
    data = {f'{id}': formatted_todos}
    print(json.dumps(data), file=open(filename, 'a'))


if __name__ == '__main__':
    id = int(sys.argv[1])
    getEmployeeData(id)
