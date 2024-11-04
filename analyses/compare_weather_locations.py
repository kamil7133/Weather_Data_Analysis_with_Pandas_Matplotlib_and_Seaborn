import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_location_comparison(data):
    data['Date_Time'] = pd.to_datetime(data['Date_Time'])
    data['Year'] = data['Date_Time'].dt.year
    data['Month'] = data['Date_Time'].dt.month

    location_compare = data.groupby(['Location', 'Month']).agg({'Temperature_C': 'mean', 'Precipitation_mm': 'mean'}).reset_index()

    heatmap_data = location_compare.pivot(index='Location', columns='Month', values='Temperature_C')

    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='coolwarm', cbar_kws={'label': 'Average Temperature (°C)'})

    plt.title('Heatmap of Average Monthly Temperatures by Location')
    plt.xlabel('Month')
    plt.ylabel('Location')
    plt.xticks(ticks=[i + 0.5 for i in range(5)],
               labels=['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    plt.tight_layout()
    plt.show()

