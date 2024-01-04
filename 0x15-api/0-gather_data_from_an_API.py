#!/usr/bin/python3
"""using REST API to get infotmation of users"""

import requests
from sys import argv


def todo(employee_id):
    """function that gets the work info of users"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    employee = requests.get(user_url).json().get("name")
    tasks = requests.get(todo_url).json()
    total_tasks = len(tasks)
    completed = [task for task in tasks if task.get("completed")]
    completed_tasks = len(completed)

    print(f"Employee {employee} is done with\
tasks({completed_tasks}/{total_tasks}):")
    for t in completed:
        print(f"\t{t.get('title')}")


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))
    else:
        print("Usage: python script.py <employee_id>")
