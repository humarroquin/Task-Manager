from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task.title)

    def delete_task(self, index):
        del self.tasks[index]

    def complete_task(self, index):
        self.tasks[index].mark_complete()

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
