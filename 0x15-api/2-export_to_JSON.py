#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == '__main__':
    emp_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get("{}/{}".format(user_url, emp_id))
    user = user_response.json()
    id = user['id']
    username = user['username']
    response = requests.get("{}/{}/todos".format(user_url, emp_id))
    todo_list = response.json()

    data_dict = {id: []}
    for lists in todo_list:
        data_dict[id].append({
            "task": lists['title'],
            "completed": lists['completed'],
            "username": username
            })
    with open('{}.json'.format(id), 'w') as f:
        json.dump(data_dict, f)
