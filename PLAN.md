# Task Manager — Learning Plan

Personal working plan. Not part of the project; add `PLAN.md` to `.gitignore`.

Legend: `[x]` done · `[~]` in progress · `[ ]` not started

---

## Done

- [x] **1. `Task.__repr__` + remove debug print**
  Objects should be able to describe themselves so you never need scaffolding prints.
  Landed as `Task(title='Learn OOP', completed=False)` — class name, both fields, `!r` on each.

- [x] **2. `list_tasks` shows numbers and status**
  A program must never ask for input it hasn't made knowable. `enumerate(start=1)`,
  1-based display converted back to a 0-based index at the boundary.

- [x] **3. Fix the complete-task flow**
  Guard clause for the empty list, `q` to cancel checked *before* `int()`, narrow `try`
  around only the line that can raise, distinct messages for "not a number" vs "no such task".

### Open follow-ups from Task 3

- [ ] Option 2 (list tasks) has inverted logic — `not tasks` means *empty*, so the branches
  need swapping. Verify by running it with tasks in the list.
- [ ] `choice = int(choice) - 1` rebinds a string name to an integer index. Use a second
  name (`index`). One name, one meaning.
- [ ] Options 2 and 3 print different sentences for the same empty state, and
  "There are not tasks to display." has a grammar slip. Resolved properly in Task 6.

---

## Next up

### [ ] 4. Wire up `delete_task` and guard its bounds

**Why.** Two separate problems. `delete_task` exists but no menu option reaches it — that's
dead code, and dead code lies: any reader assumes what's present is used, so it costs
attention forever. And `del self.tasks[99]` raises `IndexError`, while `del self.tasks[-1]`
silently deletes the *last* task, which is worse than crashing because it looks like success.

**The real question:** where does the bounds check belong — inside `TaskManager`, or in the
calling code? `TaskManager` doesn't know who's calling it. Today it's your CLI, which
validates. Tomorrow it might be a web handler that doesn't. Either `TaskManager` defends
itself and raises on bad input, or it's a dumb container whose callers are contractually
required to pass valid indices. Both are legitimate. What kills codebases is picking neither
and validating in scattered places — duplicated in four spots, missing in the fifth.

**Do:** add the menu option, decide your trust boundary, write down the reasoning.

### [ ] 5. Small cleanups

**Why.** `from task import Task` in `task_manager.py` is unused — imports declare a file's
dependencies, so an unused one misleads anyone deciding whether the module can be moved or
reused.

The `y`/`n` check duplicates logic: the condition is expressed positively in two `if`s and
negatively in a third. Add a `q` option later and you must remember both places; the day you
forget, you get a bug that *looks* correct. An `else` cannot drift out of sync with its `if`s.
Also learn the idiom `if answer not in ("y", "n")`.

---

## Structure

### [ ] 6. Break `main()` into small functions

**Why — this is the highest-value item in the plan.** `main()` is ~90 lines at three levels
of nesting. Nesting is where bugs hide, because reading any line means holding every enclosing
condition in your head. It's also *blocking* you: in Task 3 you couldn't write a real guard
clause because there was no function to `return` from, so you were forced into `if/else` and
an extra indent level. Bad structure stops you writing the clear version even when you know
what it looks like.

Extracting also kills the duplicated empty-state checks and inconsistent messages, because
each concern ends up with exactly one home.

**Do:** `handle_add(manager)`, `handle_complete(manager)`, `handle_delete(manager)`, so `main`
becomes a short read-choice-and-dispatch loop. Target: no function longer than ~15 lines.

### [ ] 7. Decide who owns errors — `TaskManager` or `main`

**Why.** Right now `TaskManager` either silently succeeds or crashes, and `main` does all the
validating. That works only while there is exactly one caller. Pick a rule and apply it
everywhere: either `TaskManager` raises (`ValueError`, `IndexError`, or your own exception
class) and `main` catches and prints, or `main` validates everything before calling.

The reason this matters more than it looks: presentation belongs to the CLI, not the model.
The moment `TaskManager` calls `print`, it can only ever be used by a terminal program.

