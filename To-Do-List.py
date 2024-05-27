from datetime import datetime
from enum import Enum

class Status(Enum):
    PENDING = 'Pending'
    COMPLETED = 'Completed'

class Task:
    _id_counter = 1

    def __init__(self, description):
        self.task_id = Task._id_counter
        self.description = description
        self.status = Status.PENDING
        self.created_timestamp = datetime.now()
        Task._id_counter += 1

    def mark_completed(self):
        self.status = Status.COMPLETED

    def __str__(self):
        return (f"Task(ID: {self.task_id}, Description: {self.description}, "
                f"Status: {self.status.value}, Created: {self.created_timestamp})")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added {task}")
        return task

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

if __name__ == "__main__":
    # Create a to-do list instance
    todo_list = ToDoList()

    # Add some tasks
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Read a book")
    todo_list.add_task("Go for a run")

    # List all tasks
    print("\nAll Tasks:")
    todo_list.list_tasks()

    # Find a task by ID and mark it as completed
    task_to_complete = todo_list.find_task_by_id(2)
    if task_to_complete:
        task_to_complete.mark_completed()
        print(f"\nUpdated Task: {task_to_complete}")

    # List all tasks again to see the updated status
    print("\nAll Tasks After Update:")
    todo_list.list_tasks()

    # Remove a task by ID
    todo_list.remove_task(1)
    print("\nAll Tasks After Removal:")
    todo_list.list_tasks()
