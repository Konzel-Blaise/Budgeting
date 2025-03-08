#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:48:16 2025

@author: blazer
"""
import os 
import pandas as pd
import shutil

# attempting to create a function that imports Cap1 data
# this will focus on returning newest expenses \
#updating with past database will be done elswhere
#________________________________________________


def load_expense_history(pathname, search_string):
    
    working_directoy = os.getcwd()
    #change to Downloads folder
    os.chdir(pathname)
    # Define the string you want to search for in the filename
    #search_string = 'transaction_download'
    # Get the current directory
    current_folder = os.getcwd()
    # List all files in the current folder that contain 'string' in the filename
    files_containing_string = []
    # Iterate through the files in the current folder
    for filename in os.listdir(current_folder):
        file_path = os.path.join(current_folder, filename)
        # Ensure it's a file (and not a directory) and check if the string is in the filename
        if os.path.isfile(file_path) and search_string in filename:
            files_containing_string.append(filename)
    # List the files found
    print("Files containing 'transaction_download' in the filename:")
    print(files_containing_string)
    
    newest_expenses = []
    #reading in both bank statements
    for i, files in enumerate(files_containing_string):
        # print(f"imported {files} statement successfully")
        df = pd.read_csv(files)
        newest_expenses.append(df)

        #if these are transaction downloads recently downloaded from cap1 we want to import and auto move files to archive. 
        if search_string == "transaction_download" and i>0:
            # could be improved, assumes only 2 files (Savor and Venture)
            full_path = [pathname + "/" + files_containing_string[0], pathname + "/" + files_containing_string[1]]
            for f in full_path: 
                shutil.move(f, "/Users/blazer/PyProjects/Personal_Finance/Cap1_Archive")

    #change back to working directory
    os.chdir(working_directoy)
    return(newest_expenses) 


# plotting funcationality 

















