from task import Task
from task_manager import TaskManager
# from task import Task

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
                if len(task_manager.tasks) > 0:
                    task_manager.list_tasks()
                else:
                    print("There are not tasks to display.")

            # complete task
            elif user_choice == 3:
                try:
                    while True:
                        selected_task = int(input("Which task do you want to mark as complete? ")) - 1
                        
                        if selected_task >= 0 and selected_task < len(task_manager.tasks):
                            task_manager.complete_task(selected_task)
                            print("Task completed!")
                            break
                        if len(task_manager.tasks) == 0:
                            print("Tasks are empty.")
                            break
                        print("Task doesn't exist.")

                except ValueError:
                    print("Add the task number.")
                
            elif user_choice == 4:
                print("Quit...")
                is_active = False

            else:
                print("Option not available,")

        except ValueError:
            print("Value must be a number.")

if __name__ == "__main__":
    main()
