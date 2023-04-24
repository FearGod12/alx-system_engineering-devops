#!/usr/bin/python3
''' using this REST API (https://jsonplaceholder.typicode.com), for a
given employee ID,returns information about his/her TODO list progress'''

import csv
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

    data = []
    for each in html:
        if each.get("completed") is True:
            task_status = "True"
        else:
            task_status = "False"
        task_title = each.get("title")
        data.append([argv[1], username, task_status, task_title])

    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
