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
