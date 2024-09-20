import pandas as pd
import os

path= './DataBase'

def read_stock_data():
    # Read the stocks data from DataBase
    stocks_list= os.listdir(path)
    all_alerts = []
    for stock in stocks_list:
        df= pd.read_csv(f'{path}/{stock}')
        alerts= detect_ema_cross(df)
        if alerts is not None:
            ticker = stock.replace('.csv', '')
            alert_message = f"Ticker: {ticker}\n{alerts.to_string()}\n\n"
            all_alerts.append(alert_message)

        with open('./Alerts/ema150.txt', 'w') as output_file:
            for alert in all_alerts:
                output_file.write(alert)

def detect_ema_cross(df):
    # Calculate the 150 EMA
    df['150_EMA'] = df['Close'].ewm(span=150, adjust=False).mean()

    # Calculate when the close price crosses above or below the 150 EMA
    df['Cross_Up'] = (df['Close'].shift(1) < df['150_EMA'].shift(1)) & (df['Close'] > df['150_EMA'])
    df['Cross_Down'] = (df['Close'].shift(1) > df['150_EMA'].shift(1)) & (df['Close'] < df['150_EMA'])

    # Save Alerts
    if df['Cross_Up'].iloc[-1]:
        return (df.iloc[-1])

    if df['Cross_Down'].iloc[-1]:
        return (df.iloc[-1])

if __name__ == "__main__":
    read_stock_data()