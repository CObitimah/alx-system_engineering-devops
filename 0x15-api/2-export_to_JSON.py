#!/usr/bin/python3
import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./2-export_to_JSON.py <employee_id>")
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
employee_name = user_data.get('username')

todos_url = f'{base_url}/todos?userId={employee_id}'
todos_response = requests.get(todos_url)
todos_data = todos_response.json()

tasks = []
for todo in todos_data:
    tasks.append({
        "task": todo.get('title'),
        "completed": todo.get('completed'),
        "username": employee_name
    })

json_filename = f"{employee_id}.json"
with open(json_filename, 'w') as json_file:
    json.dump({str(employee_id): tasks}, json_file)

print(f"Data exported to {json_filename}")
