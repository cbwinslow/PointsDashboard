# Clean data file for use in app

# Data file comes from the pybaseball Database project

# All_stats.csv


import pandas as pd


df = pd.read_csv("All_Stats.csv")

df = df[df['Season_bat'] >= 2000]


df.loc[df["Season_bat"].isnull(),'Season_bat'] = df['Season_pit'] 


df.loc[df["Name_bat"].isnull(),'Name_bat'] = df['Name_pit'] 

df.loc[df["Team_bat"].isnull(),'Team_bat'] = df['Team_pit'] 

df.loc[df["Age_bat"].isnull(),'Age_bat'] = df['Age_pit'] 


df.loc[df["Season_pit"].isnull(),'Season_pit'] = df['Season_bat'] 

df.loc[df["Name_pit"].isnull(),'Name_pit'] = df['Name_bat'] 

df.loc[df["Team_pit"].isnull(),'Team_pit'] = df['Team_bat'] 

df.loc[df["Age_pit"].isnull(),'Age_pit'] = df['Age_bat'] 


df.fillna(0, inplace=True)

# df = df.drop('Unnamed: 0_bat', 1)
# df = df.drop('Unnamed: 0_pit', 1)

print(df.head())


df.to_csv('All_Stats.csv')


print('successful')

