#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == '__main__':
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    users = user_response.json()

    data_dict = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        response = requests.get("{}/{}/todos".format(user_url, user_id))
        todo_list = response.json()
        data_dict[user_id] = []
        for lists in todo_list:
            data_dict[user_id].append({
                "task": lists['title'],
                "completed": lists['completed'],
                "username": username
                })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data_dict, f)
