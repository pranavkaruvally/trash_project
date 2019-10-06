import logging
import empty_trash
import os
from create_dir import File_management

class Master(File_management):
    if os.path.isfile('app.log'):
        #Here we are trying the read the month of last execution for comparison
        file = open('app.log', 'r')
        #file.read() return the sentence, then splitting it with '-' sperates the dates
        #the 2nd element in the list after splitting is the month
        month_no = file.read().split('-')[1]
        file.close()
    def create_dir_logger(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('Trash has been sorted')
        self.check_dir()
        self.categorise()
    def empty_trash_logger(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('Trash has been emptied')
        empty_trash.empty_trash()


if __name__ == "__main__":
    main = Master()
    main.create_dir_logger()
    try:
        print(main.month_no)
    except AttributeError:
        print('app.log created')