from datetime import datetime

class Task:
    def __init__(self, description):
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Done' if self.completed else 'Not Done'
        return f"[{status}] {self.description} (Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {task.description}")

    def mark_task_completed(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_as_completed()
            print(f"Task {task_number + 1} marked as completed.")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def __str__(self):
        return "\n".join([f"{i + 1}. {task}" for i, task in enumerate(self.tasks)])


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        print(todo_list)
        print("\nOptions:")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. List all tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            try:
                task_number = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
