#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    # Get the list of all users
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        # Loop through all users and retrieve their todo list
        # Then add the data to a dictionary in JSON format
        json.dump({
            i.get("id"): [{
                "task": j.get("title"),
                "completed": j.get("completed"),
                "username": i.get("username")
            } for j in requests.get(url + "todos",
                                    params={"userId": i.get("id")}).json()]
            for i in users}, jsonfile)
