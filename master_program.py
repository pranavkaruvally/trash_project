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
    def month_checker(self):
        file = open('app.log', 'r')
        if self.month_no != file.read().split('-')[1]:
            self.empty_trash_logger()
            #Here after emptying the trash the log file will contain two infos which are
            #the info of sorting the trash and the info of emptying the trash
            #Even if the program is executed only after a few months the code will work fine
            #As the last sorting and emptying took place at almost the same time
        file.close()

if __name__ == "__main__":
    main = Master()
    main.create_dir_logger()
    main.month_checker()