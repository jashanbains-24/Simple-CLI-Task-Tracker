import json
from task import Task

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return [Task.from_dict(task) for task in json.load(file)]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    to_write = [task.to_dict() for task in tasks]
    with open('tasks.json', 'w') as file:
        json.dump(to_write, file)
