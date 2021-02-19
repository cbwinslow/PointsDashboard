# Clean data file for use in app

# Data file comes from the pybaseball Database project

# All_stats.csv


import pandas as pd


bat = pd.read_csv("All_Batting_Stats.csv")
pit = pd.read_csv("All_Pitching_Stats.csv")


#bat = bat.add_suffix('_bat')
#pit = pit.add_suffix('_pit')


df = pd.merge(bat, pit, on=['Season', 'Name', 'Age', 'Team'], how='outer', suffixes=('_bat', '_pit'))




df = df[df['Season'] >= 2000]




df.fillna(0, inplace=True)

df = df.drop('Unnamed: 0_bat', 1)
df = df.drop('Unnamed: 0_pit', 1)

print(df.head())






print('Add Player Info')
# Add Player Information
people = pd.read_csv('baseballdatabank-master/core/People.csv')

people['Player'] = people['nameFirst'].str.cat(people['nameLast'], ' ')
df = pd.merge(df, people, left_on=['Name'], right_on=['Player'], how='left', suffixes=('', '_y'))


print('Add Apperances')
# Add Poisition Appearances
appearances = pd.read_csv('baseballdatabank-master/core/Appearances.csv')
df = pd.merge(df, appearances, left_on=['playerID', 'Season'], right_on=['playerID', 'yearID'], how='left', suffixes=('', '_appear'))
 
# Relabel Columns
df.rename(columns = {'G_P':'G_as_P',
                        'G_C':'G_as_C',
                        'G_1b':'G_as_1B',
                        'G_2b':'G_as_2B',
                        'G_3b':'G_as_3B',
                        'G_ss':'G_as_SS',
                        'G_lf':'G_as_LF',
                        'G_cf':'G_as_CF',
                        'G_rf':'G_as_RF',
                        'G_of':'G_as_OF',
                        'G_dh':'G_as_DH',
                        'G_ph':'G_as_PH',
                        'G_Pr':'G_as_PR'}, inplace = True) 


print('Add Team Info')
# Add Team Information
team = pd.read_csv('baseballdatabank-master/core/Teams.csv')

team = team.add_suffix('_team')
df = pd.merge(df, team, left_on=['teamID', 'Season'], right_on=['teamID_team', 'yearID_team'], how='left', suffixes=('', '_team'))
 
df.fillna(0, inplace=True)


df.to_csv('All_Stats.csv')


print('successful')

