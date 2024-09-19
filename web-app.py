from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ema150')
def index():
    # Read the contents of the text file
    with open('./Alerts/ema150.txt', 'r') as file:
        content = file.read()

    # Pass the content to the HTML template
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
