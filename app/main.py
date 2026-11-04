from app.menu import menu
from app.tasks import add_task, delete_task, show_task, complete_task
def start():
    choice = menu()

    match choice:
        case 1:
            print("Add Task")
            task_name1 = input("Enter task name: ")
            add_task(task_name1)
        case 2:
            print("Show Tasks")
            task_name2 = input("Enter task name: ")
            show_task(task_name2)
        case 3:
            print("Delete Task")
            task_id = int(input("Enter task id to remove: "))
            delete_task(task_id)
        case 4:
            print("Complete Task")
            task_name3 = input("which task to complete: ")
            complete_task(task_name3)
        case 5:
            print("Exiting...")

