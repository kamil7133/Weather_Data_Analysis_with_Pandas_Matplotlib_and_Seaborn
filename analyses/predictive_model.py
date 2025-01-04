import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

def train_and_evaluate_model(df):
    """
    function to train and evaluate a model
    :param data_path: 
        df (pd.DataFrame):
    :return: 
        dict: model evaluation results (MSE and R²).
    """

    required_columns = ['Temperature_C', 'Humidity_pct', 'Precipitation_mm', 'Wind_Speed_kmh', 'Date_Time']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df['Date_Time'] = pd.to_datetime(df['Date_Time'])
    df['day_of_week'] = df['Date_Time'].dt.dayofweek
    df['month'] = df['Date_Time'].dt.month

    X = df[['Humidity_pct', 'Precipitation_mm', 'Wind_Speed_kmh', 'day_of_week', 'month']]
    y = df['Temperature_C']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.xlabel("Real values")
    plt.ylabel("Predicted values")
    plt.title("Comparison of actual and predicted temperature values")
    plt.show()

    return {'mse': mse, 'r2': r2}




