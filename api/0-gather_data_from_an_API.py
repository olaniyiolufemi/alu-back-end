#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys

def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        return

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("User ID must be an integer.")
        return

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Failed to fetch todos.")
        return

    total_questions = 0
    completed = []
    for todo in response.json():
        if todo['userId'] == user_id:
            total_questions += 1
            if todo['completed']:
                completed.append(todo['title'])

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Failed to fetch user details.")
        return

    user_name = user_response.json().get('name', 'Unknown')

    print("Employee {} is done with tasks({}/{}):".format(user_name, len(completed), total_questions))
    for task in completed:
        print("\t {}".format(task))

if __name__ == '__main__':
    main()
