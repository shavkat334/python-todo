from db import add_task


def handle_add_task():
    print('--Add New Task--')
    title = input('Title: ')
    description = input('Description: ')

    add_task(title, description)
    
    print('Task has been added successfully.')


def handle_show_tasks():
    pass


def handle_show_task_detail():
    pass


def handle_mark_as_comleted():
    pass


def handle_mark_as_incomleted():
    pass


def handle_delete_task():
    pass


def handle_search_task():
    pass
