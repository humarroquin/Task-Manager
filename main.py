from task_manager import TaskManager
from prompts import handle_add, handle_list, handle_complete, handle_delete

def main():
    is_active = True
    task_manager = TaskManager()

    while is_active:
        print("""
=== Task Manager ===

1. Add task
2. List tasks
3. Complete task
4. Delete task
5. Quit
""")
        try:
            user_choice = int(input("Choose an option: "))
        except ValueError:
            print("Value must be a number.")
            continue

        if user_choice == 1:
            handle_add(task_manager)

        elif user_choice == 2:
            handle_list(task_manager)

        elif user_choice == 3:
            handle_complete(task_manager)

        elif user_choice == 4:
            handle_delete(task_manager)

        elif user_choice == 5:
            print("Quit...")
            is_active = False

        else:
            print("Option not available,")


if __name__ == "__main__":
    main()
