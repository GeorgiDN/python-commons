def take_input():
    return input("Enter your choice (1-4): ")


def take_task():
    return input("Enter your task: ")


def take_int_input():
    return int(input("Enter the index of the task to mark as completed: "))


def is_valid_index(lst, idx):
    return 0 <= idx < len(lst)


def add_task(lst, task_):
    lst.append({"task": task_, "completed": False})
    print(f"Task '{task_}' added successfully")
    return lst


def mark_task_as_completed(lst):
    print("===== Tasks =====")
    view_all_task(lst)
    idx = take_int_input()
    if is_valid_index(lst, idx-1):
        lst[idx-1]["completed"] = True
        view_all_task(lst)
        print("Task marked as completed.")
    else:
        print("Invalid index! Please enter a valid index!")
    return lst


def view_all_task(lst):
    result = ""
    for i, t in enumerate(lst):
        status = "[x]" if t["completed"] else "[]"
        result += f"{i + 1}. {status} {t['task']}\n"

    return print(result)


def quite_program():
    return exit()


def print_invalid_message():
    return print("Invalid choise. Please enter a number between 1 nad 4")


def to_do_list_implementation():
    to_do_list = []
    while True:
        print("===== To-Do List Menu =====\n"
              f"1. Add a new task\n"
              f"2. Mark a task as completed\n"
              f"3. View all tasks\n"
              f"4. Quit\n")
        print("___________________________________________________________")

        choice = take_input()

        if choice == "1":
            task = take_task()
            add_task(to_do_list, task)

        elif choice == "2":
            mark_task_as_completed(to_do_list)

        elif choice == "3":
            view_all_task(to_do_list)

        elif choice == "4":
            quite_program()

        else:
            print_invalid_message()


to_do_list_implementation()
