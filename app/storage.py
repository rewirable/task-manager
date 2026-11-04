#saving and reading to json
import json
def save(task_name):
    current_id = None
    biggest_id = 0

    try:
        with open("./tasks.json", "r") as f:
            whole = json.load(f)
            for task in whole:
                    if task["id"] > biggest_id:
                        biggest_id = task["id"]
            current_id = biggest_id + 1
    except FileNotFoundError:
        print("file doesnt exist")
        whole = []

    taskk = {
        "id": current_id,
        "name": task_name,
        "completed": False
    }
    
    try:
        whole.append(taskk)
        with open("./tasks.json", "w") as f:
            json.dump(whole, f, indent=4)

    except FileNotFoundError:
        print("file doesnt exist")


def reading(task_name):
    try:
        with open("./tasks.json", "r") as f:
            whole = json.load(f)
            for task in whole:
                if task["name"] == task_name:
                    return task
    except FileNotFoundError:
        print("file doesnt exist")
    return None


def delete(task_id: int):
    try:
        with open("./tasks.json", "r") as f:
            lines = json.load(f)
        tasks = []
        with open("./tasks.json", "w") as f:
            for task in lines:
                    if task["id"] != task_id:
                        tasks.append(task)
            json.dump(tasks, f, indent=4)
    except FileNotFoundError:
        print("file doesnt exist")
    return print("Task", task_id,"removed")

def complete(task_name):
    try:
        table = []
        with open("./tasks.json", "r") as f:
            whole = json.load(f)
            for line in whole:
                table.append(line)
                if line["name"] == task_name and line["completed"] == False:
                    line["completed"] = True
        with open("./tasks.json", "w") as f:
            json.dump(table, f, indent=4)
    except FileNotFoundError:
        print("file doesnt exist")
    return print("Task ", task_name, "completed!")