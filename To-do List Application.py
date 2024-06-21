tasks, statuses, tasks_lower = [], [], []
incomplete = True
status = 'Incomplete' if incomplete else 'Complete'

def check_response(user_input):
    while True:
        try:
            response = input(user_input)

            if response.lower() != 'yes' and response.lower() != 'no':
                raise ValueError('Invalid response. Please enter "yes" or "no".')
        except ValueError as v:
            print(v)
        else:
            return response.lower() == 'yes'

def add_tasks():
    while True:
        task_name = input('Name your task (type "done" when finished adding tasks): ')

        if task_name.lower() == 'done':
            break

        if task_name.lower() in tasks_lower:
            add_again = 'Look\'s like that task is already in your to-do list. \
Are you sure you want to add it again? (type "yes" or "no"): '

            if not check_response(add_again):
                print('Okay!')
                continue

        tasks.append(task_name)
        tasks_lower.append(task_name.lower())
        statuses.append(status)

        print('Task added!')

def view_list():
    for i in range(len(tasks)):
        print(f'{tasks[i]}: {statuses[i]}')

print('Welcome to the To-Do List App!\n\n\
Menu:\n\
1. Add a task\n\
2. View tasks\n\
3. Mark a task as complete\n\
4. Delete a task\n\
5. Quit')