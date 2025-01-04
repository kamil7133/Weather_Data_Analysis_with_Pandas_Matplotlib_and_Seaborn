import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Weather_Data_Analysis_with_Pandas_Matplotlib_and_Seaborn.analyses.trend_analysis import plot_trend_analysis
from Weather_Data_Analysis_with_Pandas_Matplotlib_and_Seaborn.analyses.seasonality_analysis import plot_seasonal_variation
from Weather_Data_Analysis_with_Pandas_Matplotlib_and_Seaborn.analyses.compare_weather_locations import plot_location_comparison
from Weather_Data_Analysis_with_Pandas_Matplotlib_and_Seaborn.analyses.predictive_model import train_and_evaluate_model

df = pd.read_csv('data/weather_data.csv', parse_dates=['Date_Time'])
df = df.dropna()

if __name__ == '__main__':
    #plot_trend_analysis(df)
    #plot_seasonal_variation(df)
    #plot_location_comparison(df)
    results = train_and_evaluate_model(df)
    print(f"Model results:\nMSE: {results['mse']}\nR²: {results['r2']}")
