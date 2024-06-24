#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

try:
    employee_id = int(sys.argv[1])
except ValueError:
    print("Employee ID must be an integer.")
    sys.exit(1)

base_url = 'https://jsonplaceholder.typicode.com'

user_url = f'{base_url}/users/{employee_id}'
user_response = requests.get(user_url)

if user_response.status_code != 200:
    print(f"User with ID {employee_id} not found.")
    sys.exit(1)

user_data = user_response.json()
employee_name = user_data.get('name')

# Fetch TODO list information
todos_url = f'{base_url}/todos?userId={employee_id}'
todos_response = requests.get(todos_url)
todos_data = todos_response.json()

total_tasks = len(todos_data)
completed_tasks = [todo for todo in todos_data if todo.get('completed')]
number_of_done_tasks = len(completed_tasks)

print(f'Employee {employee_name} is done with tasks'
      f'({number_of_done_tasks}/{total_tasks}):')
for task in completed_tasks:
    print(f"\t {task.get('title')}")
