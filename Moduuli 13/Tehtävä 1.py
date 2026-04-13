import flask
from flask import Flask  #tätä mä en tajuu miksei toimi

app = flask.Flask(__name__)

@app.route('/alkuluku/<int:number>')

def check_prime(number):
    is_prime = True
    if number < 2:
        is_prime = False

    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False

                break

    return {"Number": number, "isPrime": is_prime}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)