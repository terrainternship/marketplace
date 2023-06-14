#import numpy as np
import pandas as pd
#from matplotlib import pyplot as plt
from os import listdir
path = 'MPSTATS/Магазин/MPSTATS 01062022-31052023 Выручка по дням/'
df = pd.DataFrame()
for f in listdir(path):
    df1 = pd.read_csv(path + f, sep=';', index_col='Дата', parse_dates=['Дата'], decimal=',', dayfirst=True)
    df = pd.concat([df, df1], ignore_index=False)
df = df.drop('Unnamed: 18', axis=1)
df = df.iloc[:, :8]
#print(df.sum(axis=0))
df.to_csv('MPSTATS/Магазин/byday.csv')
path = 'MPSTATS/Магазин/MPSTATS 01062022-31052023 Товары/'
df = pd.DataFrame()
for f in listdir(path):
    df1 = pd.read_csv(path + f, sep=';', decimal=',')
    df = pd.concat([df, df1], ignore_index=True)
features = df.select_dtypes(include='number')
sel_na = features.isna().sum()
ls_cols = sel_na[sel_na == 0].index
df[ls_cols].to_csv('MPSTATS/Магазин/goods.csv')