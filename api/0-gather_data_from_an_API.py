#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)

    total_tasks = 0
    completed_tasks = []
    all_tasks = []
    for todo in response.json():
        if todo['userId'] == user_id:
            total_tasks += 1
            all_tasks.append(todo['title'])
            if todo['completed']:
                completed_tasks.append(todo['title'])

    user_name = requests.get(user_url).json()['name']

    print("Employee {} has completed {}/{} tasks:".format(user_name, len(completed_tasks), total_tasks))
    for task in all_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    main()