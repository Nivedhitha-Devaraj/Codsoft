class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            print(f'Task "{removed_task}" removed.')
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_index)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '4':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
