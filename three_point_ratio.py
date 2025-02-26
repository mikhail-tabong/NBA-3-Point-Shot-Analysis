import time
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import LeagueDashTeamStats

# Define seasons
seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(2000, 2024)]

# Initialize lists
three_attempt_ratio = []

# Fetch Data
for season in seasons:
    try:
        team_stats = LeagueDashTeamStats(season=season, season_type_all_star='Regular Season').get_data_frames()[0]
        total_FGA = team_stats['FGA'].sum()
        total_FG3A = team_stats['FG3A'].sum()
        
        ratio_3_attempt = total_FG3A / total_FGA if total_FGA else None
        three_attempt_ratio.append(ratio_3_attempt)
    except:
        three_attempt_ratio.append(None)
    time.sleep(1)

# Create DataFrame
data = pd.DataFrame({'Season': seasons, "3P Attempt Ratio": three_attempt_ratio})

# Graph 3: Three-Point Attempt Ratio Over Seasons
plt.figure(figsize=(12, 6))
plt.plot(data['Season'], data["3P Attempt Ratio"], marker='o', linestyle='-', color='purple')
plt.xlabel('Season')
plt.ylabel('3-Point Attempt Ratio')
plt.title("Ratio of 3-Point Attempts to Total Field Goal Attempts per Season (2000-2024)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
