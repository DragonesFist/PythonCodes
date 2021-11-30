# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 00:58:16 2021

@author: Jagadeesh Damarla
"""
import pandas as pd
import csv
# statement = pd.read_csv("sample.csv")
master_ddl_list=[]

with open('D://PythonCodes//DDL Statements/sample.csv') as file:
    csvreader =  csv.reader(file)
    for rowIndex, row in enumerate(csvreader): # for each row
        init_str = "create table "
        temp_list = []
        if rowIndex>0:
            init_str = init_str+row[0]+" ( "
            for itemIndex, item in enumerate(row): # for each element in the row
                if itemIndex>0:
                    init_str=init_str+row[itemIndex] + " "
                    if itemIndex%2==0 and itemIndex+1!=len(row):
                        init_str = init_str+","
                    if itemIndex%2==0 and itemIndex+1==len(row):
                        init_str = init_str+" )"
            temp_list.append(rowIndex)
            temp_list.append(init_str)
            master_ddl_list.append(temp_list)

output = pd.DataFrame(master_ddl_list,columns=['Row Number','DDL Statement'])
output.to_csv("D://PythonCodes//DDL Statements/DDLStatements.csv", index=False)
