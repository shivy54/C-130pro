import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")

df = df.dropna()


df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]
df.head()
df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.to_csv("stars.csv")