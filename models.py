import os
import json

from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, created_at, is_done=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.is_done = is_done
        self.created_at = created_at  # datetime object

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat(),  # serialize datetime
            "is_done": self.is_done,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            created_at=datetime.fromisoformat(data["created_at"]),
            is_done=data.get("is_done", False)
        )

class ToDo:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.next_id = 1
        self.filename = filename

        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    self.tasks = [
                        Task.from_dict(task_data) for task_data in json.load(f)
                    ]
                    if self.tasks:
                        self.next_id = max(task.task_id for task in self.tasks) + 1
                except json.JSONDecodeError:
                    self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks were found ❌.")
        else:
            for task in self.tasks:
                print(f"Task Id: {task.task_id}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Created at: {task.created_at}")
                print(f"Is done?: {'❌' if task.is_done == False else '✅'}")

    def add_task(self, title, description=""):
        self.tasks.append(Task(self.next_id,  title, description, created_at=datetime.now().replace(microsecond=0)))
        self.next_id += 1

    def mark_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_done = True
                print(f"Task with id: {task.task_id} was marked as done.")
                return
        print(f"Task with id: {task_id} was not found.")

    def remove_task(self, task_id):
        initial_size = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        if len(self.tasks) < initial_size:
            print(f"Task with id {task_id} was successfully deleted.")
        else:
            print(f"Task with id {task_id} wasn't found.")