#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':
    emp_id = sys.argv[1]
    user_url= "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get("{}/{}".format(user_url, emp_id))
    user = user_response.json()
    emp_name = user['name']
    response = requests.get("{}/{}/todos".format(user_url, emp_id))
    todo_list = response.json()
    no_tasks = len(todo_list)
    completed_task = 0
    completed_lists = []
    for task in todo_list:
        if task["completed"]:
            completed_task += 1
            completed_lists.append(task)

    print("Employee {} is done with tasks({}/{}):".
          format(emp_name, completed_task, no_tasks))

    for lists in completed_lists:
        print("\t{}".format(lists["title"]))
