#!/usr/bin/python3
"""API Module"""
import csv
import json
import requests
import sys

if __name__ == "__main__":

    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(sys.argv[1]))

    emp_username = user_info.json()["username"]

    todos_list = json.loads(data.text)

    with open('' + sys.argv[1] + '.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for key in todos_list:
            writer.writerow(
                [sys.argv[1]] +
                [emp_username] +
                [key['completed']] +
                [key['title']])
