from flask import *
import pandas as pd


app = Flask(__name__)

@app.route("/")
def hello():
    return("index.html")


@app.route("/index" , method = ['POST'])
def submit():
    if request.method == "POST":



@app.route("/")
def show_tables():
    data = pd.read_excel('toy_datadase.csv')
    data.set_index(['Name'], inplace=True)
    data.index.name=None
  

if __name__ == "__main__":
    app.run(debug=True)