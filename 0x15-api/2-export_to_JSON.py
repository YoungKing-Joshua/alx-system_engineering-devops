#!/usr/bin/python3
"""Script exports to-do list information for an employee's ID to JSON format."""

import requests
import json
import sys

def export_to_json(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    username = user_data.get("username")
    todo_data = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in todo_data]}, jsonfile)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please provide a valid user ID as a command-line argument.")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_json(user_id)
