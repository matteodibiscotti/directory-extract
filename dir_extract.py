import os, shutil

path = 'D:\\AGAIN\\NEW'

for dir in os.listdir(path):
    f = []
    for (dirpath, dirnames, file) in os.walk(path + '\\' + dir):
        f.extend(file)
    for i in f:
        source = dirpath + '\\' + i
        dest = path + '\\' + i
        #shutil.move(path + '\\' + dir + '\\' + i, path)
        shutil.move(source, dest)

'''
1. loop through all the directories
2. list files in that directory
3. shutil to copy files to one level up
'''