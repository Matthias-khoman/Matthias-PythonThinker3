import os
# Task 1: Create new task file
filename = 'tasks.txt'
filepath = os.getcwd()
fullpath = os.path.join(filepath, filename)
def create_file(fullpath: str):
    if not os.path.exists(fullpath):
        with open(fullpath, 'w') as file:
            file.write('My Task list:')
        print('\nOK, creating a new file')
    else:
        print('file already exists')
        choice = input('Do you want to override? (y/n)')
        if choice == 'y':
            with open(fullpath, 'w') as file:
                file.write('My Task list:')
            print('\nOK, creating a new file')


# create_file()
# Task 2: Add new task
def add_new_task(fullpath: str):
    task = input('What is your task? ')
    with open(fullpath, 'a') as file:
        file.write(f'\n{task}')
    print('Task added')

# add_new_task()

# Task 3: View all tasks
def view_all_tasks(fullpath: str):
    with open(fullpath, 'r') as file:
        tasks = file.readlines()
    if len(tasks) == 1:
        print('NO TASKS FOUND')
        return []
    for i in range(len(tasks)):
        if i == 0:
            print(tasks[i].strip())
        else:
            print(f'{i}. {tasks[i]}'.strip())
    

# view_all_tasks(fullpath)

# Task 4: Mark Task as done
def mark_task_as_done(fullpath):
    td = int(input('Which task have you done? '))
    tasks = view_all_tasks(fullpath)
    for i in range(len(tasks)):
        if i == td:
            with open(fullpath, 'a') as file:
