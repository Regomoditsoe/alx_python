#!/usr/bin/python3

""" A python script that returns information about employee or ID."""

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # Make requests for the todos 
    todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    try:
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        response_todos = requests.get(todos)
        response_employee.raise_for_status()

        user_data = response_employee.json()
        data_todos = response_todos.json()

        EMPLOYEE_NAME = user_data.get("name")
        TOTAL_NUMBER_OF_TASKS = len(data_todos)
        DONE_TASKS = sum(1 for task in data_todos if task["completed"])
        NUMBER_OF_DONE_TASKS = DONE_TASKS

        print(f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for task in data_todos:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error has occured: {e}")
