#!/usr/bin/env python3

import os

'''
The working directory is the user_data 
which is inside the Trash directory
'''

class File_management:
    def __init__(self):
        #check_list consists of all the required directories
        self.check_list = {'Photos', 'Videos', 'Audio', 'Documents', 'Others'}
        self.pic_form = ['.jpg', '.jpeg', '.png']
        self.vid_form = ['.mp4', '.mkv']
        self.doc_form = ['.pdf', '.txt', '.epub']
        self.aud_form = ['.wav', '.mp3']
        self.pics = []
        self.vids = []
        self.docs = []
        self.auds = []
        
    def check_dir(self):
        #This check whether all elements in check_list are in the previous folder
        if not self.check_list.issubset(set(os.listdir('..'))):
            [os.makedirs('../'+x, exist_ok=True) for x in self.check_list]

    #This function will move the files to the corresponding position
    #matching the corresponding data types
    def folder_shift(self, extensions, folder):
        self.pics=[y for x in extensions for y in self.all_files if x in y]
        #The additional double quotes would read the entire file as a single string and the spaces would no longer be a problem
        [os.system('mv ../"{}" ../{}/'.format(x, folder)) for x in self.pics]
        
    def categorise(self):
        self.all_files = set(os.listdir('..')) - self.check_list
        self.all_files -= {'user_data'}

        #These lines shift the files into the directories
        self.folder_shift(self.pic_form, 'Photos')
        self.folder_shift(self.vid_form, 'Videos')
        self.folder_shift(self.aud_form, 'Audio')
        self.folder_shift(self.doc_form, 'Documents')

        for x in os.listdir('..'):
            #This line moves all other files to the other directory
            if os.path.isfile(x):
                os.system('mv ../"{}" ../Others'.format(x))
            else:
                #This line moves all directories other than our default ones to Others
                if x not in list(self.check_list) + ['user_data']:
                    os.system('mv ../"{}" ../Others'.format(x))

if __name__ == '__main__':
    a = File_management()

    a.check_dir()
    a.categorise()
