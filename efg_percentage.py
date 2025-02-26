import time
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import LeagueDashTeamStats

# Define seasons
seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(2000, 2024)]

# Initialize lists
efg_list = []

# Fetch Data
for season in seasons:
    try:
        team_stats = LeagueDashTeamStats(season=season, season_type_all_star='Regular Season').get_data_frames()[0]
        total_FGA = team_stats['FGA'].sum()
        total_FGM = team_stats['FGM'].sum()
        total_FG3M = team_stats['FG3M'].sum()

        efg = (total_FGM + 0.5 * total_FG3M) / total_FGA if total_FGA else None
        efg_list.append(efg)
    except:
        efg_list.append(None)
    time.sleep(1)

# Create DataFrame
data = pd.DataFrame({'Season': seasons, "eFG%": efg_list})

# Graph 2: Effective Field Goal Percentage (eFG%) Over Seasons
plt.figure(figsize=(12, 6))
plt.plot(data['Season'], data["eFG%"], marker='o', linestyle='-', color='green')
plt.xlabel('Season')
plt.ylabel('Effective Field Goal Percentage (eFG%)')
plt.title("NBA Effective Field Goal Percentage (eFG%) per Season (2000-2024)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
