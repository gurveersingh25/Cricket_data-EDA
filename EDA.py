import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\india\OneDrive\Documents\Cricket_data.xlsx", sheet_name="Cricket_data")
df.head()
df.info()
df.describe(include='all')
df.isnull().sum().sort_values(ascending=False)
