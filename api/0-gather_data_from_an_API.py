#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """main function"""
    # Ensure there is at least one argument passed
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("The user_id should be an integer.")
        sys.exit(1)

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)

    total_questions = 0
    completed = []
    for todo in response.json():
        if todo['userId'] == user_id:
            total_questions += 1
            if todo['completed']:
                completed.append(todo['title'])

    user_response = requests.get(user_url)
    if user_response.status_code == 404:
        print("User not found.")
        sys.exit(1)
    user_name = user_response.json()['name']

    printer = ("Employee {} is done with tasks({}/{}):".format(user_name,
               len(completed), total_questions))
    print(printer)
    for q in completed:
        print("\t {}".format(q))


if __name__ == '__main__':
    main()
