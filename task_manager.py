# task_manager.py - Simple Task Manager CLI

tasks = []  # List to hold tasks

def add_task(task_name):
    tasks.append(task_name)
    print(f"Task added: '{task_name}'")

def show_tasks():
    pass  # Agha Mujeeb will implement show-task here

def delete_task(index):
    pass  # Abdul Raahim will implement delete-task here

if __name__ == "__main__":
    print("Welcome to Task Manager CLI")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Please enter a number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")