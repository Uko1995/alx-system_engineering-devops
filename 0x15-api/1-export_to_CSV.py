#!/usr/bin/python3
"""using REST API to get infotmation of users"""

import csv
import requests
from sys import argv


def export_to_csv(employee_id):
    """function that exports to csv format"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    employee = requests.get(user_url).json()
    tasks = requests.get(todo_url).json()
    csv_file = f"{employee_id}.csv"
    with open(csv_file, mode="w", newline="") as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        for t in tasks:
            lines = [t.get("userId"), employee.get("username"),
                     t.get("completed"), t.get("title")]
            write.writerow(lines)


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_csv(int(argv[1]))
    else:
        print("Usage: python script.py <employee_id>")
