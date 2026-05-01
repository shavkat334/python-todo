from db import add_task, get_all_tasks, write_file


def handle_add_task():
    print("--Add New Task--")
    title = input("Title: ")
    description = input("Description: ")

    add_task(title, description)

    print("Task has been added successfully.")


def handle_show_tasks():
    tasks = get_all_tasks()
    for task in tasks:
        print(task["id"], task["title"])


def handle_show_task_detail():
    id = int(input("task id: "))
    tasks = get_all_tasks()
    for task in tasks:
        if task["id"] == id:
            print(task["id"], task["title"], task["description"])


def handle_mark_as_completed():
    id = int(input("task id: "))
    tasks = get_all_tasks()
    for task in tasks:
        if task["id"] == id:
            task["status"] = True
    write_file(tasks)



def handle_mark_as_incompleted():
    id = int(input("task id: "))
    tasks = get_all_tasks()
    for task in tasks:
        if task["id"] == id:
            task["status"] = False
    write_file(tasks)


def handle_delete_task():
    id = int(input("task id: "))
    tasks = get_all_tasks()
    tasks = [task for task in tasks if task["id"] != id]
    write_file(tasks)
    print("Task has been deleted successfully.")


def handle_search_task():
    query = input("Search: ")
    tasks = get_all_tasks()
    found = False
    for task in tasks:
        if query.lower() in task["title"].lower() or query.lower() in task["description"].lower():
            print(task["id"], task["title"], task["description"])
            found = True
    if not found:
        print("No tasks found.")
        
