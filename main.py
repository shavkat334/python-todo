from sys import exit

from utils import print_menu, print_error_menu
from handlers import (
    handle_add_task,
    handle_show_tasks,
    handle_show_task_detail,
    handle_mark_as_completed,
    handle_mark_as_incompleted,
    handle_delete_task,
    handle_search_task,
)


def main() -> None:
    while True:
        print_menu()

        option = input("> ")
        if option == "1":
            handle_add_task()
        elif option == "2":
            handle_show_tasks()
        elif option == "3":
            handle_show_task_detail()
        elif option == "4":
            handle_mark_as_completed()
        elif option == "5":
            handle_mark_as_incompleted()
        elif option == "6":
            handle_delete_task()
        elif option == "7":
            handle_search_task()
        elif option == "0":
            exit()
        else:
            print_error_menu()


main()