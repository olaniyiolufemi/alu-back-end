import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Fetch user information
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Fetch TODO list information
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Extract required information
        employee_name = user_data['name']
        total_tasks = len(todos_data)
        completed_tasks = [todo for todo in todos_data if todo['completed']]
        number_of_done_tasks = len(completed_tasks)

        # Output the employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as the employee ID.")
