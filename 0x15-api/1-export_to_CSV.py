#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV form."""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command line argument
    user_id = sys.argv[1]

    # Set up the base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the user data and to-do list for the given ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write the to-do list data to a CSV file named after the user ID
    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write each to-do item to a row in the CSV file
        for todo in todos:
            # Extract the necessary data from the to-do item
            row = [user_id, username, todo.get("completed"), todo.get("title")]
            writer.writerow(row)
