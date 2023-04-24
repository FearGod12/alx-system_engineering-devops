#!/usr/bin/python3
'''Records all tasks from all employees'''

import json
from urllib.request import urlopen

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users'

    dump_data = {}
    users = []
    with urlopen(url_users) as response1:
        users = json.loads(response1.read().decode())

    for user in users:
        user_id = user.get("id")
        url = url_users + '/' + str(user_id) + '/todos'
        todos = []
        with urlopen(url) as response:
            todos = json.loads(response.read().decode())

        values = []
        for each in todos:
            data = {}
            data["task"] = each.get("title")
            data["completed"] = each.get("completed")
            data["username"] = each.get("username")
            values.append(data)

        dump_data[user_id] = values

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dump_data, f)
