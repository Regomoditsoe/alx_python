#!/usr/bin/python3

"""Return employee name and to-do list"""

import requests
import sys


def get_todo_list_of_employees(user_id):
    """ Return employee names and to do list"""
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{user_id}"
    todos_url = f"{base_url}todos?userId={user_id}"

    try:
        response_user = requests.get(user_url)
        response_user.raise_for_status()
        user_data = response_user.json()

        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()

        completed =[t["title"] for t in todos_data if t["completed"]]
        print(f"Employee {user_data.get('name', 'not found')} is done with tasks ({len(completed)}/{len(todos_data)}):")

        for a, task in enumerate(completed, 1):
            print(f"\t{task}")

    except requests.exceptions.HTTPError as e:
        print(f"An error occured: {e}")
    except KeyError:
        print("Employee not found.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <user_id>")
    else:
        try:
            user_id = int(sys.argv[1])
            get_todo_list_of_employees(user_id)
        except ValueError:
            print("User ID must be an integer")
