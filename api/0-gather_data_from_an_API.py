#!/usr/bin/python3

import requests
import sys


def get_todo_list_of_employees(employee_id):
    # define url
    employee_url = "https://jsonplaceholder.typicode.com"

    # A request to get employee details
    response_employee = requests.get(f"{employee_url}/users/{employee_id}")
    employee_data = response_employee.json()
    EMPLOYEE_NAME = employee_data.get("name")

    # Make requests for the todos 
    response_todos = requests.get(f"{employee_url}/users/{employee_id}/todos")
    todos_data = response_todos.json()

    # Calculating number of done tasks
    DONE_TASKS =[todo for todo in todos_data if todo["completed"]]
        
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    


    print(f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for task in DONE_TASKS:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_todo_list_of_employees(employee_id)
