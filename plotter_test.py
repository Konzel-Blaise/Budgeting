#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 20:16:47 2025

@author: blazer
"""
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go 
from dash import Dash, html, dcc, dash_table


def html_plotter(MASTER):

    app = Dash()
    app.layout = html.Div(children=[
        
        #Historgram Definition
        html.Div([
            html.H1(children='Cap1 Data Viewer'),
            html.Div(children='Viewing Histogram'),
            dcc.Graph(
                id='graph1',
                figure=px.histogram(MASTER, x="Category", y="Debit")
            ),
        ]),
        
        #Table Definition
        html.Div([
            html.Div(children='Viewing Table Data'),
            dash_table.DataTable(data=MASTER.to_dict('records'), page_size=10)
            # dcc.Graph(
            #     id='graph2',
            #     figure=fig3
            
            # ), 
        ]),  
        
        html.Div([
            html.Div(children='Updated on March 8th, 2025'),

        ]), 

    ])
               
    app.run(debug=True, port=8054)
    print('please visit.......http://127.0.0.1:8054/')


#__________ OLD CODE __________

# try to group each type of expenditure and total - histogram

# account_tot = MASTER.groupby(["Category"]).sum()



# # fig = go.Figure([go.Histogram(x=MASTER['Category'], y=MASTER['Debit'])]).show(renderer='browser')

# # fig2 = px.histogram(MASTER, x="Category", y="Debit").show(renderer='browser')

# fig2 = px.histogram(MASTER, x="Category", y="Debit")


# # Dash Definition --------------------
# app = Dash()

# app.layout = html.Div(children=[
    
#     #Historgram Definition
#     html.Div([
#         html.H1(children='Cap1 Data Viewer'),
#         html.Div(children='Viewing Histogram'),
#         dcc.Graph(
#             id='graph1',
#             figure=fig2
#         ),
#     ]),
    
#     #Table Definition
#     html.Div([
#         html.Div(children='Viewing Table'),
#         dash_table.DataTable(data=MASTER.to_dict('records'), page_size=10)
#         # dcc.Graph(
#         #     id='graph2',
#         #     figure=fig3
        
#         # ), 
#     ]),                  
# ])
           
# app.run(debug=True, port=8054)
# #http://127.0.0.1:8054/

