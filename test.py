from task import Task
from task_manager import TaskManager

# FOR TESTING PURPOSES
task1 = Task("Learn variables")
task2 = Task("Learn functions")
task3 = Task("Learn OOP")

tasks = TaskManager()
print("\n==============\n")
tasks.add_task(task1)
tasks.add_task(task2)
tasks.add_task(task3)
tasks.list_tasks()
print("\n==============\n")
tasks.delete_task(1)
tasks.list_tasks()
print("\n==============\n")

tasks.complete_task(0)
print(task1.completed)