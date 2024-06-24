import colorama
from colorama import Fore
colorama.init(autoreset = True)

tasks, statuses, tasks_lower = [], [], []

def add_tasks():
    while True:
        task_name = input('Name your task (type "done" when finished adding tasks or "undo" to undo your previous action): ')

        if task_name.lower() == 'done':
            break

        if task_name.lower() in tasks_lower:
            print('Look\'s like that item is already in your to-do list!')
            continue

        tasks.append(task_name)
        tasks_lower.append(task_name.lower())
        statuses.append('Incomplete')

        print('Task added!')

def view_tasks():
    if len(tasks) == 0:
        print('No tasks here!')
    else:
        for i in range(len(tasks)):
            color = Fore.YELLOW if statuses[i] == 'Incomplete' else Fore.GREEN
            print(f'{color}{tasks[i]}: {statuses[i]}')

def mark_as_complete():
    while True:
        if len(tasks) == 0:
            print('There\'s nothing to mark complete!')
            break
        elif statuses.count('Complete') == len(statuses):
            print('All tasks have been marked complete!')
            break

        task_to_mark = input('Enter the task you want to mark as complete \n\
(type "done" when finished marking tasks complete or "all" to mark all tasks complete): ')

        if task_to_mark.lower() == 'done':
            break

        if task_to_mark.lower() == 'all':
            for j in range(len(statuses)):
                statuses[j] = 'Complete'
                
            continue

        try:
            if task_to_mark.lower() not in tasks_lower:
                raise ValueError(f'"{task_to_mark}" is not in your list!')
        except ValueError as v:
            print(v)
            continue

        marked_task_index = tasks_lower.index(task_to_mark.lower())

        if statuses[marked_task_index] == 'Complete':
            print('This task has already been marked complete!')
            continue
        else:
            statuses[marked_task_index] = 'Complete'

        print(f'"{tasks[marked_task_index]}" has been marked complete!')
        
def delete_tasks():
    while True:
        if len(tasks) == 0:
            print('The list is empty!')
            break

        task_to_delete = input('Enter the task you want to delete \
(type "done" when finished deleting tasks or "all" to delete all tasks): ')

        if task_to_delete.lower() == 'done':
            break

        if task_to_delete.lower() == 'all':
            tasks.clear()
            statuses.clear()
            tasks_lower.clear()
            
            print('All tasks have been deleted!')
            break

        try:
            if task_to_delete.lower() not in tasks_lower:
                raise ValueError(f'"{task_to_delete}" is not in your list!')
        except ValueError as v:
            print(v)
            continue

        deleted_task_index = tasks_lower.index(task_to_delete.lower())

        print(f'"{tasks[deleted_task_index]}" has been deleted!')

        tasks.remove(tasks[deleted_task_index])
        tasks_lower.remove(tasks_lower[deleted_task_index])
        statuses.remove(statuses[deleted_task_index])

print('Welcome to the to-do list app!')

while True:
    print('\nMenu:\n\
1. Add a task\n\
2. View tasks\n\
3. Mark a task as complete\n\
4. Delete a task\n\
5. Quit\n')
    
    try:
        menu_selection = int(input('Please select an option from the menu by entering it\'s corresponding number: '))

        if menu_selection < 1 or menu_selection > 5:
            raise ValueError
    except ValueError:
        print(f'Please enter a valid numerical value and ensure the number has a corresponding menu option.')
    else:
        if menu_selection == 1:
            print('\nAdd tasks:')
            add_tasks()
        elif menu_selection == 2:
            print('\nView tasks:')
            view_tasks()
        elif menu_selection == 3:
            print('\nMark a task as complete:')
            mark_as_complete()
        elif menu_selection == 4:
            print('\nDelete a task:')
            delete_tasks()
        elif menu_selection == 5:
            break

print('\nThank you for using the to-do list app!')