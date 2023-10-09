#!/usr/bin/python3

import sys
import requests
import csv

def get_todo_list_of_employees(employee_id):
    # Define url
    employee_url = "https://jsonplaceholder.typicode.com"

    # A request to get employee details
    response_employee = requests.get(f"{employee_url}/users/{employee_id}")
    employee_data = response_employee.json()
    username = employee_data.get("username")
    user_id = employee_data.get("id")

    # Make requests for the todos 
    response_todos = requests.get(f"{employee_url}/users/{employee_id}/todos")
    todos_data = response_todos.json()

    if not todos_data:
        print(f"No tasks found for Employee {username} (ID: {user_id}).")
        return

    # Make CSV file
    csv_name = f"{user_id}.csv"
    with open(csv_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Task for CSV file
        for task in todos_data:
            task_done = "True" if task["completed"] else "False"
            csv_writer.writerow([user_id, username, task_done, task["title"]])
    print(f"Correct number of tasks in CSV for Employee {username} (ID: {user_id}).")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_todo_list_of_employees(employee_id)
