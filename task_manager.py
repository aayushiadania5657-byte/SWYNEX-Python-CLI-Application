def add_task(tasks):
    task = input("Enter your task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        new_id = max((task.get("id", 0) for task in tasks), default=0) + 1
        new_task = {
            "id": new_id,
            "title": task,
            "completed": False
        }

        tasks.append(new_task)
        print(f"Task added successfully: {task} (ID: {new_id})")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")

        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"ID: {task['id']} | {task['title']} - {status}")


def complete_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID to complete: "))

        task = None

        for item in tasks:
            if item["id"] == task_id:
                task = item
                break

        if task is None:
            print("Invalid task ID.")
            return

        if task["completed"]:
            print("Task is already completed.")
        else:
            task["completed"] = True
            print("Task marked as completed.")

    except ValueError:
        print("Please enter a valid number.")



def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID to delete: "))

        task = None

        for item in tasks:
            if item["id"] == task_id:
                task = item
                break

        if task is None:
            print("Invalid task ID.")
            return

        tasks.remove(task)

        print(f"Task deleted successfully: {task['title']}")

    except ValueError:
        print("Please enter a valid number.")


def search_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    keyword = input("Enter keyword to search: ").strip().lower()

    if keyword == "":
        print("Search keyword cannot be empty.")
        return

    found = False

    print("\nSearch Results:")

    for task in tasks:
        if keyword in task["title"].lower():
            status = "Completed" if task["completed"] else "Pending"
            print(f"ID: {task['id']} | {task['title']} - {status}")
            found = True

    if not found:
        print("No matching tasks found.")