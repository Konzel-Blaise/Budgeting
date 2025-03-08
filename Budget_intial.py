#!/usr/bin/env python

#trying to automate budgeting from capital one csv exported statements. 

# import numpy as np
# import csv
import pandas as pd
# import os
import matplotlib.pyplot as plt
# this may be pulling from local copy.. need to fix 
from func_load_cap1 import load_expense_history
# import plotly.express as px
# import plotly.graph_objects as go 
# from dash import Dash, html, dcc, dash_table
from plotter_test import html_plotter

#import new data from downlaods 
path = "/Users/blazer/Downloads"
search_string = 'transaction_download'

dataframes = load_expense_history(path, search_string)

print("DATA IMPORTED....PLEASE REVIEW")
print(dataframes)

#%% section to merge with existing data

#import MASTER data from local "Personal_Finance/Budgeting" directory 

MASTER = load_expense_history("/Users/blazer/PyProjects/Personal_Finance/Budgeting", "MASTER_SPEND_HISTORY")
MASTER = MASTER[0]
print(MASTER)

if dataframes == []: 
    print("--------NO NEW DATA--------")
    
else: 
    # Append or concatenate all DataFrames in the list
    RECENT = pd.concat(dataframes, ignore_index=True)
    print("--------NEW DATA ADDED TO RECENT--------")
# this was used to write original file - probably wont need again
#RECENT.to_csv('MASTER_SPEND_HISTORY.csv', index=False)  


#%% Update MASTER 

MASTER = pd.concat([MASTER, RECENT], ignore_index=True)
MASTER.to_csv('/Users/blazer/PyProjects/Personal_Finance/Budgeting/MASTER_SPEND_HISTORY.csv', index=False)  

#%% RECENT STATS

#remove credit payments marked as NaN in the Debit column
credit_expenses = RECENT.dropna(subset=['Debit'])

#calc number totals of each categories in fallout
merch = credit_expenses["Category"].value_counts()
expen_tot = credit_expenses["Debit"].sum()

print(f"number of merchandise expenses {sum(merch)} for a total of ${expen_tot}")

### quick plotting pie chart
plt.figure()
plt.pie(merch, labels=credit_expenses["Category"].unique(), autopct='%1.1f%%', startangle=90)
# Title
plt.title('Expenditure Distribution')
# Show the plot
plt.show()


#%% Monthly Stats

#convert transaction date column to type datetime
MASTER["Transaction Date"] = pd.to_datetime(MASTER["Transaction Date"], format="%Y-%m-%d")
# adding month column to MASTER
MASTER['Month'] = MASTER["Transaction Date"].dt.month
# locate(loc) rows with trans date in november (11)
print(MASTER.loc[MASTER['Month']==11])


#%% Plotter call 

html_plotter(MASTER)




