class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        return f"Task(title={self.title!r}, completed={self.completed!r})"
