#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the ID from command line argument
    id = sys.argv[1]

    # API endpoint URL
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information from the API
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")

    # Get to-do list information for the user from the API
    todos = requests.get(url + "todos", params={"userId": id}).json()

    # Write the to-do list information to a JSON file
    with open("{}.json".format(id), "w") as jsonfile:
        json.dump(
            {
                id: [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": username
                    }
                    for t in todos
                ]
            },
            jsonfile,
            indent=4
        )
