#!/usr/bin/python3
''' using this REST API (https://jsonplaceholder.typicode.com), for a
given employee ID,returns information about his/her TODO list progress'''

import json
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users/' + argv[1]

    name = ''
    with urlopen(url_users) as response1:
        name = json.loads(response1.read().decode()).get("name")

    url = 'https://jsonplaceholder.typicode.com/users/' + argv[1] + '/todos'
    html = []
    with urlopen(url) as response:
        html = json.loads(response.read().decode())

    number = 0
    for each in html:
        if each.get("completed") is True:
            number += 1

    print("Employee {} is done with tasks({}/{}):".format(name, number,
                                                          len(html)))
    for each in html:
        if each.get("completed") is True:
            print("\t {}".format(each.get("title")))
