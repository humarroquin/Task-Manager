from task import Task

def get_index(manager):
    if not manager.tasks:
        print("Task list is empty.")
        return None

    while True:
        manager.list_tasks()
        choice = input("Which task? Select the No. (or press 'q' to go back) ").strip().lower()
        if choice == 'q':
            return None

        try:
            index = int(choice) - 1
        except ValueError:
            print("That's not a valid number.")
            continue

        if not 0 <= index < len(manager.tasks):
            print("Task doesn't exist! Select from the options above.")
            continue

        return index

def add_task(manager):
    while True:
        task = input("Write a task: ").strip()
        if task:
            manager.add_task(Task(task))
            print("Task added!")
            while True:
                check_point = input("Add new task? Yes (Y) | No (N): ").strip().lower()
                if check_point == "y":
                    break
                elif check_point == "n":
                    return
                else:
                    print("Invalid option.")
        else:
            print("Task can't be empty.")
