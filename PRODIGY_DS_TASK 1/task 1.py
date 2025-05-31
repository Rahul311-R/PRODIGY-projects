import pandas as pd
import matplotlib.pyplot as plt


file_name = 'data.csv'


df = pd.read_csv(file_name, skiprows=4)


year = '2023'
df_year = df[['Country Name', year]].dropna()


df_year[year] = df_year[year] / 1_000_000


df_year_sorted = df_year.sort_values(by=year, ascending=False)


top_n = 20
df_top = df_year_sorted.head(top_n)

plt.figure(figsize=(12, 8))
plt.barh(df_top['Country Name'], df_top[year], color='skyblue')
plt.xlabel('Population (in millions)')
plt.title(f'Top {top_n} Most Populous Countries in {year}')
plt.gca().invert_yaxis()  # Highest first
plt.tight_layout()
plt.show()

 
plt.figure(figsize=(10, 6))
plt.hist(df_year[year], bins=30, color='lightgreen', edgecolor='black')
plt.xlabel('Population (in millions)')
plt.ylabel('Number of Countries')
plt.title(f'Distribution of Country Populations in {year}')
plt.tight_layout()
plt.show()
