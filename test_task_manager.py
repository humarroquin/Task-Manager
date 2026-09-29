import pytest

from task import Task
from task_manager import TaskManager

def test_add_task_appends_to_the_list():
    manager = TaskManager()
    manager.add_task(Task("write tests"))
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "write tests"


def test_mark_a_task_complete():
    task = Task("write tests")
    task.mark_complete()
    assert task.completed


def test_delete_removes_the_second_task():
    manager = TaskManager()
    manager.add_task(Task("first"))
    manager.add_task(Task("second"))
    manager.add_task(Task("third"))

    manager.delete_task(1)

    remaining = [task.title for task in manager.tasks]
    assert remaining == ["first", "third"]


def test_delete_removes_the_first_task():
    manager = TaskManager()
    manager.add_task(Task("first"))
    manager.add_task(Task("second"))
    manager.add_task(Task("third"))

    manager.delete_task(0)

    remaining = [task.title for task in manager.tasks]
    assert remaining == ["second", "third"]


def test_complete_empty_tasks():
    manager = TaskManager()

    with pytest.raises(IndexError):
        manager.complete_task(0)


def test_complete_outside_range_start():
    manager = TaskManager()
    manager.add_task(Task("test task"))

    with pytest.raises(IndexError):
        manager.complete_task(-1)


def test_complete_outside_range_end():
    manager = TaskManager()
    manager.add_task(Task("test task"))

    with pytest.raises(IndexError):
        manager.complete_task(1)
