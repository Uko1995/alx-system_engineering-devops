#!/usr/bin/python3
"""using REST API to export to json format"""

import json
import requests
from sys import argv


def export_to_json(employee_id):
    """function that exports to json format"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    employee = requests.get(user_url).json().get("name")
    tasks = requests.get(todo_url).json()
    json_file = f"{employee_id}.json"
    order = []
    for task in tasks:
        order.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee}
            )

    with open(json_file, "w") as file:
        json.dump({employee_id: order}, file)


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_json(int(argv[1]))
    else:
        print("Usage: python script.py <employee_id>")
