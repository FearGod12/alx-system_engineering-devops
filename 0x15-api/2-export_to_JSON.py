#!/usr/bin/python3
''' using this REST API (https://jsonplaceholder.typicode.com), for a
given employee ID,returns information about his/her TODO list progress'''

import json
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users/' + argv[1]

    username = ''
    with urlopen(url_users) as response1:
        username = json.loads(response1.read().decode()).get("username")

    url = 'https://jsonplaceholder.typicode.com/users/' + argv[1] + '/todos'
    html = []
    with urlopen(url) as response:
        html = json.loads(response.read().decode())

    key = argv[1]
    values = []
    for each in html:
        data = {}
        data["task"] = each.get("title")
        if each.get("completed") is True:
            data["completed"] = "True"
        else:
            data["completed"] = "False"
        data["username"] = username
        values.append(data)

    dump_data = {key: values}
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump(dump_data, f)
