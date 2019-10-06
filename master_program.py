import logging
import empty_trash
from create_dir import File_management

class Master(File_management):
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