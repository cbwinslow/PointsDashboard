
import pandas as pd


bat = pd.read_csv("All_Batting_Stats.csv")
# pit = pd.read_csv("All_Pitching_Stats.csv")

bat = bat[bat['Season'] >= 2000]

bat["Season"] = bat["Season"].astype(int)

min_year = bat.Season.min()
max_year = bat.Season.max()


SeasonRange = range(min_year, (max_year + 1) )

avgList = pd.DataFrame()

avgList = []
for year in SeasonRange:
    temp = bat[bat['Season'] == year]
    avg = temp.mean(axis=0, skipna=True)
    avg = avg.round(2)
    avgList.append(avg)




print(avgList)


