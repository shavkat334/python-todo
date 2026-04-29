from db import add_task, get_all_tasks


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


def handle_mark_as_comleted():
    pass


def handle_mark_as_incomleted():
    pass


def handle_delete_task():
    pass


def handle_search_task():
    pass
