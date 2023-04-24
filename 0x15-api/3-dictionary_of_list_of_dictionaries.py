#!/usr/bin/python3
'''Records all tasks from all employees'''

import json
from urllib.request import urlopen

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todo = 'https://jsonplaceholder.typicode.com/todos'

    users = []
    with urlopen(url_users) as response1:
        users = json.loads(response1.read().decode())

    with urlopen(url_todo) as response:
        todos = json.loads(response.read().decode())

    dump_data = {}
    for user in users:
        values = []
        user_id = user.get("id")
        for each in todos:
            if user_id == each.get("userId"):
                values.append({"task": each.get("title"),
                               "completed": each.get("completed"),
                               "username": user.get("username")})
        dump_data[user_id] = values

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dump_data, f)
