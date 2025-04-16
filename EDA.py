import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\india\OneDrive\Documents\Cricket_data.xlsx", sheet_name="Cricket_data")
df.head()
df.info()
df.describe(include='all')
df.isnull().sum().sort_values(ascending=False)
df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')]
def split_score(score):
    try:
        runs, wickets = map(int, str(score).split('/'))
        return runs, wickets
    except:
        return None, None

df['1st_innings_runs'], df['1st_innings_wkts'] = zip(*df['1st_inning_score'].map(split_score))
df['2nd_innings_runs'], df['2nd_innings_wkts'] = zip(*df['2nd_inning_score'].map(split_score))
df[['1st_innings_runs', '2nd_innings_runs', '1st_innings_wkts', '2nd_innings_wkts']].describe()
df.dropna(subset=['1st_innings_runs', '2nd_innings_runs'], inplace=True)
numeric_cols = ['1st_innings_runs', '2nd_innings_runs', 'home_runs', 'away_runs']
df[numeric_cols].corr()
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
sns.boxplot(x=df['1st_innings_runs'])
plt.title("Outliers in 1st Innings Runs")
plt.show()
sns.histplot(df['1st_innings_runs'], bins=30, kde=True, color='blue')
plt.title("Distribution of 1st Innings Runs")
plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.show()
top_winners = df['winner'].value_counts().head(10)
top_winners.plot(kind='bar', color='red')
plt.title("Top 10 Winning Teams")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.show()
toss_win = df[df['toss_won'] == df['winner']]
percentage = len(toss_win) / len(df) * 100
print(f"Percentage of matches where toss winner also won the match: {percentage:.2f}%")
sns.scatterplot(x='1st_innings_runs', y='1st_innings_wkts', data=df)
plt.title("Runs vs Wickets in 1st Innings")
plt.show()
top_players = df['pom'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_players.values, y=top_players.index, hue=top_players.index, palette="magma", dodge=False, legend=False)
plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Awards")
plt.ylabel("Player")
plt.tight_layout()
plt.show()
