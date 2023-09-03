class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def markasdone(self):
        self.done = True

    def __str__(self):
        status = "Done" if self.done else "Not done"
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def addtask(self, task):
        self.tasks.append(Task(task))
        print(f"Task added to the list.")

    def removetask(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            print(f"Task removed from the list.")
        else:
            print("Invalid task index.")

    def marktaskasdone(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.markasdone()
            print(f"Task '{task.description}' marked as done.")
        else:
            print("Invalid task index.")

    def listtasks(self):
        print("Tasks in the list:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as done")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.addtask(task)
        elif choice == "2":
            task_index = int(input("Enter the task index to remove: ")) - 1
            todo_list.removetask(task_index)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as done: ")) - 1
            todo_list.marktaskasdone(task_index)
        elif choice == "4":
            todo_list.listtasks()
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
