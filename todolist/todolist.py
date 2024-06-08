
#It is a simple todo list
#The class is defined by using class

class List:
    # def is udes to define the function

    def __init__(self):

        # self is used to refer to current instance of class

        self.tasks = []

# The task is added

    def add(self, task):
        self.tasks.append(task)
        print("Task Added")

# This is used to view all the tasks present currently

    def view(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list.")

#This is used to mark the current task as completed

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1] += " - Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

#This is used to delete the task

    def delete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")


def main():
    
    #The List() refer to class List

    todlist = List()
    while True:
        print("1. Add the Task")
        print("2. View the Tasks")
        print("3. Mark the Task as Completed")
        print("4. Delete the Task")
        print("5. Quit")
        Input = input("Enter  number from above to perform the task: ")

        if Input == '1':
            task = input("Enter the task: ")
            todlist.add(task)

        elif Input == '2':
            todlist.view()

        elif Input == '3':
            task_number = int(input("Enter task number to mark the task as completed: "))
            todlist.mark_completed(task_number)

        elif Input == '4':
            task_number = int(input("Enter task number to delete the task: "))
            todlist.delete(task_number)

        elif Input == '5':
            print("The task is Exiting...")
            break

        else:
            print("Invalid choice")
            print("Provide valid input")


if __name__ == "__main__":
    main()
