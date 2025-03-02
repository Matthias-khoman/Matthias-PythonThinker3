import os 
filepath = os.getcwd()

fullpath = os.path.join(filepath, "file.txt")

if os.path.exists(fullpath):
    print("{} exist".format)