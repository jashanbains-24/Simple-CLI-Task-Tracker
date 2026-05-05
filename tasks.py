import sys
import json

tasks = []

def main():
    command = sys.argv[1]

    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    

    if command == 'add':
        print("Adding a new task...")
        task = sys.argv[2]
        tasks.append(task)
        print(f"Added: {task}")
    elif command == 'list':
        print("Listing all tasks...")
        for task in tasks:
            print(task + " ")
    elif command == 'done':
        print("Marking task as done...")
        task = sys.argv[2]
        tasks.remove(task)
        print(f"Task '{task}' marked as done")
    else:
        print("Unknown command")
    

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)




# python creates a name for the file that is run so we are checking that is the file being run is "main"
# then we call the main function
if __name__ == "__main__":
    main()