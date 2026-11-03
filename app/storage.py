#saving and reading to json
import json
def save(task_name):
    task = {
        "id": 1,
        "name": task_name,
        "completed": False
    }
    with open("./tasks.json", "w") as f:
        json.dump([task], f, indent=5)

def reading(task_name):
    with open("./tasks.json", "r") as f:
        whole = json.load(f)
        for task in whole:
            if task["name"] == task_name:
                return task
    return None

save("BRUDAS")
reading("BRUDAS")
