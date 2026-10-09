
def show_tasks(tasks):
    print("\nYour tasks:")

    if len(tasks) == 0:
        print("No tasks added.")
    else:
        number = 1

        for task in tasks:
            print(f"{number}. {task}")
            number = number + 1