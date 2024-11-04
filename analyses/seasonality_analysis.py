import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_season(month):
    if month in [12, 1 ,2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'

def plot_seasonal_variation(data):
    data['Season'] = data['Date_Time'].dt.month.apply(get_season)

    season_data = data.groupby('Season').agg({'Temperature_C': 'mean', 'Precipitation_mm': 'mean'})


    plt.figure(figsize=(10, 5))
    sns.barplot(data=season_data, hue='Season', y='Temperature_C', palette='coolwarm')
    plt.title('Average Temperature by Season')
    plt.ylabel('Average Temperature (°C)')
    plt.xlabel('Season')
    plt.show()


    plt.figure(figsize=(10, 5))
    sns.boxplot(data=data, x='Location', y='Precipitation_mm')
    plt.title('Box Plot of Precipitation by Location')
    plt.xticks(rotation=45)
    plt.show()
