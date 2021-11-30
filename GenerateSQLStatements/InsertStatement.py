# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 05:32:42 2021

@author: Jagadeesh Damarla
"""
import pandas as pd
import csv
# statement = pd.read_csv("sample.csv")
master_ddl_list=[]

with open('D://PythonCodes//DDL Statements/sample_insert.csv') as file:
    csvreader =  csv.reader(file)
    for rowIndex, row in enumerate(csvreader): # for each row
        table_name = row[0]
        init_str = "insert into "+table_name+" values ("
        temp_list = []
        if rowIndex>0:
            for itemIndex, item in enumerate(row): # for each element in the row
                if itemIndex>0 and itemIndex+1!=len(row):
                    init_str=init_str+"'"+row[itemIndex]+"'" + ","
                if itemIndex+1==len(row):
                    init_str = init_str+"'"+row[itemIndex]+"'"
            init_str = init_str+")"+";"
            
                    
            temp_list.append(rowIndex)
            temp_list.append(init_str)
            master_ddl_list.append(temp_list)

output = pd.DataFrame(master_ddl_list,columns=['Row Number','DDL Statement'])
output.to_csv("D://PythonCodes//DDL Statements/DMLInsertStatements.csv", index=False)


