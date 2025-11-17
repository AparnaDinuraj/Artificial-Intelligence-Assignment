# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("covid_19_clean_complete.csv")  # Ensure this file is in your project folder
print("Dataset loaded successfully")
print(df.head())

# Data Cleaning
df['Date'] = pd.to_datetime(df['Date'])  # Convert Date column to datetime
print("Date column type:", df['Date'].dtype)  # Confirm conversion
df.fillna(method='ffill', inplace=True)  # Fill missing values forward
print("Data cleaned")

# Global Trend Over Time
global_trend = df.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum()

plt.figure(num="Global COVID-19 Trends", figsize=(12,6))  # Custom figure title
for col in global_trend.columns:
    plt.plot(global_trend.index, global_trend[col], label=col)

plt.title("Global COVID-19 Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Country-Level Analysis (India)
india = df[df['Country/Region'] == 'India'].groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum()

plt.figure(num="India COVID-19 Trend", figsize=(10,5))  # Custom figure title
plt.plot(india.index, india['Confirmed'], label='Confirmed')
plt.plot(india.index, india['Deaths'], label='Deaths')
plt.plot(india.index, india['Recovered'], label='Recovered')

plt.title("COVID-19 Trend in India")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 10 Countries by Confirmed Cases (latest date)
latest = df[df['Date'] == df['Date'].max()]
top10 = latest.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(10)

plt.figure(num="Top 10 Countries", figsize=(10,6))  # Custom figure title
sns.barplot(x=top10.values, y=top10.index, palette="Reds_r")
plt.title("Top 10 Countries by Confirmed Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Statistical Summary
latest_global = global_trend.iloc[-1]
mortality_rate = latest_global['Deaths'] / latest_global['Confirmed']
recovery_rate = latest_global['Recovered'] / latest_global['Confirmed']

print("\nStatistical Summary:")
print(f"Total Confirmed Cases: {latest_global['Confirmed']:,}")
print(f"Total Deaths: {latest_global['Deaths']:,}")
print(f"Total Recovered: {latest_global['Recovered']:,}")
print(f"Mortality Rate: {mortality_rate:.2%}")
print(f"Recovery Rate: {recovery_rate:.2%}")