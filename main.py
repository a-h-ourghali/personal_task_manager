
name = input("Enter your name: ")

print(f"Welcome, {name}!")
print("Welcome to Personal Task Manager!")

tasks = []

while True:
    task = input("Enter a task (or type 'done' to finish): ")

    if task.lower() == "done":
        break

    if task.strip() == "":
        print("Task cannot be empty!")
        continue

    tasks.append(task)
    print("Task added successfully!")


print("\nYour tasks:")

if len(tasks) == 0:
    print("No tasks added.")
else:
    number = 1

    for task in tasks:
        print(f"{number}. {task}")
        number = number + 1