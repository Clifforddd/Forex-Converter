from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import Flask, request, render_template,redirect, flash, redirect

app = Flask(__name__)

app.run(debug=True)


@app.route("/", methods=["GET"])
def homepage():
    """Render homepage."""

    return render_template('base.html') 


@app.route("/currency", methods=["POST"])
def currency():
    """Currency converting page"""
    currency1 = request.form["currency1"]
    currency2 = request.form["currency2"]
    amount = request.form["amount"]
  

    s = CurrencyCodes()
    c = CurrencyRates()

    
    symbol = s.get_symbol(currency2)


    result = c.convert(currency1, currency2, int(amount))
    return render_template('currency.html', result=result, symbol=symbol)


