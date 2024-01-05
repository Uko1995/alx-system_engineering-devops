#!/usr/bin/python3
"""dictionary of dictionaries"""

import json
import requests


def export_all_to_json():
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{base_url}/users").json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        employee = user.get("username")

        tasks = requests.get(f"{base_url}/todos?userId={user_id}").json()

        user_tasks = [
            {
                "username": employee,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in tasks
        ]

        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_all_to_json()
