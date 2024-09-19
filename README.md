# Stock Whisper

## Description
Stock Whisper is a Python-based application that calculates and tests trading strategies. It downloads historical stock data for a list of tickers, applies various trading strategies, and saves the results. The application includes a Flask web interface to display all the results in a user-friendly format.

## Key Features
- Downloads historical stock data from a predefined list of tickers
- Implements and tests multiple trading strategies
- Saves strategy results for analysis
- Provides a web interface to view all results

## Technologies Used
- Python (main application logic)
- Flask (web interface)
- HTML (web page structure)
- Key libraries: yfinance, pandas, backtrader

## Installation
All required libraries to run Stock Whisper locally are listed in the `requirements.txt` file. To install these dependencies, run:

```
pip install -r requirements.txt
```

## Usage
To run Stock Whisper locally, follow these steps:

1. Ensure all dependencies are installed (see Installation section).
2. Create two directories in the project root:
   - `DataBase`: for storing downloaded stock data
   - `Alerts`: for storing strategy results
3. Run the Python scripts in the following order:
   a. delete.py (to remove old data)
   b. download.py (to fetch fresh stock data)
   c. calc_*.py files (to run all calculation scripts)

### Current Strategies
- EMA (Exponential Moving Average) strategy
- Bollinger Bands strategy

More strategies are planned for future development.

### Modifying Parameters
- To change strategy parameters, modify the 'params' field in the respective calculation (calc) Python files.
- To adjust the time period for testing, update the start and end dates in the download Python file.
- To modify the list of stocks to analyze, edit the stocks text file.

## Dependencies
Key dependencies include:
- yfinance (for downloading stock data)
- pandas (for data manipulation)
- backtrader (for strategy testing)

Refer to `requirements.txt` for a complete list of dependencies.

## Contributing
This is a private project intended for the developer's CV. Contributions are not currently being accepted.

## License
This project is not currently under any specific license.

## Future Plans
- Implementation of additional trading strategies
- Enhanced web interface for result visualization
- Optimization of strategy parameters

---

**Note:** This project is part of a personal portfolio and is not intended for public distribution or use.