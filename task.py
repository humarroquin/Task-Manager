class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False


task1 = Task("Learn Python")

print(task1.title, task1.completed)