import os 

def delete_stocks_data():
    with open('stocks.txt', 'r') as f:
        for ticker in f:
            Symbol = ticker.strip()
            file_name = f'{Symbol}.csv'
            os.remove(f'./DataBase/{file_name}') 
            
if __name__ == "__main__":
    delete_stocks_data()
