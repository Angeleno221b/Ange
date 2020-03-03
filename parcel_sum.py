# Author: Xuanye Zuo
# Date: 02/03/2020
# Purpose: Summarize the APN info for parcel file
# Project: Land Inventory

import os
import pandas as pd
 
"""
save_path = "//Scagfs02/gisdata/Data3/Tom_Vo/=Annual_LU_Update/shp/OR"
#convert txt file to csv file 
in_filename = os.path.join(save_path,'Parcel_OR.txt')
out_filename = os.path.join(save_path,'Parcel_OR.csv')
 
df = pd.read_csv(in_filename, sep=",")
df.to_csv(out_filename, index=False)
"""
#import two files for join
df1=pd.read_csv("//Scagfs02/gisdata/ata3/Tom_Vo/=Annual_LU_Update/shp/OR/Parcel_Polygons/Attribute.csv")
df2=pd.read_csv("

#join the files by showing all the records in both files
df3=pd.merge(df1, df2, how='outer')

#check the null valuein the join table
df3.isnull().any()
        
                


