import sys
from task import Task
from storage import load_tasks, save_tasks

def main():
    command = sys.argv[1]

    tasks = load_tasks()

    if command == 'add':
        print("Adding a new task...")
        task_name = sys.argv[2]
        priority = input("Enter the priority of the task: ")
        due_date = input("Enter the due date of the task: ")
        new_task = Task(task_name, due_date, priority)
        tasks.append(new_task)
        print(f"Added: {task_name}")
    elif command == 'list':
        print("Listing all tasks...")
        for task in tasks:
            print(task)
    elif command == 'done':
        print("Marking task as done...")
        task_name = sys.argv[2]
        for task in tasks:
            if task.name == task_name:
                task.completed = True
                print(f"Task '{task.name}' marked as done")
                tasks.remove(task)
                break
        else:
            print("Task not found")
    else:
        print("Unknown command")
    

    save_tasks(tasks)



# python creates a name for the file that is run so we are checking that is the file being run is "main"
# then we call the main function
if __name__ == "__main__":
    main()