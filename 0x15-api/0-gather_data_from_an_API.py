#!/usr/bin/python3
"""Script that uses REST API for a given employee ID and
returns information about employee's TODO list progress."""


import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please provide a valid employee ID as a command-line argument.")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = int(sys.argv[1])
    user_data = requests.get(url + 'users/{}'.format(employee_id)).json()
    todo_data = requests.get(url + 'todos',
                             params={'userId': employee_id}).json()

    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):".
          format(user_data['name'], len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))
