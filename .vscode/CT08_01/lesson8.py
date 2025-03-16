import os
# Task 1: Create new task file
filename = 'tasks.txt'
filepath = os.getcwd()
fullpath = os.path.join(filepath, filename)
def create_file():
    global fullpath
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
    else:
        print('file exists')

    
