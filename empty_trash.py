from create_dir import File_management
from os import system

def empty_trash():
    create_dir_class = File_management()
    check_list = list(create_dir_class.check_list)

    for directory in check_list:
        system('rm -r ../{}'.format(directory))

if __name__ == '__main__':
    empty_trash()