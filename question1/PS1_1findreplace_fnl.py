#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:24:09 2018

@author: jenniferlaing

-------------------------------------
CTA200H 2018
Problem Set #1

Question #1
Find and replace
-------------------------------------
"""

import os
import glob
import sys
import fileinput
import shutil


#look for files ending in .txt and makes a list of names
FileNames = glob.glob("*.txt") #generates an array of file names

#file = 'textfiles/Dickens1.txt'

def Replace(file, findwrd, replacewrd):
    for line in fileinput.input(file, inplace=1):
        if findwrd in line:
            line = line.replace(findwrd, replacewrd)
        sys.stdout.write(line)
        

#identify current directory and create a new one in which to put changed files
working_dir = os.getcwd()
new_directory = os.path.join(working_dir, r'Replace')
if not os.path.exists(new_directory):
   os.makedirs(new_directory)

#copy text files into new directory
for files in FileNames:
    shutil.copy(files, new_directory)


#Request word to find 
find_word = ' ' + input("Input word to find: ") + ' '
print(find_word)

#Request word with which to replace the old word
new_word = ' ' + input("Input new word: ") + ' '
print(new_word)


#make the change to the new files
if __name__ == '__main__':
    files = os.listdir(new_directory)
    for file in files:
        newfile = os.path.join('Replace', file)
        Replace(newfile, find_word, new_word)



