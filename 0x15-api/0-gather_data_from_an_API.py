#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress using a REST API.

Usage:
    python3 todo_progress.py <employee_id>

Arguments:
    employee_id (int): The ID of the employee whose TODO list progress will be retrieved.

Example:
    python3 todo_progress.py 5

Dependencies:
    - requests (Install with `pip install requests`)

The script makes a GET request to the REST API at 'https://jsonplaceholder.typicode.com' to fetch the name of the employee
and all the tasks. It then counts the number of completed tasks for the given employee and outputs the progress information.

"""

import requests
import sys

if __name__ == "__main__":
    # REST API URL
    url = "https://jsonplaceholder.typicode.com"

    # Get the employee ID from command-line arguments
    user_id = int(sys.argv[1])

    # Retrieve the employee's name
    user_ep = "{}/users/{}".format(url, user_id)
    u_name = requests.get(user_ep).json().get("name")

    # Retrieve all tasks
    tasks_ep = "{}/todos".format(url)
    tasks = requests.get(tasks_ep).json()

    # Filter tasks for the given employee ID
    total_tasks = [user_dict for user_dict in tasks if user_dict.get("userId") == user_id]

    # Filter completed tasks
    task_c = [user_dic for user_dic in total_tasks if user_dic.get("completed")]

    # Output employee's progress information
    print("Employee {} is done with tasks ({}/{})".format(u_name, len(task_c), len(total_tasks)))

    # lists out the titles of the completed tasks
    for task in task_c:
        print("{}".format(task.get("title")))
