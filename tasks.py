import json
import os
from datetime import datetime

# Function to load tasks from file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = {"tasks": []}
    else:
        tasks = {"tasks": []}
    return tasks


# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    tasks["tasks"].append({
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    task_index = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_index < len(tasks["tasks"]):
        del tasks["tasks"][task_index]
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_completed(tasks):
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks["tasks"]):
        tasks["tasks"][task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to display tasks
def display_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks["tasks"], 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTODO LIST MENU:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
