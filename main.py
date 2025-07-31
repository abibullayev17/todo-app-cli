from utils import check_task_id
from models import ToDo

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