import requests
import sys

def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"
    try:
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()
        EMPLOYEE_NAME = employee_data["name"]

        response_todo = requests.get(todo_url)
        response_todo.raise_for_status()
        todo_data = response_todo.json()

        done_tasks = [task for task in todo_data if task["completed"]]
        NUMBER_OF_DONE_TASKS = len(done_tasks)
        TOTAL_NUMBER_OF_TASKS = len(todo_data)

        print(f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for task in done_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.HTTPError as e:
        print(f"An error occured: {e}")
    except KeyError:
        print(f"Employee not found.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
