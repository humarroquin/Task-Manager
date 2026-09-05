from task import Task
from task_manager import TaskManager

def main():
    is_active = True
    task_manager = TaskManager()
    while is_active:
        try:
            user_choice = int(input("""What do you want to do?

Add task (1)
List tasks (2)
Complete task (3)
Quit (4)

Select a number: """))

            # add task
            if user_choice == 1:
                is_adding_tasks = True
                while is_adding_tasks:
                    task = input("Write a task: ").strip()
                    if task != "":
                        task_manager.add_task(Task(task))
                        print("Task added!")
                        while True:
                            check_point = input("Add new task? Yes (Y) | No (N): ").lower()
                            if check_point == "y":
                                break
                            if check_point == "n":
                                is_adding_tasks = False
                                break
                            if check_point != "y" and check_point != "n":
                                print("Invalid option.")
                    else:
                        print("Task can't be empty.")

            # list task
            elif user_choice == 2:
                if task_manager.tasks:
                    task_manager.list_tasks()
                else:
                    print("There are no tasks available.")

            # complete task
            elif user_choice == 3:

                if not task_manager.tasks:
                    print("There are no tasks available.")

                else:
                    while True:
                        task_manager.list_tasks()
                        choice = input("Which task did you complete? Select the No. (or press 'q' to go back) ").strip().lower()
                        if choice == 'q':
                            break

                        try:
                            index = int(choice) - 1
                        except ValueError:
                            print("That's not a valid number.")
                            continue

                        if not 0 <= index < len(task_manager.tasks):
                            print("Task doesn't exist! Select from the options above.")
                            continue

                        task_manager.complete_task(index)
                        print("Task is now complete!")
                        break

            elif user_choice == 4:
                print("Quit...")
                is_active = False

            else:
                print("Option not available,")

        except ValueError:
            print("Value must be a number.")

if __name__ == "__main__":
    main()
