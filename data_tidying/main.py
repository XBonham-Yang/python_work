#this is my learning notes
import pandas as pd

df = pd.read_csv('data/titanic.csv')

print(df.shape)
#I need to put print but NB doesn't need print

df.info()
print(df.head())