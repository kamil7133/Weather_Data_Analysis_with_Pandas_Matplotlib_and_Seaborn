import pandas as pd
import matplotlib.pyplot as plt

def plot_trend_analysis(data):
    data['Date_Time'] = pd.to_datetime(data['Date_Time'])
    data['Year'] = data['Date_Time'].dt.year
    data['Month'] = data['Date_Time'].dt.month
    trend_data = data.groupby(['Year', 'Month']).agg({'Temperature_C': 'mean', 'Precipitation_mm': 'mean'}).reset_index()

    trend_data['Date'] = pd.to_datetime(trend_data[['Year', 'Month']].assign(Day=1))

    trend_data = trend_data.round(1)

    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(trend_data['Date'], trend_data['Temperature_C'], color='tomato')
    plt.xlabel('Date time')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Trend of average temperature in time')

    plt.subplot(2, 1, 2)
    plt.plot(trend_data['Date'], trend_data['Precipitation_mm'], color='dodgerblue')
    plt.xlabel('Date time')
    plt.ylabel('Average precipitation (mm)')
    plt.title('Trend of average precipitation in time')

    plt.tight_layout()
    plt.show()


