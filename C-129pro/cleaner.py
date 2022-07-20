import pandas as pd
import csv
 
df = pd.read_csv("stars.csv")
print(df.shape)


del df["Radius"]
df.to_csv('cleaned.csv')