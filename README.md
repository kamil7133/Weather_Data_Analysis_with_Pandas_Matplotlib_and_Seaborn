# Weather Data Analysis with Pandas and Matplotlib

This project performs comprehensive analysis and visualization of weather data using Pandas, Matplotlib and Seaborn. The code is organized into separate modules for trend analysis, seasonality visualization, and location comparison.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Functionality](#functionality)
- [Future Enhancements](#future-enhancements)

## Project Overview

This project analyzes weather data from a CSV file, providing insights into trends in temperature and precipitation over time, seasonal patterns, and comparisons across different weather locations.

https://www.kaggle.com/datasets/prasad22/weather-data?resource=download
## Technologies Used

- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## File Structure
```
weather_analysis/
├── analyses/
│   ├── compare_weather_locations.py             
│   ├── seasonality_analysis.py        
│   └── trend_analysis.py   
├── data/
│   └── weather_data.csv 
├── png/
├── LICENSE         
├── main.py                           
└── README.md
```


## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/kamil7133/Weather_Data_Analysis_with_Pandas_Matplotlib_and_Seaborn
2. Navigate to the project directory:
   ```bash
   cd Weather_Data_Analysis_with_Pandas_Matplotlib_and_Seaborn
3. Ensure you have all the necessary libraries installed:
    ```
   pip install pandas matplotlib seaborn
4. Run the main script:
    ```
   python main.py
   
## Functionality
### `main.py `
The entry point of the program that imports and runs analysis functions:

- `plot_trend_analysis`: Analyzes and visualizes trends in average temperature and precipitation over time.
- `plot_seasonal_variation`: Visualizes seasonal variations in temperature and precipitation.
- `plot_location_comparison`: Compares weather metrics across different locations using heatmaps.

### `trend_analysis.py`
Contains the `plot_trend_analysis` function, which:
- Processes the weather data to extract yearly and monthly averages.
Generates line plots for average temperature and precipitation trends over time.
![Trend_analysis](png/Trend_analysis.png)

### `seasonality_visualization.py`
Defines the `plot_seasonal_variation` function, which:

- Calculates average temperature and precipitation by season.
- Creates bar plots and box plots to visualize seasonal data.
![Average temperature by Season](png/average_temperature_by_season.png)
![Box Plot of Precipitation by Location](png/box_plot_of_precipitation_by_location.png)

### `compare_weather_locations.py`
Includes the `plot_location_comparison` function, which:
- Aggregates weather data by location and month.
Generates a heatmap to compare average monthly temperatures across different locations.
![Compare weather locations](png/compare_weather_locations.png)

## Future Enhancements
- Additional Metrics: Include analysis for other weather parameters, such as humidity and wind speed.

## Contributing
- Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request
