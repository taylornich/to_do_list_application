The To-Do application is a command-line tool for managing tasks and creating a simple to-do list. It provides the user with 4 options for manipulating a to do list including adding a task, viewing the tasks, marking a task as complete, delete a task, and an option to quit the application.
The application provides a basic menu-driven user interface for interacting with a task list.

The Features:
1. Add a task: adds a new task to the list with a title.
2. View tasks: This features allows the user to view the tasks they have added to the to do list as well as their completion status.
3. Mark complete: Allows the user to view their current task list and completion rates, select a specific incomplete task and change the status to complete.
4. Delete a task: This feature allows the user to look at their current task list, select a specific task and remove the task from the list.
5. Quit: Allows the user to quit the application when they are finished making and manipulating their task list.

Installing this application:
1. Clone the repository
2. Navigate to the application directory
3. Run the application
4. Use the application, follow the on screen menu to choose what you would like to do to your to-do list.

Error Handling in this application:
There are a few different except blocks in the code to try handling errors before they arise.
- ValueError: This will be raised if the user enters an input that is not a valid number when enter the desired task index for the different options.
- IndexError: This will be raised if the index entered by the user is out of range when trying to mark a task as complete or when the user is trying to delete a task.
- Exception: This will be raised if an unexpected error occurs while the code is running.

