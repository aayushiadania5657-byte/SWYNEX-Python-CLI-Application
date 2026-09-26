from task_manager import (
    add_task,
    view_tasks,
    complete_task,
    delete_task,
    search_tasks
)


from Validator import get_menu_choice

from storage import load_tasks, save_tasks

print("========================================")
print("          SWYNEX TASK MANAGER")
print("========================================")

tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

    choice = get_menu_choice()

    if choice == "1":
        add_task(tasks)
        save_tasks(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)
        save_tasks(tasks)

    elif choice == "4":
        delete_task(tasks)
        save_tasks(tasks)

    elif choice == "5":
        search_tasks(tasks)

    elif choice == "6":
        print("Thank you for using SWYNEX Task Manager!")
        break