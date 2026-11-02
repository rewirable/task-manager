from menu import menu
from tasks import add_task, delete_task, show_task, complete_task
choice = menu()

match choice:
    case 1:
        print("Add Task")
        add_task()
    case 2:
        print("Show Tasks")
        show_task()
    case 3:
        print("Delete Task")
        delete_task()
    case 4:
        print("Complete Task")
        complete_task()
    case 5:
        print("Exiting...")
