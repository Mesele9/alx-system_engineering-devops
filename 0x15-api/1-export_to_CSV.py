#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

    with open('{}.csv'.format(emp_id), 'w') as f:
        for lists in todo_list:
            f.write("{}, {}, {}, {}\n".
                    format(id, username, lists['completed'], lists['title']))
