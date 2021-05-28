import pandas as pd
import numpy as np

data = pd.read_excel("etudiant.xls",sheet_name='tab1', usecols="A,C:H" , skiprows =5,index_col=0)
data.dropna(inplace=True)
print(data)
print(data.sum())
print(data.mean(axis=1))