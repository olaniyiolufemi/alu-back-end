#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # Get user data
    user_response = requests.get(user_url)
    user_name = user_response.json()['name']

    # Get todos data
    todos_response = requests.get(todo_url)
    todos = todos_response.json()

    total_tasks = 0
    completed_tasks = []

    # Filter tasks for the given user
    for todo in todos:
        if todo['userId'] == user_id:
            total_tasks += 1
            if todo['completed']:
                completed_tasks.append(todo['title'])

    # Print the result
    print("Employee {} is done with tasks({}/{}):".format(user_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    main()
