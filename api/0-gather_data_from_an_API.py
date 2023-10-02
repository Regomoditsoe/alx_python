#!/usr/bin/python3

"""Return employee name and to-do list"""

import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)


    employee_id = sys.argv[1]

    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    try:
        response_user = requests.get(user_url)
        response_user.raise_for_status()
        user_data = response_user.json()

        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()

        completed =[t["title"] for t in todos_data if t["completed"]]
        print(f"Employee {user_data['name']} is done with tasks ({len(completed)}/{len(todos_data)}):")

        for task in completed:
            print(f"\t{task}")

    except requests.exceptions.HTTPError as e:
        print(f"An error occured: {e}")
    except KeyError:
        print("Employee not found.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
