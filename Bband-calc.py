import pandas as pd
import os

path= './DataBase'

def read_stock_data():
    # Read the stocks data from DataBase
    stocks_list= os.listdir(path)
    all_alerts = []
    for stock in stocks_list:
        df= pd.read_csv(f'{path}/{stock}')
        calculate_rsi(df)
        calculate_bollinger_bands(df)
        alerts= get_alerts(df)
        if alerts is not None:
            ticker = stock.replace('.csv', '')
            alert_message = f"Ticker: {ticker}\n{alerts}\n\n"
            all_alerts.append(alert_message)

        with open('./Alerts/Bband.txt', 'w') as output_file:
            for alert in all_alerts:
                output_file.write(alert)


def calculate_bollinger_bands(df):
    window= 30
    num_std= 2
    # Calculate the Simple Moving Average (Middle Band)
    df['Middle Band'] = df['Close'].rolling(window=window).mean()
    
    # Calculate the rolling standard deviation
    rolling_std = df['Close'].rolling(window=window).std()
    
    # Calculate the Upper and Lower Bollinger Bands
    df['Upper Band'] = df['Middle Band'] + (rolling_std * num_std)
    df['Lower Band'] = df['Middle Band'] - (rolling_std * num_std)
    
def calculate_rsi(df):
    # Calculate daily price changes
    df['change'] = df['Close'].diff()

    # Separate gains and losses
    df['gain'] = df['change'].clip(lower=0)
    df['loss'] = -df['change'].clip(upper=0)

    # Calculate the rolling average of gains and losses
    window_length = 13
    df['avg_gain'] = df['gain'].rolling(window=window_length, min_periods=1).mean()
    df['avg_loss'] = df['loss'].rolling(window=window_length, min_periods=1).mean()

    # Calculate RS (Relative Strength)
    df['rs'] = df['avg_gain'] / df['avg_loss']

    # Calculate RSI
    df['rsi'] = 100 - (100 / (1 + df['rs']))

def get_alerts(df):
    if df['Close'].iloc[-1] < df['Lower Band'].iloc[-1] and df['rsi'].iloc[-1] < 30:
        return (f'{df.iloc[-1]} \nbuy long')
    
    if df['Close'].iloc[-1] > df['Upper Band'].iloc[-1] and df['rsi'].iloc[-1] > 70:
        return (f'{df.iloc[-1]} \nsell short')

if __name__ == "__main__":
    read_stock_data()