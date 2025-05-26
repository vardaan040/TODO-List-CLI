import sys

todo_list = []

def show_menu():
    print("\nTODO List CLI")
    print("1. View TODO List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour TODO list is empty.")
    else:
        print("\nTODO List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task to add: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def remove_task():
    view_todo_list()
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def clear_tasks():
    confirm = input("\nAre you sure you want to clear all tasks? (yes/no): ").strip().lower()
    if confirm == 'yes':
        todo_list.clear()
        print("All tasks cleared.")
    else:
        print("Clear operation canceled.")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_todo_list()
            elif choice == 2:
                add_task()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                clear_tasks()
            elif choice == 5:
                print("Exiting TODO List CLI. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()