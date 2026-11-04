from app.storage import save, reading, delete, complete

def add_task(task_name):
    save(task_name)

def delete_task(task_id):
    return delete(task_id)

def show_task(task_name):
    return print(reading(task_name))

def complete_task(task_name):
    return complete(task_name)

