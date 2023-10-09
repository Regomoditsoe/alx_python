#!/usr/bin/python3

import sys
import requests
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    try:
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        response_todos = requests.get(todos)
        response_todos.raise_for_status()

        user_data = response_employee.json()
        data_todos = response_todos.json()

        EMPLOYEE_NAME = user_data.get("username")
        user_id = user_data.get("id")

        csv_name = f"{user_id}.csv"
        
        # CSV data to name
        with open(csv_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # CSV header
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Counts initialize
            done_tasks = 0
            total_number_of_tasks = len(data_todos)

            # Tasks data
            for task in data_todos:
                task_completed_status = "Completed" if task["completed"] else "Not Completed"
                csv_writer.writerow([user_id, EMPLOYEE_NAME, task_completed_status, task["title"]])

                if task["completed"]:
                    done_tasks += 1
        print(f"First line: Employee {EMPLOYEE_NAME} is done with tasks ({done_tasks}/{total_number_of_tasks}):")
        print(f"Data exported to {csv_name} successfully.")


    except requests.exceptions.RequestException as e:
        print(f"An error has occured: {e}")
