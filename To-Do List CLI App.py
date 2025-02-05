import os

# Define the file where tasks will be stored
TASKS_FILE = "tasks.txt"


def load_tasks():
    """
    Load tasks from the file and return them as a list.
    If the file does not exist, return an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]


def save_tasks(tasks):
    """
    Save the tasks to the file.
    Each task is stored on a new line.
    """
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(task):
    """
    Adds a new task to the list.
    """
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")


def view_tasks():
    """
    Displays all tasks currently in the list.
    """
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found. Your to-do list is empty.")
    else:
        print("\n📋 Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def complete_task(task_number):
    """
    Marks a task as completed by removing it from the list.
    """
    tasks = load_tasks()

    if task_number <= 0 or task_number > len(tasks):
        print("❌ Invalid task number. Please try again.")
        return

    removed_task = tasks.pop(task_number - 1)
    save_tasks(tasks)
    print(f"✅ Task completed: {removed_task}")


def delete_task(task_number):
    """
    Deletes a task from the list.
    """
    tasks = load_tasks()

    if task_number <= 0 or task_number > len(tasks):
        print("❌ Invalid task number. Please try again.")
        return

    deleted_task = tasks.pop(task_number - 1)
    save_tasks(tasks)
    print(f"🗑️ Task deleted: {deleted_task}")


def main():
    """
    Main function that runs the to-do list menu.
    """
    while True:
        print("\n📌 To-Do List Menu:")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Complete Task")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            task = input("Enter a new task: ").strip()
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_number = int(input("Enter the number of the task to complete: "))
                complete_task(task_number)
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        elif choice == "4":
            view_tasks()
            try:
                task_number = int(input("Enter the number of the task to delete: "))
                delete_task(task_number)
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
