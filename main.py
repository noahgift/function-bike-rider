from flask import Flask
from flask import jsonify
app = Flask(__name__)

def greedy_change(amount):
    amount = float(amount)
    res = []
    coins = [1,5,10,25]
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    res.append({num:coin_lookup[coin]})
    while rem > 0:
        print(f"This is the num: {num} and this is the rem: {rem}")
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World!'

@app.route('/change/<dollar>/<cents>')
def change(dollar, cents):
    dollar_value = {"dollar":dollar}
    cents_value = {"cents": cents}
    passed_in = [dollar_value,cents_value]
    print(f"These values are passed in {passed_in}")
    res = f"{dollar}.{cents}"
    float_res = float(res)
    change_made = greedy_change(float_res)
    return jsonify(change_made)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)