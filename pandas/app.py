import pandas as pd
from pandas import re

df = pd.read_csv('pokemon_data.csv')

# df.columns
# print(df['Name'])

#print(df.head(3))


# print(df.iloc[2,1])

# printb (df.loc[df['Type 1']=='Grass'])

# df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"] 

# df["Total"]= df.iloc[:, 4:9].sum(axis=1)

# df.to_csv('modified.csv',index=False)

# new_df = df.loc[(df["Type 1"]=="Grass") & (df["Type 2"]=="Poison")]

# new_df.to_csv('GrassPoison.csv')

printDF = df.loc[df['Name'].str.contains('Fire | Grass', flags=re.i, regex=True)]
print(printDF)