import os
# Task 1: Create new task file
filename = 'tasks.txt'
filepath = os.getcwd()
fullpath = os.path.join(filepath, filename)
def create_file():
    if not os.path.exists(fullpath):
        with open(fullpath, 'w') as file:
            file.write('My Task list:')
        print('\nOK, creating a new file')
    else:
        print('file already exists')
        input('')

create_file()