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


save("test")