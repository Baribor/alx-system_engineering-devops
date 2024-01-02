#!/usr/bin/python3
""" Gathers data from an API
"""
import requests
import sys
import os

BASE = 'https://jsonplaceholder.typicode.com'


def getEmployeeData(id):
    """Saves an employee's detail to csv file

    Args:
        id (integer): Id of the employee
    """
    filename = f'{id}.csv'
    if os.path.exists(filename):
        os.remove(filename)

    emp = requests.get(f'{BASE}/users/{id}').json()
    todos = requests.get(f'{BASE}/todos?userId={id}').json()
    for todo in todos:
        print('"{}","{}","{}","{}"'.format(
            id,
            emp.get('username'),
            todo.get('completed'),
            todo.get('title')
        ), file=open(filename, 'a'))


if __name__ == '__main__':
    id = int(sys.argv[1])
    getEmployeeData(id)
