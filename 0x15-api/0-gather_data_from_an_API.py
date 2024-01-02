#!/usr/bin/python3
""" Gathers data from an API
"""
import requests
import sys

BASE = 'https://jsonplaceholder.typicode.com'


def getEmployeeData(id):
    """Displays an employee's detail

    Args:
        id (integer): Id of the employee
    """
    emp = requests.get(f'{BASE}/users/{id}').json()
    todos = requests.get(f'{BASE}/todos?userId={id}').json()
    completed_todos = list(filter(lambda t: t['completed'], todos))
    print(
        'Employeee {} is done with tasks({}/{}):'.format(
            emp.get('name'),
            len(completed_todos),
            len(todos)
        ))
    for todo in completed_todos:
        print(f"\t {todo['title']}")


if __name__ == '__main__':
    id = int(sys.argv[1])
    getEmployeeData(id)
