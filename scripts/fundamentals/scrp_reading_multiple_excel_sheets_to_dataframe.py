# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:11:24 2020

@author: Ashish
"""

import pandas as pd
import numpy as np

excel_file_path = "python_3/fake_data_generator/data/logbook.xlsx"
# create dataframe for testing
# xls = pd.ExcelFile(excel_file_path)
# xls_sheet_names = xls.sheet_names
# print(xls_sheet_names)

# Read all sheets and store it in a dictionary
# sheet_to_df_map = {}
# for sheet_name in xls.sheet_names:
#     sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
df_sheet_map = pd.read_excel(excel_file_path, sheet_name=None)
# for key, val in df_sheet_map.items():
    # print(key)
    #print(val)
# read specific cols of the excel sheet
df_sheet_map = pd.read_excel(excel_file_path, sheet_name=None,
                             index_col=None, na_values=['NA'], usecols = "B:I")

# for key, val in df_sheet_map.items():
    # print(val)
    
# convert dictionary to dataframe
# logbook_data = pd.DataFrame(df_sheet_map,
#                             columns = df_sheet_map.keys())
# logbook_data = pd.DataFrame.from_records(df_sheet_map)
logbook_data = pd.Series(df_sheet_map).to_frame()
print(logbook_data.columns)