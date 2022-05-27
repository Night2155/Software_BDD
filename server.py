from flask import Flask, render_template, request
from calc import calculator
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Calculator.html")


@app.route('/calculate', methods=['POST'])  # javascript 傳值處理
def get_Value():
    value = request.data
    ans = calculator(value)
    return str(ans)


if __name__ == "__main__":
    app.run(debug=True, port=2022)
