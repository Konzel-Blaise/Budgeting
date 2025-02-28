#!/usr/bin/env python

#trying to automate budgeting from capital one csv exported statements. 

# import numpy as np
# import csv
import pandas as pd
# import os
import matplotlib.pyplot as plt
from func_load_cap1 import *

#import new data from downlaods 
path = "/Users/blazer/Downloads"
search_string = 'transaction_download'

dataframes = load_expense_history(path, search_string)

print("NEW DATA IMPORTED....PLEASE REVIEW")
print(dataframes)


#%% section to merge with existing data

#import MASTER data from working directory 

MASTER = load_expense_history("/Users/blazer/PyProjects/Personal_Finance/Budgeting", "MASTER_SPEND_HISTORY")
MASTER = MASTER[0]
print(MASTER)


# Append or concatenate all DataFrames in the list
RECENT = pd.concat(dataframes, ignore_index=True)
# print(f'{RECENT}')


# this was used to write original file - probably wont need again
#RECENT.to_csv('MASTER_SPEND_HISTORY.csv', index=False)  


#%% Update MASTER 

MASTER = pd.concat([MASTER, RECENT], ignore_index=True)
MASTER.to_csv('MASTER_SPEND_HISTORY.csv', index=False)  

#%%

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
#

# try to group each type of expenditure and total - histogram

account_tot = RECENT.groupby(["Category"]).sum()

# plt.figure()
# plt.hist(account_tot["Debit"], bins=8)
# plt.show()


# categories = account_tot['Debit'].value_counts().index
# counts = account_tot['Debit'].value_counts().values
# plt.bar(categories, counts, width=0.5)


#---------------------------------------------------------------------

# need to beef out plotting 
# go two routes with this monthly and total 


# -------monthly stats 

# -------total stats 




