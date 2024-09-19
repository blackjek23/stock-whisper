import pandas as pd
import os

path= './DataBase'

def read_stock_data():
    # Read the stocks data from DataBase
    stocks_list= os.listdir(path)
    for stock in stocks_list:
        df= pd.read_csv(f'{path}/{stock}')
        alerts= calculate_bollinger_bands(df)
        if alerts is not None:
            with open('./Alerts/Bband.txt', 'a') as output_file:
            # Write the ticker name and the last row to the alerts file
                ticker= stock.replace('.csv', '')
                output_file.write(f"Ticker: {ticker}\n")
                output_file.write(f"{alerts}\n")
                output_file.write("\n")  # Add a newline for separation between entries

def calculate_bollinger_bands(df):
    window= 15
    num_std= 2
    # Calculate the Simple Moving Average (Middle Band)
    df['Middle Band'] = df['Close'].rolling(window=window).mean()
    
    # Calculate the rolling standard deviation
    rolling_std = df['Close'].rolling(window=window).std()
    
    # Calculate the Upper and Lower Bollinger Bands
    df['Upper Band'] = df['Middle Band'] + (rolling_std * num_std)
    df['Lower Band'] = df['Middle Band'] - (rolling_std * num_std)

    if df['Close'].iloc[-1] < df['Lower Band'].iloc[-2]:
        return (f'{df.iloc[-1]} buy long')

    if df['Close'].iloc[-1] > df['Upper Band'].iloc[-2]:
        return (f'{df.iloc[-1]} sell short')    
    
# Example usage
if __name__ == "__main__":
    read_stock_data()