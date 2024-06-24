# Mini-Project: To-Do List Application

Author: Jaycob Hoffman

Date: 24 June 2024

## Documentation

The To-Do List Application is a CLI application that allows the user to easily create and manage a to-do list in a simple manner.

### Main Features

- **Add Tasks**: With the ```Add a task``` feature, the user can add as many tasks as they like. By default, each task will be assigned a status of "Incomplete". When the user is finished adding tasks, they can type "done" to exit the feature.
- **View Tasks**: With the ```View tasks``` feature, the user can easily view their list of tasks and their statuses in ```task-name: status (Incomplete/Complete)``` format. If the to-do list is empty, the user will be notified as such.
- **Mark Tasks Complete**: With the ```Mark a task as complete``` feature, the user can mark tasks complete by entering the task's name. If the task has not yet been marked complete, the status will be changed from "Incomplete" to "Complete". If it has been marked complete, the status will remain the same and the user will be reminded that the task has already been marked complete. If the to-do list is empty, the user will be notified as such. When the user is finished marking tasks complete, they can type "done" to exit the feature.
- **Delete Tasks**: With the ```Delete a task``` feature, the user can delete tasks until the to-do list is empty. If it is already empty, the user will be notified as such. When the user is finished deleting tasks, they can type "done" to exit the feature. They will also exit the feature when the list is empty.

### Bonus Features

- **Mark All Tasks as Complete/Delete All Tasks**: When marking tasks as complete, the user has the option to mark all tasks complete. Likewise, when deleting tasks, the user has the option to delete all tasks. Both can be accomplished by typing "all" when prompted.
- **Color Coding**: When viewing tasks, tasks with a status of "Incomplete" will be shown in yellow, while tasks with a status of "Complete" will be shown in green.
- **Case Insensitivity**: All user inputs are case-insensitive.

### UI

When the user first runs the To-Do List Application, the following UI will display:

```
Welcome to the to-do list app!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit

Please select an option from the menu by entering it's corresponding number: 
```

The user can select an option from the menu by entering the number that precedes it. When the task has finished, the menu will display again and prompt the user to select another option. This cycle will continue indefinitely until the user selects option #5 and quits the program. Then, the following message will display:

```
Thank you for using the to-do list app!
```

### Errors

The To-Do List Application will raise ```ValueError```s with accompanying messages under the following circumstances:

- If the user enters the name of a task that is not contained within the to-do list while marking tasks complete or while deleting tasks.
- If the user enters a non-numeric value or a number that is not between 1 and 5 (inclusive) while selecting options in the main menu.

For each circumstance, the To-Do List Application will continue to prompt the user until they enter an appropriate value.