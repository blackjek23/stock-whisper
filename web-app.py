from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page to list available strategies
@app.route('/')
def home():
    strategies = [
        {"name": "EMA150 Strategy", "url": "/ema150"},
        {"name": "Bollinger Bands Strategy", "url": "/bband"},
        # {"name": "New Strategy", "url": "/new_strategy"}  # Add your new strategy here
    ]
    return render_template('home.html', strategies=strategies)

# Route for the EMA150 strategy
@app.route('/ema150')
def ema150():
    # Read the contents of the EMA150 text file
    with open('./Alerts/ema150.txt', 'r') as file:
        content = file.read()

    # Pass the content to the HTML template
    return render_template('strategy.html', strategy_name="EMA150 Strategy", content=content)

# Route for the Bollinger Bands strategy
@app.route('/bband')
def bband():
    # Read the contents of the Bollinger Bands text file
    with open('./Alerts/Bband.txt', 'r') as file:
        content = file.read()

    # Pass the content to the HTML template
    return render_template('strategy.html', strategy_name="Bollinger Bands Strategy", content=content)

# @app.route('/new_strategy')
# def new_strategy():
#     # Read the contents of the new strategy's text file
#     with open('./Alerts/new_strategy.txt', 'r') as file:
#         content = file.read()

#     # Pass the content to the HTML template
#     return render_template('strategy.html', strategy_name="New Strategy", content=content)

if __name__ == '__main__':
    app.run(debug=True)
