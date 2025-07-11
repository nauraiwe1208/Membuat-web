from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_date = datetime.now().strftime("%d %B %Y")
    return render_template('index.html', date=current_date)  

if __name__ == '__main__':
    app.run(debug=True) 
