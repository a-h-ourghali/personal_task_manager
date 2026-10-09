
from tasks import show_tasks

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
    task = input("Enter a task or type done: ")

    if task.lower() == "done":
        break

    if task.strip() == "":
        print("Task cannot be empty")
    else:
        tasks.append(task)
        print("Task added")

lines = []

with open("tasks.txt", "r") as file:
    for line in file:
        lines.append(line)

with open("tasks.txt", "w") as file:
    found = False

    for line in lines:
        if line.startswith(name + " / "):
            file.write(name + " / " + " / ".join(tasks) + "\n")
            found = True
        else:
            file.write(line)

    if found == False:
        file.write(name + " / " + " / ".join(tasks) + "\n")

show_tasks(tasks)