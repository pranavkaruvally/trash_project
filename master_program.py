import logging
from create_dir import File_management

class Master(File_management):
    def logger(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('Trash has been sorted')

if __name__ == "__main__":
    main = Master()
    main.check_dir()
    main.categorise()
    main.logger()