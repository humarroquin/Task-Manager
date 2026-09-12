# Task Manager

A command-line task manager built while learning Python. Practice project for
classes, input validation, and error handling.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Running it

```bash
uv run python main.py
```

## Features

- Add tasks
- List tasks with completion status
- Mark a task complete
- Delete a task

## Project layout

| File              | Purpose                                                |
| ----------------- | ------------------------------------------------------ |
| `main.py`         | Menu loop and dispatch                                 |
| `prompts.py`      | All user interaction — prompting, validation, messages |
| `task.py`         | The `Task` object                                      |
| `task_manager.py` | Operations on the collection of tasks                  |
