tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice : ")

    


    if choice == "1":
        if not tasks:
            print("******************")
            print("There are no tasks currently.")
            print("******************")

        else:
            print("******************")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            print("******************")

    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        print("******************")
        print("Task added !")
        print("******************")

    elif choice == "3":
        if not tasks:
            print("******************")
            print("No tasks to delete !")
            print("******************")

        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            dele = int(input("Enter task to delete: "))
            if 1 <= dele <= len(tasks):
                rem = tasks.pop(dele -1)
                print("******************")
                print(f"Task {rem} -- Deleted!")
                print("******************")
            else:
                print("******************")
                print("Invalid Number!")
                print("******************")

    elif choice == "4":
        print("******************")
        print("Goodbye !")
        print("******************")
        break

    else:
        print("******************")
        print("Invalid Choice. Try again !")
        print("******************")