#!/usr/bin/python3
"""Get info of get information using API REST FULL
Get info of get information using API REST FULL
Get info of get information using API REST FULL"""
import requests
import sys


if __name__ == "__main__":
    employee = ''
    task_complete = 0
    array_task_complete = []
    tasks = 0
    page = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    req = requests.get(page)
    employee = req.json()['name']

    page = ("https://jsonplaceholder.typicode.com/todos?userId={}".format
            (sys.argv[1]))
    req = requests.get(page)
    for task in req.json():
        tasks += 1
        if task.get('completed') is True:
            task_complete += 1
            array_task_complete.append(task.get('title'))
    print(
        f'Employee {employee} is done with tasks({task_complete}/{tasks}):')
    for task in array_task_complete:
        print(f'\t{task}')
