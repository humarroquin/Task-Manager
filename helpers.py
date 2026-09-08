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
