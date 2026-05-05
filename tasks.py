import sys
import json
from datetime import date
import uuid


class Task:
    def __init__(self, name,due_date, priority):
        self.id = str(uuid.uuid4())
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.created_at = str(date.today())
        self.completed = False

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'due_date': self.due_date,
            'priority': self.priority,
            'created_at': self.created_at,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data['name'], data['due_date'], data['priority'])
        task.id = data['id']
        task.name = data['name']
        task.due_date = data['due_date']
        task.priority = data['priority']
        task.created_at = data['created_at']
        task.completed = data['completed']
        return task

def main():
    command = sys.argv[1]

    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    
    tasks = [Task.from_dict(task) for task in tasks]
    if command == 'add':
        print("Adding a new task...")
        task_name = sys.argv[2]
        priority = input("Enter the priority of the task: ")
        due_date = input("Enter the due date of the task: ")
        new_task = Task(task_name, due_date, priority)
        tasks.append(new_task)
        print(f"Added: {new_task.name}")
    elif command == 'list':
        print("Listing all tasks...")
        for task in tasks:
            print(task.name + " ")
    elif command == 'done':
        print("Marking task as done...")
        task_name = sys.argv[2]
        for task in tasks:
            if task.name == task_name:
                task.completed = True
                print(f"Task '{task.name}' marked as done")
                break
        else:
            print("Task not found")
    else:
        print("Unknown command")
    

    to_write = [task.to_dict() for task in tasks]
    with open('tasks.json', 'w') as file:
        json.dump(to_write, file)




# python creates a name for the file that is run so we are checking that is the file being run is "main"
# then we call the main function
if __name__ == "__main__":
    main()