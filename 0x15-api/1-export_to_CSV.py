#!/usr/bin/python3
"""Script exports data into CSV format"""

import csv
import requests
import sys


def export_to_csv(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    username = user_data.get("username")
    todo_data = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            csv_writer.writerow([user_id, username,
                                task.get("completed"), task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please provide a valid user ID as a command-line argument.")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_csv(user_id)
