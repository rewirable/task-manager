from storage import save, reading

def add_task(task_name):
    save(task_name)

def delete_task():
    pass

def show_task(task_name):
    return print(reading(task_name))

def complete_task():
    pass

add_task("aa")