**New concept:** custom exception classes and `raise`.
**Read:** https://docs.python.org/3/tutorial/errors.html §8.4–8.5

---

## Tests

### [ ] 8. Replace `test.py` with real pytest tests

**Why.** `test.py` prints things you have to eyeball — which means it only catches bugs when
you remember to look, and you're the one who already believes the code works. Three times
now a change has shipped broken because running the program by hand was tedious enough to
skip. Tests make "did I break anything?" a two-second question.

**Do:** `uv add --dev pytest`, then `test_task_manager.py` asserting that `add_task` grows the
list, `complete_task` sets `completed = True`, `delete_task` removes the right item, and that
an out-of-range index does whatever you decided in Task 7. Run with `uv run pytest`.

**New concepts:** `assert`, test discovery naming (`test_*.py`, `test_*` functions),
`pytest.raises` for asserting that something *does* fail.
**Read:** https://docs.pytest.org/en/stable/getting-started.html

---

## Persistence

### [ ] 9. JSON save and load

**Why.** Right now quitting destroys everything, which makes the program a demo rather than a
tool. This is also your first step outside pure objects into the messy outside world — where
files can be missing, half-written, or edited by someone else. That's where real bugs live.

**Do:** `to_dict()` on `Task` and a `from_dict()` classmethod, `save()`/`load()` on
`TaskManager` writing `tasks.json`. Load on start, save on quit.

**New concepts:** the `json` module, `with open(...)` context managers (they close the file
even if an exception fires mid-write), `pathlib.Path`, and `@classmethod` as an alternate
constructor.
**Read:** https://realpython.com/python-json/ · https://realpython.com/instance-class-and-static-methods-demystified/

### [ ] 10. Handle the missing or corrupt save file

**Why.** The first run has no `tasks.json`. And a hand-edited file can be invalid JSON. If
either crashes the program on startup, it isn't something another person can use. Handling
these is most of the difference between a script and a program.

**Do:** catch `FileNotFoundError` (start with an empty list — this is normal, not an error)
and `json.JSONDecodeError` (tell the user their file is unreadable rather than dumping a
traceback). Keep each `try` narrow.

---

## Polish and stretch

### [ ] 11. Type hints and a linter

**Why.** Type hints document intent in a way comments can't, because tools check them —
`def add_task(self, task: Task) -> None` says what goes in and what comes back without anyone
reading the body. Linters catch the whole class of small things (unused imports, unreachable
code, the trailing-newline rule) mechanically, so they stop consuming review attention.

This is also where formatting config moves from your personal editor settings into the repo,
where it belongs — editors can be misconfigured; a tool in CI cannot.

**Do:** annotate every function and method. `uv add --dev ruff`, then `uv run ruff check .`
and fix what it reports. Stretch: `mypy`.
**Read:** https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html · https://docs.astral.sh/ruff/

### [ ] 12. Due dates and priority

**Why.** A stretch feature that forces genuinely new problems: `datetime` isn't
JSON-serializable, so your `to_dict`/`from_dict` from Task 9 has to decide on a string format
(look up ISO 8601 and `datetime.fromisoformat`). Sorting introduces `sorted()` with a `key`
function, which is your first real taste of passing functions as values — the bridge into
functional programming, your next Boot.dev course.

**Do:** optional due date and priority on `Task`, then let the user sort or filter by them.
**New concepts:** `datetime`, `sorted(key=...)`, optional/`None`-able fields.

### [ ] 13. README and tag v1.0

**Why.** `README.md` is empty. A finished, documented project is worth more in a job hunt
than three abandoned ones — and the README is the only part a reviewer is guaranteed to read.
Writing "what I learned" also forces you to notice how much you did.

**Do:** what it is, how to install and run it, what you learned building it. Commit, then
`git tag v1.0`.

---

## After this project

An API-consuming CLI is the natural follow-on — it reuses the OOP, files and tests you'll
have, and adds network errors, real-world JSON you don't control, and third-party libraries
(`requests`). That combination is close to what junior work actually looks like.
