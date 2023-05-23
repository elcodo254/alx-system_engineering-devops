#!/usr/bin/python3
"""Using REST api exports to-do list for employees given an id, in json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            u.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": u.get("username")
            } for todo in requests.get(url + "todos", params={
                "userId": u.get("id")}).json()] for u in users}, json_file)
