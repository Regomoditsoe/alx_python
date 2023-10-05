#!/usr/bin/python3

import requests
import sys


def get_todo_list_of_employees(user_id):
    """ Return employee names and to do list"""
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{user_id}"
    todos_url = f"{base_url}todos?userId={user_id}"

    try:
        response_user = requests.get(user_url)
        user_data = response_user.json()
        
        response_todos = requests.get(todos_url)
        todos_data = response_todos.json()

        DONE_TASKS =[task for task in todos_data if task["completed"]]
        
        TOTAL_NUMBER_OF_TASKS = len(todos_data)
        NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
        EMPLOYEE_NAME = user_data['name']


        print(f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for task in DONE_TASKS:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
    except ValueError as ve:
        print(f"Error parsing JSON response: {ve}")

if __name__ == "__main__":
    user_id = int(input("Enter User ID: "))
    get_todo_list_of_employees(user_id)
