#!/usr/bin/env python

#trying to automate budgeting from capital one csv exported statements. 

# import numpy as np
# import csv
import pandas as pd
import os
import matplotlib.pyplot as plt
# this may be pulling from local copy.. need to fix 
from func_load_cap1 import *
import plotly.express as px
import plotly.graph_objects as go 
from dash import Dash, html, dcc, dash_table

#import new data from downlaods 
path = "/Users/blazer/Downloads"
search_string = 'transaction_download'

dataframes = load_expense_history(path, search_string)

print("DATA IMPORTED....PLEASE REVIEW")
print(dataframes)


#%% section to merge with existing data

#import MASTER data from working directory 

MASTER = load_expense_history("/Users/blazer/PyProjects/Personal_Finance/Budgeting", "MASTER_SPEND_HISTORY")
MASTER = MASTER[0]
print(MASTER)

if dataframes == []: 
    print("--------NO NEW DATA--------")
    
    
else: 
    # Append or concatenate all DataFrames in the list
    RECENT = pd.concat(dataframes, ignore_index=True)
    
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

#%%


# try to group each type of expenditure and total - histogram

account_tot = MASTER.groupby(["Category"]).sum()


# fig = go.Figure([go.Histogram(x=MASTER['Category'], y=MASTER['Debit'])]).show(renderer='browser')

# fig2 = px.histogram(MASTER, x="Category", y="Debit").show(renderer='browser')

fig2 = px.histogram(MASTER, x="Category", y="Debit")


# Dash Definition --------------------
app = Dash()

app.layout = html.Div(children=[
    
    #Historgram Definition
    html.Div([
        html.H1(children='Cap1 Data Viewer'),
        html.Div(children='Viewing Histogram'),
        dcc.Graph(
            id='graph1',
            figure=fig2
        ),
    ]),
    
    #Table Definition
    html.Div([
        html.Div(children='Viewing Table'),
        dash_table.DataTable(data=MASTER.to_dict('records'), page_size=10)
        # dcc.Graph(
        #     id='graph2',
        #     figure=fig3
        
        # ), 
    ]),                  
])
           
app.run(debug=True, port=8054)
#http://127.0.0.1:8054/


#----------------------
# go two routes with this monthly and total 
# -------monthly stats 

# -------total stats 




