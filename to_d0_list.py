def task():
    tasks = []
    print("Welcome to the To-Do List App")

    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"\nToday's tasks are:\n{tasks}")

    while True:
        operation = int(input("\nChoose an option:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nEnter choice: "))

        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task name: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task updated to '{up}'.")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            print("\nYour current tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

        elif operation == 5:
            print("Closing the program... Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

task()
