from datetime import datetime

def check_task_id(task_id):
    if len(task_id) < 1:
        print("Task id cannot be empty.")
        return False
    try:
        task_id = int(task_id)
        return True
    except ValueError:
        print("Task id must be an integer.")
        return False

class Task:
    def __init__(self, task_id, title, description, created_at):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.is_done = False
        self.created_at = created_at

class ToDo:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

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

def main():
    todo = ToDo()

    while True:
        print("Menu:")
        print("1. Show all tasks.")
        print("2. Add a task.")
        print("3. Mark as done.")
        print("4. Delete a task.")
        print("5. Exit the program.")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            while True:
                title = input("Enter task title: ")
                description = input("Enter task description (optional): ")

                if len(title) < 1:
                    print("Task title cannot be empty.")
                else:
                    todo.add_task(title, description)
                    break
        elif choice == "3":
            task_id = input("Enter task id: ")

            if check_task_id(task_id):
                todo.mark_done(int(task_id))
        elif choice == "4":
            task_id = input("Enter task id: ")

            if check_task_id(task_id):
                todo.remove_task(int(task_id))
        elif choice == "5":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()