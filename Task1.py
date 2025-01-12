#A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists

import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low, Medium, High): ")
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending"
    })
    print("Task added successfully!")


def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Due: {task['due_date']}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
