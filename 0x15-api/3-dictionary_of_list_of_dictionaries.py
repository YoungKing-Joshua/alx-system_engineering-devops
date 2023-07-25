#!/usr/bin/python3
"""Script exports to-do list info of all employees to JSON format."""

import json
import requests


def export_all_to_json():
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_tasks = {}
    for user in users:
        user_id = str(user["id"])
        username = user["username"]
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        user_tasks = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            } for task in todos
        ]
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_all_to_json()
