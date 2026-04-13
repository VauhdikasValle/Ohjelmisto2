from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<int:integer>')

def aluku(integer):
    is_prime = True
    if integer < 2:
        is_prime = False

    else:
        for i in range(2, integer):
            if integer % i == 0:
                is_prime = False

                break

    return {"Number": integer, "isPrime": is_prime}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)