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

# create_file(fullpath)


# create_file()
# Task 2: Add new task
def add_new_task(fullpath: str):
    task = input('What is your task? ')
    with open(fullpath, 'a') as file:
        file.write(f'\n{task}')
    print('Task added')

# add_new_task(fullpath)

# Task 3: View all tasks
def view_all_tasks(fullpath: str) -> list:
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
    return tasks
    

view_all_tasks(fullpath)

# Task 4: Mark Task as done
def mark_task_as_done(fullpath):
    print('Marking a task as done')
    
    tasks = view_all_tasks(fullpath)
    if len(tasks) <= 0:
        print('No Tasks available')
        return
    td = int(input('Which task have you done? '))
    if td < 1 or td > len(tasks) - 1:
        print('invalid input')
        return
    task_index = td
    if '[DONE]' in tasks[task_index]:
        print('This is already done')
    else:
        tasks[task_index] = tasks[task_index].strip()+" [DONE] "
        print(f'Task {td} marked as done. ')
    
    with open(fullpath, 'w') as file:
        file.writelines(tasks)

# mark_task_as_done(fullpath)

# Task 6: Delete a task
def delete_task(fullpath: str) -> None:
    tasks = view_all_tasks(fullpath)
    if len(tasks) <= 0:
        print('No tasks available')
        return
    dt = int(input('which task do you want to remove? '))
    if dt < 1 or dt > len(tasks):
        print('Invalid input')
        return
    task_index = dt
    tasks_deleted = tasks.pop(task_index)
    with open(fullpath, 'w') as file:
        file.writelines(tasks)
    view_all_tasks(fullpath)

# delete_task(fullpath)

# Task 7:Display Menu
while True:
    print('Welcome to Your Task List:')
    print('\n')
    print("1. Create a new task file")
    print("2. View all tasks")
    print("3. Add new task")
    print("4. Delete a task")
    print("5. Mark a task as done")
    print("6. Exit")
    choice = int(input("What do you want to do? "))
    if choice == 1:
        create_file(fullpath)
    elif choice == 2:
        view_all_tasks(fullpath)
    elif choice == 3:
        add_new_task(fullpath)
    elif choice == 4:
        delete_task(fullpath)
    elif choice == 5:
        mark_task_as_done(fullpath)
    elif choice == 6:
        print("Exiting...\n")
        break
    else:
        print("Not a Valid option")



