from task_manager import TaskManager
from prompts import get_index, handle_add

def main():
    is_active = True
    task_manager = TaskManager()
    while is_active:
        try:
            user_choice = int(input("""What do you want to do?

Add task (1)
List tasks (2)
Complete task (3)
Delete task (4)
Quit (5)

Select a number: """))

            # add task
            if user_choice == 1:
                handle_add(task_manager)

            # list task
            elif user_choice == 2:
                if task_manager.tasks:
                    task_manager.list_tasks()
                else:
                    print("There are no tasks available.")

            elif user_choice == 3:
                selection = get_index(task_manager)
                if selection is None:
                    continue
                task_manager.complete_task(selection)
                print("Task is now complete!")

            elif user_choice == 4:
                selection = get_index(task_manager)
                if selection is None:
                    continue
                task_manager.delete_task(selection)
                print("Task deleted!")

            elif user_choice == 5:
                print("Quit...")
                is_active = False

            else:
                print("Option not available,")

        except ValueError:
            print("Value must be a number.")

if __name__ == "__main__":
    main()
