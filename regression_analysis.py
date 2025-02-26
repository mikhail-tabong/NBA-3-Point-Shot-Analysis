import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from nba_api.stats.endpoints import LeagueDashTeamStats

# Define seasons
seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(2000, 2024)]

# Initialize lists
three_attempt_ratio = []
efg_list = []

# Fetch Data
for season in seasons:
    try:
        team_stats = LeagueDashTeamStats(season=season, season_type_all_star='Regular Season').get_data_frames()[0]
        total_FGA = team_stats['FGA'].sum()
        total_FG3A = team_stats['FG3A'].sum()
        total_FGM = team_stats['FGM'].sum()
        total_FG3M = team_stats['FG3M'].sum()

        efg = (total_FGM + 0.5 * total_FG3M) / total_FGA if total_FGA else None
        ratio_3_attempt = total_FG3A / total_FGA if total_FGA else None

        efg_list.append(efg)
        three_attempt_ratio.append(ratio_3_attempt)
    except:
        efg_list.append(None)
        three_attempt_ratio.append(None)
    time.sleep(1)

# Create DataFrame
data = pd.DataFrame({'Season': seasons, "eFG%": efg_list, "3P Attempt Ratio": three_attempt_ratio})

# Remove missing data
data_reg = data.dropna(subset=['eFG%', '3P Attempt Ratio'])

# Regression Analysis
X = data_reg['3P Attempt Ratio']
y = data_reg['eFG%']
X_const = sm.add_constant(X)
model = sm.OLS(y, X_const)
results = model.fit()

# Print Regression Summary
print("\nRegression Analysis Summary:")
print(results.summary())

# Plot Regression Analysis
plt.figure(figsize=(10, 6))
sns.regplot(x='3P Attempt Ratio', y='eFG%', data=data_reg, ci=95, scatter_kws={"s": 50})
plt.xlabel("3P Attempt Ratio")
plt.ylabel("Effective Field Goal Percentage (eFG%)")
plt.title("Regression Analysis: eFG% vs. 3P Attempt Ratio")
plt.grid(True)
plt.tight_layout()
plt.show()
