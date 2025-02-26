import time
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import LeagueDashTeamStats

# Define seasons
seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(2000, 2024)]

# Initialize lists
two_attempts = []
three_attempts = []

# Fetch Data
for season in seasons:
    try:
        team_stats = LeagueDashTeamStats(season=season, season_type_all_star='Regular Season').get_data_frames()[0]
        total_FGA = team_stats['FGA'].sum()
        total_FG3A = team_stats['FG3A'].sum()
        total_FG2A = total_FGA - total_FG3A

        two_attempts.append(total_FG2A)
        three_attempts.append(total_FG3A)
    except:
        two_attempts.append(None)
        three_attempts.append(None)
    time.sleep(1)

# Create DataFrame
data = pd.DataFrame({'Season': seasons, "Two's Attempted": two_attempts, "Three's Attempted": three_attempts})

# Graph 1: Two-Point vs. Three-Point Shot Attempts per Season
plt.figure(figsize=(12, 6))
plt.plot(data['Season'], data["Two's Attempted"], label="Two's Attempted", marker='o', linestyle='-', color='blue')
plt.plot(data['Season'], data["Three's Attempted"], label="Three's Attempted", marker='o', linestyle='-', color='red')
plt.xlabel('Season')
plt.ylabel('Total Attempts')
plt.title("NBA Two's vs. Three's Attempted per Season (2000-2024)")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
