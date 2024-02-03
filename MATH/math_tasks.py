from random import randint
correct = 0
quit_condition = False
tasks_is_over = False
right_format = False
message = 'Welcome!\nIf you want to start write Y.If you want to quit write N.'
number_task = ''
task_kind = ''
print(message)
first_inp = input()

while True:
    if right_format:
        break
    if first_inp == "Y" or first_inp == 'y':
        while True:
            try:
                number_task = int(input('Please enter how many task do you want: '))
                right_format = True
                break
            except ValueError:
                print("OOPS you have to write integer!")

    elif first_inp == "N" or first_inp == 'n':
        print("Good bye!")
        quit_condition = True
        break
    else:
        print("Please write Y or N")
        first_inp = input()


if not quit_condition:
    print("If you want to quit,write one of this commands:(End; end or END).Else:")
    task_kind = input("Please enter what kind of task do you want with:\ndivision, multiplication, subtract, add: ")


while True:
    if quit_condition:
        break
    if tasks_is_over:
        break
    if task_kind == "end" or task_kind == "END" or task_kind == 'End':
        quit_condition = True
        print("Good bye!")
        break
    if task_kind == "add":
        for _ in range(number_task):
            a = randint(0, 100)
            b = randint(0, 100)
            rd = a + b
            print(a, "+", b, "=")
            r = int(input())

            if r == rd:
                correct += 1

        tasks_is_over = True

    elif task_kind == "subtract":
        for _ in range(number_task):
            a = randint(0, 100)
            b = randint(0, 100)
            rd = a - b
            print(a, "-", b, "=")
            r = int(input())

            if r == rd:
                correct += 1

        tasks_is_over = True

    elif task_kind == "multiplication":
        for _ in range(number_task):
            a = randint(0, 100)
            b = randint(0, 100)
            rd = a * b
            print(a, "*", b, "=")
            r = int(input())

            if r == rd:
                correct += 1

        tasks_is_over = True

    elif task_kind == "division":
        print("Please write your answer rounded to the second decimal point!")
        for _ in range(number_task):
            a = randint(0, 100)
            b = randint(0, 100)
            rd = a / b
            print(a, "/", b, "=")

            # print("{:.2f}".format(rd))
            r = float(input())

            if "{:.2f}".format(r) == "{:.2f}".format(rd):
                correct += 1
        tasks_is_over = True

    else:
        print(f"There is no task kind with name {task_kind}!")
        print()
        print("If you want to quit,write one of this commands:(End; end or END).Else:")
        task_kind = input("Please enter what kind of task do you want with:\ndivision, multiplication, subtract, add: ")


if not quit_condition:
    print(f"Your score is {correct}/{number_task}!")

