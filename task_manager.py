class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def formatted_tasks(self):
        list_of_tasks = []
        for index, task in enumerate(self.tasks, start=1):
            list_of_tasks.append(f"{index}. {task.title}: {'[x]' if task.completed else '[ ]'}")
        return list_of_tasks

    def delete_task(self, index):
        if not 0 <= index < len(self.tasks):
            raise IndexError(f"No task at index {index}")
        del self.tasks[index]

    def complete_task(self, index):
        if not 0 <= index < len(self.tasks):
            raise IndexError(f"No task at index {index}")
        self.tasks[index].mark_complete()
