from task import Task
from task_manager import TaskManager


def test_add_task_appends_to_the_list():
    manager = TaskManager()
    manager.add_task(Task("write tests"))
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "write tests"


def test_mark_complete():
    task = Task("write tests")
    task.mark_complete()
    assert task.completed
