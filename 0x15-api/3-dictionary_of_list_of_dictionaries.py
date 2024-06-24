#!/usr/bin/python3
import json
import requests


def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    # Fetch data from the API
    users = fetch_data("https://jsonplaceholder.typicode.com/users")
    todos = fetch_data("https://jsonplaceholder.typicode.com/todos")

    # Create a dictionary to hold all tasks for all users
    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]
        user_tasks = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos if todo["userId"] == user_id
        ]
        all_tasks[user_id] = user_tasks

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    main()
