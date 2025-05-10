from datetime import datetime

class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def task_completed(self):
        self.completed = True

    def get_task_info(self):
        status = "Completed" if self.completed else "Not completed"
        return f"Name: {self.name}\nDescription: {self.description}\nDeadline: {self.deadline}\nStatus: {status}\n"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task {task.name} added.")

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Task {name} removed.")
                return
        print(f"Task with name {name} not found.")

    def task_completed(self, name):
        for task in self.tasks:
            if task.name == name:
                task.task_completed()
                print(f"Task {name} marked as completed.")
                return
        print(f"Task with name {name} not found.")

    def list_tasks(self):
        if not self.tasks:
            print("Task list is empty.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"Task {i}:\n{task.get_task_info()}")

if __name__ == "__main__":
    manager = TaskManager()

    task1 = Task("Do homework", "Math, page 45, exercises 3-6", "2025-05-12")
    task2 = Task("Read a book", "Read 3 chapters", "2025-05-15")

    manager.add_task(task1)
    manager.add_task(task2)

    manager.list_tasks()

    manager.task_completed("Do homework")

    manager.remove_task("Read a book")

    manager.list_tasks()
