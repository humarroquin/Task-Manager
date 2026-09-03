from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"({index}) {task.title}: {task.completed}")

    def delete_task(self, index):
        del self.tasks[index]

    def complete_task(self, index):
        self.tasks[index].mark_complete()
