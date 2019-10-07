#!/usr/bin/env python3

from create_dir import File_management
from os import system, path

def empty_trash():
    create_dir_class = File_management()
    #The set check_list in the class File_management has
    #the names of all the folders that were created
    #and hence the names of all the folders to be deleted
    check_list = list(create_dir_class.check_list)

    for directory in check_list:
        #This line checks whether each of the directories are present
        #The function is actually used to check whether the file is a directory
        if path.isdir('../' + directory):
            system('rm -r ../{}'.format(directory))

if __name__ == '__main__':
    empty_trash()
