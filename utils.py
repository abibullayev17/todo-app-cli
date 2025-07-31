def check_task_id(task_id):
    try:
        task_id = int(task_id)
        return True
    except ValueError:
        print("Task id must be an integer.")
        return False