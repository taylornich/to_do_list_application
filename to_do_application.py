# module 2 mini project 

# task 1
class Application:

    def __init__(self):
        self.list = []

    def main_menu(self):

        print('''Welcome to the To Do List Application!
            
            Menu:
            1. Add a task
            2. View tasks
            3. Mark task as complete
            4. Delete a task
            5. Quit''')
        
    # task 2
    def add_task(self, title="incomplete"):
        self.list.append({"title": title, "complete": False})

    def view_task_list(self):
        if not self.list:
            print("There is nothing in the to do list yet :()")
        else:
            print("Things to do:")
            for i in range(len(self.list)):
                task = self.list[i]
                status = "complete" if task['complete'] else "incomplete"
                print(f"{i+1}. {task['title']} : {status}")

    def mark_complete(self, task_index):
        if self.is_valid_index(task_index):
            self.list[task_index - 1]['complete'] = True

            print("Task was successfully marked complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if self.is_valid_index(task_index):
            self.list.pop(task_index - 1)
            print("Task was successfully deleted.")
        
        else:
            print("Invalid task index.")

    def quit(self):
        print("You have successfully quit the application.")
        quit()

    def is_valid_index(self, index):
        return 1 <= index <= len(self.list)

def main():
    todo_list = Application()

    while True:
        # task 3 and 4
        try:
            menu_choice = input("Please enter number of the action you would like to perform: ").strip()

            if menu_choice == "1":
                title = input("Enter the title of the task to add: ").strip()
                todo_list.add_task(title)

                print(f"{title} added to the to do list successfully.")

            elif menu_choice == "2":
                todo_list.view_task_list()
            
            elif menu_choice == "3":
                todo_list.view_task_list()

                task_index = input("What is the index of the task to mark as complete: ").strip()
                if task_index.isdigit():
                    todo_list.mark_complete(int(task_index))
                else:
                    print("The input provided was invalid, please enter a valid number.")

            elif menu_choice == "4":
                todo_list.view_task_list()

                task_index = input("What is the index of the task to delete from the to do list: ").strip()

                if task_index.isdigit():
                    todo_list.delete_task(int(task_index))
                else:
                    print("The input provided was invalid, please enter a valid number.")
            elif menu_choice == "5":
                todo_list.quit()

            else:
                print("The choice entered is invalid. Please enter a number between 1 and 5, corresponding to the menu action you would like to perform.")

        except ValueError as InputError:
            print(f"ValueError occurred: {InputError}")

        except IndexError as IndexOutOfBounds:
            print(f"IndexError occurred: {IndexOutOfBounds}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        finally:
            print("Thank you for using the to do list application :)")

if __name__ == "__main__":
    main()