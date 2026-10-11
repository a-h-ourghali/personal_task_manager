
import os
from dotenv import load_dotenv
from tasks import show_tasks

load_dotenv()

admin_choice = input("Do you want to enter Admin Mode? (yes/no): ")

if admin_choice.lower() == "yes":
    password = input("Enter admin password: ")
    admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

    if password == admin_password and admin_password:
        print("Admin Mode enabled.")
    else:
        print("Wrong password.")
        exit()

name = input("Enter your name: ")
print("Welcome", name)
print("Welcome to Personal Task Manager!")

tasks = []

with open("tasks.txt", "a") as file:
    pass

with open("tasks.txt", "r") as file:
    for line in file:
        if line.startswith(name + " / "):
            old_tasks = line.strip().split(" / ")
            tasks = old_tasks[1:]

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ").strip()

        if task == "":
            print("Task cannot be empty.")
            continue

        priority = input(
            "Enter priority (low/medium/high): "
        ).lower().strip()

        if priority not in ["low", "medium", "high"]:
            print("Invalid priority!")
            continue

        tasks.append(task + " [Priority: " + priority + "]")
        print("Task added.")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)

        number = input("Enter task number: ")

        if number.isdigit():
            number = int(number)

            if number >= 1 and number <= len(tasks):
                if "[Done]" not in tasks[number - 1]:
                    tasks[number - 1] = "[Done] " + tasks[number - 1]
                    print("Task marked as done.")
                else:
                    print("Task is already done.")
            else:
                print("Invalid task number.")
        else:
            print("Enter a valid number.")

    elif choice == "4":
        show_tasks(tasks)

        number = input("Enter task number to delete: ")

        if number.isdigit():
            number = int(number)

            if number >= 1 and number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")
        else:
            print("Enter a valid number.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

lines = []

with open("tasks.txt", "r") as file:
    for line in file:
        if not line.startswith(name + " / "):
            lines.append(line)

with open("tasks.txt", "w") as file:
    for line in lines:
        file.write(line)

    file.write(name + " / " + " / ".join(tasks) + "\n")

show_tasks(tasks)
