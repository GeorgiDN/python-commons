from colorama import Fore, Back, Style, init

init(autoreset=True)


def take_input():
    return input("Enter your choice (1-4): ")


def take_task():
    return input("Enter your task: ")


def take_index_to_remove():
    return int(input("Enter which task do you want to remove: "))


def take_index_to_mark_to_complete():
    return int(input("Enter the index of the task to mark as completed: "))


def take_index_to_unmark_to_complete():
    return int(input("Enter the index of the task to unmark as completed: "))


def is_valid_index(my_list, idx):
    return 0 <= idx < len(my_list)


def is_empy_list(my_list):
    return len(my_list) == 0


def add_task(my_list, task_):
    task_names = [t["task"] for t in my_list]
    if task_ not in task_names:
        my_list.append({"task": task_, "completed": False})
        print(Fore.LIGHTGREEN_EX + f"- Task '{Fore.YELLOW + task_ + Fore.LIGHTGREEN_EX}' "
                                   f"added successfully")
    else:
        print(Back.YELLOW + Fore.BLACK + "This task is already added in the list!")
    view_all_task(my_list)
    return my_list


def mark_task_as_completed(my_list):
    view_all_task(my_list)
    if not is_empy_list(my_list):
        idx = take_index_to_mark_to_complete()
        if is_valid_index(my_list, idx - 1):
            if not my_list[idx - 1]["completed"]:
                my_list[idx - 1]["completed"] = True
                view_all_task(my_list)
                print(
                    Fore.LIGHTGREEN_EX + f"- Task {Fore.YELLOW + my_list[idx - 1]['task'] + Fore.RESET + Fore.LIGHTGREEN_EX} is marked as completed.")
            else:
                print(Back.YELLOW + Fore.BLACK + f" This task is already marked as completed!")
        else:
            print(Back.YELLOW + Fore.BLACK + "Invalid index! Please enter a valid index!")
    return my_list


def unmark_task_as_completed(my_list):
    view_all_task(my_list)
    if not is_empy_list(my_list):
        idx = take_index_to_unmark_to_complete()
        if is_valid_index(my_list, idx - 1):
            if my_list[idx - 1]["completed"]:
                my_list[idx - 1]["completed"] = False
                view_all_task(my_list)
                print(
                    Fore.LIGHTGREEN_EX + f"Task {Fore.YELLOW + my_list[idx - 1]['task'] + Fore.RESET + Fore.LIGHTGREEN_EX} is unmarked as completed.")
            else:
                print(Back.YELLOW + Fore.BLACK + "This task is not marked as completed!")
        else:
            print(Back.YELLOW + Fore.BLACK + "Invalid index! Please enter a valid index!")
    return my_list


def remove_task(my_list):
    if not is_empy_list(my_list):
        view_all_task(my_list)
        idx = take_index_to_remove()
        if is_valid_index(my_list, idx - 1):
            if len(my_list) > 1:
                my_list.pop(idx)
                print(
                    Fore.LIGHTGREEN_EX + f"Task {Fore.YELLOW + my_list[idx - 1]['task'] + Fore.RESET + Fore.LIGHTGREEN_EX} is removed successfully")
            else:
                print(
                    Fore.LIGHTGREEN_EX + f"Task {Fore.YELLOW + my_list[idx - 1]['task'] + Fore.RESET + Fore.LIGHTGREEN_EX} is removed successfully")
                my_list.clear()
        else:
            print(Back.YELLOW + Fore.BLACK + f"Not valid index! ")
    view_all_task(my_list)
    return my_list


def view_all_task(my_list):
    if not is_empy_list(my_list):
        result = Fore.CYAN + "- Task in the list:\n" + Fore.RESET
        for i, t in enumerate(my_list):
            # status = "[x]" if t["completed"] else "[]"
            if t["completed"]:
                status = Fore.GREEN + "[x]" + Fore.RESET
            else:
                status = Fore.RED + "[]" + Fore.RESET
            result += f"{i + 1}. {status} {t['task']}\n"

        return print(result)
    return print(Fore.CYAN + "- The list is Empty." + Fore.RESET)


def quite_program():
    print("Bye!")
    return exit()


def print_invalid_message():
    return print(
        Back.YELLOW + Fore.BLACK + "---------- Invalid choice! Please enter a number between 1 and 4! ---------")


def to_do_list_implementation():
    to_do_list = []
    while True:
        print(Fore.LIGHTBLUE_EX + "===== To-Do List Menu =====\n" + Fore.MAGENTA +
              f"1. Add a new task\n"
              f"2. Mark a task as completed\n"
              f"3. Unmark a task as completed\n"
              f"4. View all tasks\n"
              f"5. Remove task\n"
              f"6. Quit")
        print(Fore.RED + "__________________________________________________________________________")

        choice = take_input()

        if choice == "1":
            task = take_task()
            add_task(to_do_list, task)

        elif choice == "2":
            mark_task_as_completed(to_do_list)

        elif choice == "3":
            unmark_task_as_completed(to_do_list)

        elif choice == "4":
            view_all_task(to_do_list)

        elif choice == "5":
            remove_task(to_do_list)

        elif choice == "6":
            quite_program()

        else:
            print_invalid_message()


to_do_list_implementation()
