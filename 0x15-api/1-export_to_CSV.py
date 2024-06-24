#!/usr/bin/python3
import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-export_to_CSV.py <employee_id>")
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

csv_filename = f"{employee_id}.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for todo in todos_data:
        writer.writerow([employee_id, employee_name, todo.get('completed')
                         todo.get('title')])

print(f'Data exported to {csv_filename}')
